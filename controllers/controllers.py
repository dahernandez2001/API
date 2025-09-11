from flask import Blueprint, request, jsonify, abort

def create_director_controller(service):
    bp = Blueprint('directors', __name__)

    @bp.route('/directors', methods=['GET'])
    def get_directors():
        directors = service.get_all()
        return jsonify([d.to_dict() for d in directors])

    @bp.route('/directors/<int:id_>', methods=['GET'])
    def get_director(id_):
        director = service.get_by_id(id_)
        if not director:
            abort(404, "Director not found")
        return jsonify(director.to_dict())

    @bp.route('/directors', methods=['POST'])
    def create_director():
        data = request.json
        if not data or 'name' not in data:
            abort(400, "Name is required")
        director = service.create(data['name'])
        if not director:
            abort(500, "Failed to create director")
        return jsonify(director.to_dict()), 201

    @bp.route('/directors/<int:id_>', methods=['PUT'])
    def update_director(id_):
        data = request.json
        if not data or 'name' not in data:
            abort(400, "Name is required")
        director = service.update(id_, data['name'])
        if not director:
            abort(404, "Director not found or update failed")
        return jsonify(director.to_dict())

    @bp.route('/directors/<int:id_>', methods=['DELETE'])
    def delete_director(id_):
        director = service.delete(id_)
        if not director:
            abort(404, "Director not found or delete failed")
        return jsonify({"result": True})

    return bp

def create_movie_controller(service, director_service):
    bp = Blueprint('movies', __name__)

    @bp.route('/movies', methods=['GET'])
    def get_movies():
        movies = service.get_all()
        res = []
        for m in movies:
            d = director_service.get_by_id(m.director_id)
            movie_dict = m.to_dict()
            movie_dict['director_name'] = d.name if d else None
            res.append(movie_dict)
        return jsonify(res)

    @bp.route('/movies/<int:id_>', methods=['GET'])
    def get_movie(id_):
        movie = service.get_by_id(id_)
        if not movie:
            abort(404, "Movie not found")
        d = director_service.get_by_id(movie.director_id)
        movie_dict = movie.to_dict()
        movie_dict['director_name'] = d.name if d else None
        return jsonify(movie_dict)

    @bp.route('/movies', methods=['POST'])
    def create_movie():
        data = request.json
        if not data or not all(k in data for k in ('title', 'year', 'director_id')):
            abort(400, "title, year and director_id are required")
        movie = service.create(data['title'], data['year'], data['director_id'])
        if not movie:
            abort(400, "Director does not exist or movie creation failed")
        return jsonify(movie.to_dict()), 201

    @bp.route('/movies/<int:id_>', methods=['PUT'])
    def update_movie(id_):
        data = request.json
        if not data:
            abort(400)
        movie = service.update(
            id_,
            title=data.get('title'),
            year=data.get('year'),
            director_id=data.get('director_id')
        )
        if not movie:
            abort(404, "Movie not found or update failed")
        return jsonify(movie.to_dict())

    @bp.route('/movies/<int:id_>', methods=['DELETE'])
    def delete_movie(id_):
        movie = service.delete(id_)
        if not movie:
            abort(404, "Movie not found or delete failed")
        return jsonify({"result": True})

    return bp
