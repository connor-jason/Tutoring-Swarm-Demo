from swarm import Swarm, Agent
import dotenv

dotenv.load_dotenv()

# Initialize the Swarm client
client = Swarm()

# Define the transfer functions for handoffs between subjects
def transfer_to_math_agent():
    print("Switching to Math Agent...")
    return math_agent

def transfer_to_history_agent():
    print("Switching to History Agent...")
    return history_agent

def transfer_to_science_agent():
    print("Switching to Science Agent...")
    return science_agent

def transfer_to_english_agent():
    print("Switching to English Agent...")
    return english_agent

# Define the agents for different subjects
math_agent = Agent(
    name="Math Agent",
    instructions="""You are a Math tutor. Help students with math-related questions. 
    You can solve problems, explain concepts, and help the student understand the steps.""",
    functions=[transfer_to_history_agent, transfer_to_science_agent],
)

history_agent = Agent(
    name="History Agent",
    instructions="""You are a History tutor. Help students with questions about history. 
    You can explain historical events, important figures, and help with understanding timelines and causes.""",
    functions=[transfer_to_math_agent, transfer_to_science_agent],
)

science_agent = Agent(
    name="Science Agent",
    instructions="""You are a Science tutor. Help students with questions about science. 
    You can explain concepts from physics, chemistry, biology, or other scientific areas.""",
    functions=[transfer_to_math_agent, transfer_to_history_agent],
)

english_agent = Agent(
    name="English/Writing Agent",
    instructions="""You are an English/Writing tutor. Help students with questions related to English grammar, writing, essay feedback, and other writing-related topics.""",
    functions=[transfer_to_math_agent, transfer_to_history_agent, transfer_to_science_agent],
)

# Define a Router Agent to direct the student's question to the right subject agent
def router_instructions(context_variables):
    """This function helps direct the student to the right subject based on their query."""
    return "You are the Question Router. Your task is to route the question to the correct subject agent (Math, History, or Science)."

question_router = Agent(
    name="Question Router",
    instructions=router_instructions,
    functions=[transfer_to_math_agent, transfer_to_history_agent, transfer_to_science_agent, transfer_to_english_agent],
)

# Simulate a conversation where a user asks a question
context_variables = {
    "student_name": "Connor"
}

# Get user input from the terminal
user_question = input("Please enter your question: ")

# User input will be routed by the Question Router
response = client.run(
    agent=question_router,
    messages=[{"role": "user", "content": user_question}],
    context_variables=context_variables
)

# Print the final response from the relevant subject agent
print("Answer:", response.messages[-1]["content"])
