"""empty message

Revision ID: e5e60462867d
Revises: 
Create Date: 2022-11-29 21:05:34.725347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5e60462867d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Payment_Methods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Debts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creditor', sa.String(length=150), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id_payment_methods', sa.Integer(), nullable=True),
    sa.Column('number_installments', sa.String(length=60), nullable=True),
    sa.Column('installment_value', sa.Float(), nullable=True),
    sa.Column('initial_date', sa.Date(), nullable=True),
    sa.Column('final_date', sa.Date(), nullable=True),
    sa.Column('pay', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_payment_methods'], ['Payment_Methods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Debt_Installment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_debt', sa.Integer(), nullable=True),
    sa.Column('installment_value', sa.Float(), nullable=True),
    sa.Column('payment_date', sa.Date(), nullable=True),
    sa.Column('installment_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_debt'], ['Debts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Debt_Installment')
    op.drop_table('Debts')
    op.drop_table('Users')
    op.drop_table('Payment_Methods')
    # ### end Alembic commands ###
