"""first migration

Revision ID: 3fd7ae6327c4
Revises: 
Create Date: 2024-08-22 23:21:00.026570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fd7ae6327c4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.Column('rooms_count', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('houses')
    # ### end Alembic commands ###
