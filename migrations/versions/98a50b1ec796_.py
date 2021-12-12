"""empty message

Revision ID: 98a50b1ec796
Revises: 9afddbd15070
Create Date: 2021-12-13 00:11:42.936043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a50b1ec796'
down_revision = '9afddbd15070'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'media')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('media', sa.BLOB(), nullable=True))
    # ### end Alembic commands ###