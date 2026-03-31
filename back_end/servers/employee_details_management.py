from fastmcp import FastMCP
from models.employees import employee
from database import postgresql_con as postgres
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from prompts.query_generation_prompt import generate_query_system_prompt


load_dotenv()
edm = FastMCP("employee_details_management")


@edm.tool
def get_employee_details():
    """
    get the details of the employee
    """

    # model = init_chat_model(
    #     "microsoft/Phi-3-mini-4k-instruct",
    #     model_provider="huggingface",
    #     temperature=0.7,
    #     max_tokens=1024,
    # )
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto",  # let Hugging Face choose the best provider for you
    )

    model = ChatHuggingFace(llm=llm)

    llmchain = generate_query_system_prompt | model  # | StrOutputParser()

    response = llmchain.invoke({"query": "what is the email of Alexander"})
    print(response)

    # query = "select * from employees LIMIT 5"
    # result = postgres.get_employee_details(query)
    # print(result)


if __name__ == "__main__":
    get_employee_details()
