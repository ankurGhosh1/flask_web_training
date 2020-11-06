from ma import ma
from models.loan import LoanModel
from models.agent import AgentModel


class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoanModel
        load_only = ("agent",)
        load_instance = True
        include_fk = True