"""crate post table

Revision ID: 95d4a0fccf54
Revises: 
Create Date: 2021-12-23 22:29:37.480245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d4a0fccf54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column(
        'id', sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False)
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
