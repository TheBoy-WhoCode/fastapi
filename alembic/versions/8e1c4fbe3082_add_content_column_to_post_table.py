"""add content column to post table

Revision ID: 8e1c4fbe3082
Revises: 95d4a0fccf54
Create Date: 2021-12-23 22:39:22.841329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1c4fbe3082'
down_revision = '95d4a0fccf54'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
