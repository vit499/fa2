"""flat

Revision ID: 6e8a2a0e7a74
Revises: 625e75ffb4cb
Create Date: 2023-08-07 13:53:20.881217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e8a2a0e7a74'
down_revision = '625e75ffb4cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param1', sa.String(), nullable=True),
    sa.Column('param2', sa.String(), nullable=True),
    sa.Column('param3', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_flats_id'), 'flats', ['id'], unique=False)
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param1', sa.String(), nullable=True),
    sa.Column('param2', sa.String(), nullable=True),
    sa.Column('param3', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['flats.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rooms_id'), 'rooms', ['id'], unique=False)
    op.create_table('dots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param1', sa.String(), nullable=True),
    sa.Column('param2', sa.String(), nullable=True),
    sa.Column('param3', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dots_id'), 'dots', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dots_id'), table_name='dots')
    op.drop_table('dots')
    op.drop_index(op.f('ix_rooms_id'), table_name='rooms')
    op.drop_table('rooms')
    op.drop_index(op.f('ix_flats_id'), table_name='flats')
    op.drop_table('flats')
    # ### end Alembic commands ###