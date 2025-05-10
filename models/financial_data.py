from . import db

class FinancialData(db.Model):
    __tablename__ = 'financial_data'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    expenses = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<FinancialData {self.month}>'
