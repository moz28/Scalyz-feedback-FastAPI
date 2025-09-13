"""Initial migration - Create feedbacks table

Revision ID: 001
Revises: 
Create Date: 2024-12-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create feedbacks table
    op.create_table(
        'feedbacks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=100), nullable=True, comment='User name (optional)'),
        sa.Column('email', sa.String(length=255), nullable=True, comment='User email (optional)'),
        sa.Column('message', sa.Text(), nullable=False, comment='Feedback message (required)'),
        sa.Column(
            'created_at', 
            sa.DateTime(timezone=True), 
            server_default=sa.text('now()'), 
            nullable=False,
            comment='Timestamp when feedback was created'
        ),
        sa.PrimaryKeyConstraint('id'),
        comment='Table for storing user feedback'
    )
    
    # Create index on id column for faster queries
    op.create_index(op.f('ix_feedbacks_id'), 'feedbacks', ['id'], unique=False)
    
    # Create index on created_at for ordering
    op.create_index(op.f('ix_feedbacks_created_at'), 'feedbacks', ['created_at'], unique=False)


def downgrade() -> None:
    # Drop indexes
    op.drop_index(op.f('ix_feedbacks_created_at'), table_name='feedbacks')
    op.drop_index(op.f('ix_feedbacks_id'), table_name='feedbacks')
    
    # Drop table
    op.drop_table('feedbacks')