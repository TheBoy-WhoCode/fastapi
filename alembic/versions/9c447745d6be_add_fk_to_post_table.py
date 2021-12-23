"""add FK to post table

Revision ID: 9c447745d6be
Revises: b73198f4e99e
Create Date: 2021-12-23 22:52:01.863602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c447745d6be'
down_revision = 'b73198f4e99e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column("owner_id",
                            sa.Integer, nullable=False),
                  )
    op.create_foreign_key("post_users_fk", source_table="posts",
                          referent_table="users", local_cols=["owner_id"], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id ')
    pass
