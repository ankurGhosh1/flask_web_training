from db import db

class LoanModel(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False,)
    amount = db.Column(db.Integer, nullable=False,)

    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False,)
    agent = db.relationship('AgentModel')

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()