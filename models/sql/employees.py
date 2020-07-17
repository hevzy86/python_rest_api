#
# Model Employees
#
from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean, Sequence
from sqlalchemy import BigInteger, Date, DateTime, Float, Numeric, Unicode, Text
from employees.lib.powlib import relation
from employees.database.sqldblib import Base
from employees.lib.powlib import PowBaseMeta
from sqlalchemy import schema
from sqlalchemy.sql.sqltypes import NULLTYPE
import enum
from sqlalchemy import Integer

# @relation.has_many("<plural_other_models>")
@relation.setup_sql_schema()
class Employees(Base, metaclass=PowBaseMeta):

    #
    # cerberus style schema
    #
    schema = {
        'emp_no':   {'type': 'integer',
                     "sql":
                     {
                         "primary_key": True,
                         "default": NULLTYPE,
                         "unique": True,
                         "nullable": True
                     }, },
        'birth_date':   {'type': 'datetime', "sqltype": "date"},
        'first_name':   {'type': 'string', 'maxlength': 14},
        'last_name':   {'type': 'string', 'maxlength': 16},
        'gender':   {'type': 'string', "allowed": ["M", "F"],  "sqltype": "enum"},
        'hire_date':   {'type': 'datetime', "sqltype": "date"}

    }


    # if you want to define a custom tablename for this model:
    __tablename__ = "employees"


# if you dont want to use the pow schema extension
_use_pow_schema_attrs = False

# define class attributes/variables here that should be included in to_dict()
# conversion and also handed to the encoders but that are NOT part of the schema.
include_attributes = []

# Add sqlalchemy table_args here. Add "autoload" : True for database reflection
__table_args__ = {"extend_existing": True}

#
# init
#


def __init__(self, **kwargs):
    self.setup_instance_values()
    self.init_on_load(**kwargs)
    #
    # your model's methods down here
    #
