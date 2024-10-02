"""empty message

Revision ID: f15d3ab8e313
Revises: 7dd05e7b526f
Create Date: 2024-10-01 11:03:58.583570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f15d3ab8e313'
down_revision = '7dd05e7b526f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partners', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('nif',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('ciudad',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('sector',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partners', schema=None) as batch_op:
        batch_op.alter_column('sector',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('ciudad',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('nif',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###
