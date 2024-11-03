from secret_key import GROQ_API_KEY
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain



llm = ChatGroq(
    temperature = 0,
    groq_api_key=GROQ_API_KEY,
    model_name="gemma-7b-it"
)#Sequential chain template



def get_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
                                        input_variables={'cuisine'},
                                        template = "I want to open a restaurant for {cuisine} food.Suggest only one fency name for this."
                                    )
    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key="Restaurant_name")


    prompt_template_items = PromptTemplate(
                                            input_variables={'Restaurant_name'},
                                            template = "Suggest me 10 menu items for {Restaurant_name} and also do not show the numbers of the items.only menu items not there description."
                                        )
    food_items_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['Restaurant_name','menu_items'],
        verbose=True
        )
    response = chain.invoke({'cuisine': cuisine})
    return response

if __name__ == "__main__":
       print(get_restaurant_name_and_items("Italian"))
