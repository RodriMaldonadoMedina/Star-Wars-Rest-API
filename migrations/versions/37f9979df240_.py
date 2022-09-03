"""empty message

Revision ID: 37f9979df240
Revises: 8b348cb5fa6c
Create Date: 2022-09-02 17:15:14.707475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f9979df240'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
