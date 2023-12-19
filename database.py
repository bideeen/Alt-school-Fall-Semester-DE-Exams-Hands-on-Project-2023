# 
import uuid
from datetime import datetime



# The Expense Class
class Expense:

    def __init__(self, title, amount) -> None:
        self.id =  str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at       


