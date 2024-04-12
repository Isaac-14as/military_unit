"""Init

Revision ID: eb79a2212527
Revises: 
Create Date: 2024-04-12 03:41:40.167497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb79a2212527'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    job_title_table = op.create_table('job_title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    rank_table = op.create_table('rank',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    subdivision_table = op.create_table('subdivision',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subdivision_id', sa.Integer(), nullable=False),
    sa.Column('job_title_id', sa.Integer(), nullable=False),
    sa.Column('rank_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('cabinet', sa.Integer(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('nfc_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_title.id'], ondelete='SET NUll'),
    sa.ForeignKeyConstraint(['rank_id'], ['rank.id'], ondelete='SET NUll'),
    sa.ForeignKeyConstraint(['subdivision_id'], ['subdivision.id'], ondelete='SET NUll'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nfc_id'),
    sa.UniqueConstraint('phone')
    )
    data_job_title = [
        {'name': 'командир'},
        {'name': 'зам командира'},
        {'name': 'нач штаба'},
        {'name': 'зам нач штаба'},
        ]
    data_rank = [
        {'name': 'прапорщик'},
        {'name': 'старший прапорщик'},
        {'name': 'младший лейтенант'},
        {'name': 'лейтенант'},
        {'name': 'старший лейтенант'},
        {'name': 'капитан'},
        {'name': 'майор'},
        {'name': 'подполковник'},
        {'name': 'полковник'},
    ]
    data_subdivision = [
        {'name': 'командование'},
        {'name': 'штаб'},
        {'name': 'служба горючего'},
        {'name': 'прод служба'},
        ]
    op.bulk_insert(job_title_table, data_job_title)
    op.bulk_insert(rank_table, data_rank)
    op.bulk_insert(subdivision_table, data_subdivision)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    op.drop_table('subdivision')
    op.drop_table('rank')
    op.drop_table('job_title')
    # ### end Alembic commands ###