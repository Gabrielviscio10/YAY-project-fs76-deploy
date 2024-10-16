"""empty message

Revision ID: f2682f77aa1b
Revises: 
Create Date: 2024-10-17 09:21:24.189418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2682f77aa1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entidades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('intereses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('descripcion', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=True),
    sa.Column('apellidos', sa.String(length=120), nullable=True),
    sa.Column('foto', sa.String(length=255), nullable=True),
    sa.Column('foto_perfil', sa.String(length=255), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('breve_descripcion', sa.String(length=255), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('latitud', sa.Float(), nullable=True),
    sa.Column('longitud', sa.Float(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('partners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=True),
    sa.Column('nif', sa.String(length=120), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('latitud', sa.Float(), nullable=True),
    sa.Column('longitud', sa.Float(), nullable=True),
    sa.Column('sector', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('entidad_id', sa.Integer(), nullable=True),
    sa.Column('foto', sa.String(length=255), nullable=True),
    sa.Column('foto_perfil', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['entidad_id'], ['entidades.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('usuarios_intereses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('interes_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interes_id'], ['intereses.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('hora_inicio', sa.Time(), nullable=True),
    sa.Column('hora_fin', sa.Time(), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('latitud', sa.Float(), nullable=True),
    sa.Column('longitud', sa.Float(), nullable=True),
    sa.Column('breve_descripcion', sa.String(length=120), nullable=True),
    sa.Column('accesibilidad', sa.Boolean(), nullable=True),
    sa.Column('dificultad', sa.String(length=120), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('cupo', sa.Integer(), nullable=True),
    sa.Column('observaciones', sa.String(length=120), nullable=True),
    sa.Column('foto_evento', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('partner_id', sa.Integer(), nullable=True),
    sa.Column('partner_nombre', sa.String(length=120), nullable=True),
    sa.Column('interes_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interes_id'], ['intereses.id'], ),
    sa.ForeignKeyConstraint(['partner_id'], ['partners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('imagenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('partner_email', sa.String(length=120), nullable=True),
    sa.Column('es_perfil', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['partner_email'], ['partners.email'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inscripciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_registro', sa.String(length=120), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('evento_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['evento_id'], ['eventos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inscripciones')
    op.drop_table('imagenes')
    op.drop_table('eventos')
    op.drop_table('usuarios_intereses')
    op.drop_table('partners')
    op.drop_table('usuarios')
    op.drop_table('user')
    op.drop_table('intereses')
    op.drop_table('entidades')
    # ### end Alembic commands ###
