"""empty message

Revision ID: ed82f4cec1b9
Revises: f8635590b444
Create Date: 2024-10-17 09:46:01.133477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed82f4cec1b9'
down_revision = 'f8635590b444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id_perfil', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_column('public_id_perfil')

    # ### end Alembic commands ###
