def greet():
    print("Hi")
    print("Here's your Med Agent")

def takeInput():
    userInput = input("Enter your symptom:")
    print(userInput)
    return userInput

class ChatGpt_LLM:
    def __init__(self, model_name):
       self.model_name = model_name 

    def generateResponse(self, prompt):
        # call openai api to get response based on the prompt
        # openai url
        # openai key 
        # make http call
        return "This is a dummy response from " + self.model_name   



class Gemini_LLM:
    def __init__(self, model_name):
       self.model_name = model_name 

    def generateResponse(self, prompt):
        # call gemini api to get response based on the prompt
        # gemini url
        # gemini key 
        # make http call
        return "This is a dummy response from " + self.model_name   

class Practo_Tool:
    def __init__(self, name):
        self.name = name

    def useTool(self, input):
        # api url
        # api key
        # http call
        print("Using tool " + self.name + " with input " + input)


class Messanger_Tool:
    def __init__(self, name):
        self.name = name        

    def useTool(self, input):
        # api url
        # api key
        # http call
        print("Using tool "+ self.name + " with input " + input)
class Agent:
    def __init__(self, name, llm, tool):
        self.name = name
        self.llm = llm 
        self.tool = tool

    def giveAdvice(self, symptom):
        # llm = ChatGpt_LLM("gpt-4")
        response = llm.generateResponse("Provide advice for the symptom:" + symptom)
        print("Advice for " + symptom + ": " + response)

    def takeAction(self, tool, input):
        tool.useTool(input)  

    def giveAdviceAndTakeAction(self, symptom):
        self.giveAdvice(symptom)
        self.takeAction(symptom) 

class AutoAgent:
    def __init__(self, name, llm, tool, prompt):
        self.name = name 
        self.llm = llm
        self.tool = tool
        self.prompt = prompt

    def decideToUseTool(self, response):
        # logic to decide whether to use tool based on response
        if "visit doctor" in response:
            return True
        return False 

    def execute(self):
        response = llm.generateResponse(self.prompt)
        if(self.decideToUseTool(response)):
            tool.useTool(symptom) 
        else:
            print("no action needed")


    chatMessages = []

    inquiryAgent = AutoAgent("AutoHealthBotGemini", Gemini_LLM("gemini-1"), Messanger_Tool("MessangerAPI"), "Ask questions to understand the problem in detail" + chatMessages) 
    inquiryAgent.execute()       

    advisorAgent = AutoAgent("AutoHealthBot", ChatGpt_LLM("gpt-4"), Practo_Tool("PractoAPI"), "Provide advice for the problem: " + chatMessages)
    advisorAgent.execute()

class Manager:
    def __init__(self, name, agents):
            self.name = name
            self.agents = agents

    def coordinate(self, symptom):
            for agent in self.agent:
                agent.execute()  







greet()
name="Supriyo"
age=20

symptomList = [{
    "name": "cough",
    "severity": "mild",
    "duration": "2 days",
    "priority": 1
},
{
 "name": "fever",
 "severity": "high",
 "duration": "5 days",
 "priority": 2
 },
 {
    "name": "headache",
    "severity": "low",
    "duration": "1 day",
    "priority": 2
 }]

# print("hi")
# print(name)
# # print(symptomList)
# # print(symptomList[0])

# for symptom in symptomList:
#     if(symptom["priority"] == 2):
#         print(symptom["name"])
#         print(symptom["priority"])


symptom = takeInput()

llm = ChatGpt_LLM("gpt-4")
tool = Practo_Tool("PractoAPI")
agent = Agent("HealthBot1.0", llm, tool)
agent.giveAdvice(symptom)

print("Thankyou for using our bot")


