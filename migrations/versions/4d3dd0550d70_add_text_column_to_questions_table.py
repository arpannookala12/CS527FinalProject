"""add text column to questions table

Revision ID: 4d3dd0550d70
Revises: fe41bb8e7e41
Create Date: 2025-05-01 13:18:10.287143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d3dd0550d70'
down_revision = 'fe41bb8e7e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=True))
        batch_op.drop_column('is_answered')
        batch_op.drop_column('question_text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_text', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('is_answered', sa.BOOLEAN(), server_default=sa.text("'0'"), nullable=True))
        batch_op.drop_column('status')
        batch_op.drop_column('text')

    # ### end Alembic commands ###
