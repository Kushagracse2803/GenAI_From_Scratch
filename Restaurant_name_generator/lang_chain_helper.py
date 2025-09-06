from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI
from secret_key_gem import gemini_key

# ✅ Define LLM first
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=gemini_key,
    temperature=0.7
)

# ✅ Prompt templates
name_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="Suggest a fancy name for an {cuisine} restaurant."
)

menu_prompt = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest some menu items for a restaurant named {restaurant_name}."
)

# ✅ Chains
name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="restaurant_name")
menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu_items")

# ✅ Sequential Chain
restaurant_chain = SequentialChain(
    chains=[name_chain, menu_chain],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"]
)

# ✅ Exposed function
def generate_restaurant_name(cuisine):
    return restaurant_chain({"cuisine": cuisine})
