"""add remainig post column

Revision ID: 903e912a5167
Revises: 9c447745d6be
Create Date: 2021-12-23 23:04:18.235113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '903e912a5167'
down_revision = '9c447745d6be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column("published",
                            sa.Boolean, server_default="True", nullable=False),

                  )
    op.add_column("posts", sa.Column("created_at",
                                     sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
                                     ))

    pass


def downgrade():
    op.drop_column('posts', "published")
    op.drop_column('posts', "created_at")
    pass
