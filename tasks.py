from robocorp.tasks import task
from robocorp import vault, storage, excel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
import json

@task
def compare_addresses():
    addresses = excel.open_workbook("addresses.xlsx").worksheet("Sheet1").as_list(header=True)

    openai_credentials = vault.get_secret("OpenAI")
    llm = ChatOpenAI(openai_api_key=openai_credentials["key"])

    template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=("You are a helpful assistant that compares addresses for the user.")),
            HumanMessagePromptTemplate.from_template(storage.get_text("example_prompt_template")),
        ]
    )

    for row in addresses:
        print(f"\nComparing addresses: {row['First address']} to {row['Second address']}.")
        response = llm(template.format_messages(address_one=row["First address"], address_two=row["Second address"]))
        response_json = json.loads(response.content)
        print(f"RESULT: {response_json['result']}, because {response_json['reason']}")
