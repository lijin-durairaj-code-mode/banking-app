from pydantic import BaseModel, Field
from typing import Annotated, Optional
from datetime import date


class employee(BaseModel):
    firstname: Annotated[
        Optional[str], Field(default=None, description="first name of the employee")
    ]
    lastname: Annotated[
        Optional[str], Field(default=None, description="last name of the employee")
    ]
    employee_id: Annotated[
        Optional[str], Field(default=None, description="employee id of the employee")
    ]

    email: Annotated[
        Optional[str], Field(default=None, description="email of the employee")
    ]
    phone: Annotated[
        Optional[str], Field(default=None, description="phone number of the employee")
    ]
    city: Annotated[
        Optional[str],
        Field(default=None, description="city of the employee where he stays or works"),
    ]
    state: Annotated[
        Optional[str],
        Field(
            default=None, description="state of the employee where he stays or works"
        ),
    ]
    country: Annotated[
        Optional[str],
        Field(
            default=None, description="country of the employee where he stays or works"
        ),
    ]
    department: Annotated[
        Optional[str], Field(default=None, description="department of the employee")
    ]
    designation: Annotated[
        Optional[str], Field(default=None, description="designation of the employee")
    ]
    role: Annotated[
        Optional[str], Field(default=None, description="role of the employee")
    ]
    date_of_birth: Annotated[
        Optional[date], Field(default=None, description="date of birth of the employee")
    ]
    date_of_joining: Annotated[
        Optional[date],
        Field(default=None, description="date of joining of the employee"),
    ]
    years_of_experience: Annotated[
        Optional[str],
        Field(default=None, description="employees total years of experience"),
    ]
    manager_id: Annotated[
        Optional[str], Field(default=None, description="employees manager id")
    ]
    salary: Annotated[
        Optional[str], Field(default=None, description="salary of the employee")
    ]
    skills: Annotated[
        Optional[str],
        Field(
            default=None,
            description="skills which the employee knows or currenlty working / learning on",
        ),
    ]
    emergency_contact_details: Annotated[
        Optional[str],
        Field(default=None, description="emergency contact details of the employee"),
    ]
    married: Annotated[
        Optional[str], Field(default=None, description="marital status of the employee")
    ]
