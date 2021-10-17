from flask_restx import Model, fields


user_model = Model('User', {
    'id': fields.Integer(readonly=True, description='Identificador único do usuário'),
    'email': fields.String(required=True, description='E-mail do usuário')
})

post_model = Model('Post', {
    'id': fields.Integer(readonly=True, description='Identificador único do post'),
    'title': fields.String(required=True, description='Título do post'),
    'body': fields.String(required=True, description='Corpo do post em Markdown'),
    'user': fields.Nested(user_model, description='Criador do post')
})

comment_model = Model('Comment', {
    'id': fields.Integer(readonly=True, description='Identificador único do comentário'),
    'body': fields.String(required=True, description='Corpo do comentário'),
    'user': fields.Nested(user_model, required=True, description='Criador do comentário'),
    'post': fields.Nested(post_model, required=True, description='Post comentado')
})

delete_comment_model = Model('Comment', {
    'id': fields.Integer(readonly=True, description='Identificador único do comentário'),
    'body': fields.String(required=True, description='Corpo do comentário'),
    'post_id': fields.Integer(readonly=True, description='Identificador único do post'),
})

_post_comment_model = Model('PostComment', {
    'id': fields.Integer(readonly=True, description='Identificador único do comentário'),
    'body': fields.String(required=True, description='Corpo do comentário'),
    'user': fields.Nested(user_model, required=True, description='Criador do comentário')
})

commented_post_model = Model('CommentedPost', {
    'id': fields.Integer(readonly=True, description='Identificador único do post'),
    'title': fields.String(required=True, description='Título do post'),
    'body': fields.String(required=True, description='Corpo do post em Markdown'),
    'user': fields.Nested(user_model, description='Criador do post'),
    'comments': fields.List(fields.Nested(_post_comment_model), description='Comentários do post')
})
