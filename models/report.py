from . import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)  # e.g., 'Income Statement', 'Balance Sheet'
    generated_date = db.Column(db.DateTime, nullable=False)
    data = db.Column(db.Text, nullable=False)  # This could be JSON data representing the report

    def __repr__(self):
        return f'<Report {self.report_type}>'
