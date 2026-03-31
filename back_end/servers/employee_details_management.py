from fastmcp import FastMCP
from models.employees import employee

edm = FastMCP("employee_details_management")


@edm.tool
def get_employee_details():
    """
    get the details of the employee
    """
