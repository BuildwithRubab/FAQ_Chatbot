
import streamlit as st

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 FAQ Chatbot")
st.write("Ask me anything! I can answer questions about programming, AI, studies, careers, science, general knowledge and more.")

faqs = {
    # AI and Technology
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "what is artificial intelligence": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "who invented ai": "Artificial Intelligence was developed through the contributions of many researchers. John McCarthy is widely known for coining the term Artificial Intelligence in 1956.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn from data.",
    "what is machine learning used for": "Machine Learning is used in recommendation systems, fraud detection, image recognition and predictions.",
    "what is deep learning": "Deep Learning is a branch of machine learning that uses neural networks with multiple layers.",
    "what is generative ai": "Generative AI is a type of AI that creates new content such as text, images, music and videos.",
    "what is chatgpt": "ChatGPT is an AI chatbot developed by OpenAI that can understand and generate human-like text.",
    "what is chatgpt used for": "ChatGPT can help with learning, writing, brainstorming, coding, research and problem-solving.",
    "what is an llm": "LLM stands for Large Language Model. It is an AI model trained on large amounts of text.",
    "what is nlp": "Natural Language Processing enables computers to understand and process human language.",
    "what is computer vision": "Computer Vision enables computers to interpret and understand images and videos.",
    "what is robotics": "Robotics is a field of technology that deals with designing, building and operating robots.",
    "what is an ai tool": "An AI tool is software that uses artificial intelligence to perform tasks such as writing, analysis and translation.",
    "what is prompt engineering": "Prompt Engineering is the process of designing effective instructions to get useful responses from AI models.",
    "what is an ai agent": "An AI agent is a system that can perceive information, make decisions and perform tasks to achieve a goal.",
    "what is automation": "Automation is the use of technology to perform tasks with minimal human intervention.",
    "what is n8n": "n8n is a workflow automation platform that connects applications and automates tasks.",
    "what is hugging face": "Hugging Face is a platform that provides tools, datasets and models for machine learning and AI development.",
    "what is an ai model": "An AI model is a computer system trained on data to recognize patterns, make predictions or generate content.",
    "what is an llm chatbot": "An LLM chatbot uses a Large Language Model to understand questions and generate human-like responses.",
    "what is data science": "Data Science combines statistics, programming and domain knowledge to extract useful insights from data.",
    "can ai replace humans": "AI can automate certain tasks, but human creativity, judgment, empathy and decision-making remain important.",
    "is ai always accurate": "No. AI can sometimes generate incorrect or misleading information, so important answers should be verified.",

    # Programming
    "what is programming": "Programming is the process of writing instructions for a computer.",
    "how to learn coding": "Start with one programming language, learn its fundamentals, practise small problems and gradually build projects.",
    "what is python": "Python is a high-level, interpreted programming language known for its simple syntax.",
    "what is java": "Java is an object-oriented programming language used to develop various applications.",
    "what is c": "C is a general-purpose programming language widely used in system programming.",
    "what is c++": "C++ is a general-purpose programming language that supports procedural and object-oriented programming.",
    "what is html": "HTML stands for HyperText Markup Language. It is used to structure web pages.",
    "what is css": "CSS stands for Cascading Style Sheets. It is used to style web pages.",
    "what is javascript": "JavaScript is a programming language used to make web pages interactive.",
    "what is a variable": "A variable is a named storage location used to hold data.",
    "what is a loop": "A loop is a programming structure used to repeat a set of instructions.",
    "what is a function": "A function is a reusable block of code that performs a particular task.",
    "what is an algorithm": "An algorithm is a step-by-step procedure for solving a problem.",
    "what is debugging": "Debugging is the process of finding and fixing errors in a program.",
    "what is dsa": "DSA stands for Data Structures and Algorithms. It helps programmers organize data and solve problems efficiently.",
    "what is syntax error": "A syntax error occurs when code violates the grammatical rules of a programming language.",
    "what is a runtime error": "A runtime error occurs while a program is executing.",
    "what is a logical error": "A logical error occurs when a program runs but produces an incorrect result.",
    "what is an array": "An array is a data structure that stores multiple elements in an indexed collection.",
    "what is a string": "A string is a sequence of characters used to represent text.",
    "what is a list in python": "A list in Python is an ordered, mutable collection of elements.",
    "what is a dictionary in python": "A dictionary in Python stores data in key-value pairs.",
    "what is object oriented programming": "Object-oriented programming is a programming approach based on objects and classes.",
    "what is inheritance": "Inheritance is an OOP concept in which one class can acquire properties and methods from another class.",
    "what is polymorphism": "Polymorphism allows the same interface or method name to have different implementations.",
    "what is a compiler": "A compiler translates source code into machine code or another target form before execution.",
    "what is an interpreter": "An interpreter executes source code by processing instructions at runtime.",
    "what is github used for": "GitHub is used to host code, manage projects, track changes and collaborate with developers.",
    "what is git": "Git is a version control system used to track changes in files and code.",
    "what is an api": "API stands for Application Programming Interface. It allows different software applications to communicate.",
    "what is cybersecurity": "Cybersecurity is the practice of protecting computers, networks and data from digital attacks.",

    # Computer Science
    "what is a computer": "A computer is an electronic device that processes data and performs calculations.",
    "what is hardware": "Hardware refers to the physical components of a computer.",
    "what is software": "Software is a collection of programs and instructions that tell a computer what to do.",
    "what is an operating system": "An operating system manages computer hardware and software resources.",
    "what is ram": "RAM stands for Random Access Memory. It temporarily stores data used by running programs.",
    "what is rom": "ROM stands for Read Only Memory. It stores data that is generally retained even when power is off.",
    "what is cpu": "CPU stands for Central Processing Unit. It executes instructions and processes data.",
    "what is gpu": "GPU stands for Graphics Processing Unit. It handles graphics and parallel computations.",
    "what is a database": "A database is an organized collection of information.",
    "what is sql": "SQL stands for Structured Query Language. It is used to manage and retrieve data from databases.",
    "what is a computer network": "A computer network is a group of connected devices that share information and resources.",
    "what is the internet": "The internet is a global network of interconnected computer networks.",
    "what is cloud computing": "Cloud computing provides computing services such as storage and processing over the internet.",
    "what is an ip address": "An IP address is a numerical address used to identify a device on a network.",

    # Projects and Development
    "how to build a project": "Choose a problem, plan the features, select suitable technologies, develop the application and test it.",
    "what is a frontend": "Frontend development focuses on the user-facing part of an application.",
    "what is a backend": "Backend development handles server-side logic, databases and application functionality.",
    "what is full stack development": "Full stack development involves working on both frontend and backend parts of an application.",
    "what is streamlit": "Streamlit is a Python framework used to create interactive web applications.",
    "what is streamlit used for": "Streamlit is used to quickly build interactive Python web applications, especially for data and AI projects.",
    "what is deployment": "Deployment is the process of making an application available for users to access.",
    "what is an api key": "An API key is a credential used to identify and authorize an application when accessing an API.",
    "what is testing in software": "Software testing is the process of checking whether an application works correctly and meets its requirements.",
    "what is a chatbot": "A chatbot is a software application that communicates with users through text or voice.",
    "what is an faq chatbot": "An FAQ chatbot answers frequently asked questions using a predefined collection of questions and answers.",
    "what is a website": "A website is a collection of related web pages available on the internet.",
    "what is a browser": "A browser is software used to access and view websites.",
    "what is an app": "An app is a software application designed to perform specific tasks.",
    
    # Study and College
    "how to prepare for exams": "Create a study timetable, understand important concepts, practise previous question papers and revise regularly.",
    "how to improve concentration": "Study in a quiet environment, avoid distractions, take short breaks and use focused study sessions.",
    "how to make notes": "Write important concepts in short points, use headings and include examples, diagrams and keywords.",
    "how to overcome procrastination": "Break large tasks into smaller steps, set deadlines and start with the easiest task.",
    "how to improve memory": "Use active recall, spaced repetition, practice tests and sufficient sleep.",
    "how to manage time": "Prioritize important tasks, create a daily schedule and avoid unnecessary distractions.",
    "how to study effectively": "Understand concepts instead of memorizing everything, practise regularly and revise what you learn.",
    "what is active recall": "Active recall is a learning technique in which you test yourself by remembering information without looking at your notes.",
    "what is time management": "Time management is the process of planning and organizing time to complete tasks efficiently.",

    # Career and Jobs
    "how to create a resume": "Include your contact details, education, technical skills, projects, certifications and relevant achievements.",
    "what is a resume": "A resume is a document that summarizes your education, skills, experience and achievements.",
    "what is an internship": "An internship is a temporary work experience that helps students gain practical skills and industry exposure.",
    "how to get an internship": "Build relevant skills, create projects, prepare a resume, maintain a professional profile and apply to suitable opportunities.",
    "what is linkedin": "LinkedIn is a professional networking platform used for career development, job searching and connecting with professionals.",
    "what are technical skills": "Technical skills are abilities related to specific tools, technologies, programming languages or professional tasks.",
    "what is a portfolio": "A portfolio is a collection of projects and work samples that demonstrates your skills and abilities.",
    "how to prepare for an interview": "Research the organization, revise relevant concepts, practise common questions and prepare to explain your projects.",
    "what is a placement": "A placement is an opportunity for students to secure employment through campus or off-campus recruitment.",

    # Science
    "what is gravity": "Gravity is the force of attraction between objects that have mass.",
    "what is photosynthesis": "Photosynthesis is the process by which plants use sunlight, water and carbon dioxide to produce food and release oxygen.",
    "what is electricity": "Electricity is a form of energy associated with the movement or presence of electric charges.",
    "what is solar energy": "Solar energy is energy obtained from sunlight.",
    "what is water": "Water is a chemical compound made of two hydrogen atoms and one oxygen atom, represented as H2O.",
    "what is the speed of light": "The speed of light in a vacuum is approximately 300,000 kilometres per second.",
    "what is the human brain": "The human brain is the control centre of the nervous system and manages thinking, memory, movement and emotions.",
    "what is renewable energy": "Renewable energy comes from naturally replenished sources such as sunlight, wind and water.",
    "why is the sky blue": "The sky appears blue because air molecules scatter shorter blue wavelengths of sunlight more strongly than longer wavelengths.",
    "why do stars twinkle": "Stars appear to twinkle because Earth's atmosphere bends their light in changing ways.",
    "why is seawater salty": "Seawater contains dissolved salts and minerals carried into oceans by rivers and released through underwater geological processes.",
    "how are rainbows formed": "Rainbows form when sunlight is refracted, reflected and dispersed inside water droplets.",
    "why do we dream": "Dreaming is associated with brain activity during sleep and may be involved in memory, emotions and information processing.",
    "how do airplanes fly": "Airplane wings generate lift as air flows around them, while engines provide thrust to move the aircraft forward.",
    "what is a black hole": "A black hole is a region of space where gravity is so strong that nothing, not even light, can escape from within its event horizon.",
    "what is dna": "DNA is the molecule that carries genetic information in living organisms.",
    "which is the largest organ in the human body": "The skin is the largest organ of the human body.",
    "how many bones are in an adult human body": "An adult human body typically has 206 bones.",
    "which animal is the fastest": "The peregrine falcon is the fastest animal when diving, reaching speeds over 300 kilometres per hour.",
    "which animal is the largest": "The blue whale is the largest animal known to have ever lived.",
    "can sound travel in space": "No. Sound needs a medium such as air, water or solids, and space is mostly a vacuum.",
    "why do we see lightning before thunder": "Light travels much faster than sound, so lightning reaches our eyes before thunder reaches our ears.",

    # Geography and General Knowledge
    "what is the capital of india": "New Delhi is the capital of India.",
    "what is the capital of usa": "Washington, D.C. is the capital of the United States.",
    "what is the capital of japan": "Tokyo is the capital of Japan.",
    "what is the capital of france": "Paris is the capital of France.",
    "what is the capital of china": "Beijing is the capital of China.",
    "what is the capital of australia": "Canberra is the capital of Australia.",
    "what is the capital of canada": "Ottawa is the capital of Canada.",
    "what is the capital of russia": "Moscow is the capital of Russia.",
    "which is the largest continent": "Asia is the largest continent by area.",
    "which is the smallest continent": "Australia is the smallest continent.",
    "which is the largest ocean": "The Pacific Ocean is the largest ocean.",
    "which is the highest mountain": "Mount Everest is the highest mountain above sea level.",
    "which is the longest river": "The Nile is traditionally considered the longest river in the world, although some measurements favour the Amazon.",
    "which is the largest country": "Russia is the largest country in the world by land area.",
    "which is the smallest country": "Vatican City is the smallest country in the world.",
    "how many continents are there": "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe and Australia.",
    "how many oceans are there": "There are five oceans: Pacific, Atlantic, Indian, Southern and Arctic.",
    "which planet is closest to the sun": "Mercury is the closest planet to the Sun.",
    "which planet is known as the red planet": "Mars is known as the Red Planet.",
    "which planet has rings": "Saturn is famous for its prominent ring system, although other giant planets also have rings.",
    "which is the hottest planet": "Venus is the hottest planet in our solar system.",
    "which is the largest planet": "Jupiter is the largest planet in our solar system.",
    "how many planets are there": "There are eight recognized planets in our solar system.",
    "what is the national animal of india": "The Bengal tiger is the national animal of India.",
    "what is the national bird of india": "The Indian peacock is the national bird of India.",
    "what is the national flower of india": "The lotus is the national flower of India.",
    "who is known as the father of the nation in india": "Mahatma Gandhi is widely known as the Father of the Nation in India.",
    "when did india get independence": "India gained independence on 15 August 1947.",
    "who wrote the indian national anthem": "Rabindranath Tagore wrote the Indian national anthem, Jana Gana Mana.",

    # History and Inventions
    "who invented the telephone": "Alexander Graham Bell is widely credited with inventing and patenting the first practical telephone.",
    "who invented the light bulb": "Thomas Edison developed a commercially practical incandescent light bulb, building on earlier inventors' work.",
    "who invented the computer": "Charles Babbage is often called the Father of the Computer for his designs of mechanical computing machines.",
    "who invented the internet": "The internet was developed through contributions from many researchers. Vint Cerf and Bob Kahn helped develop TCP/IP.",
    "who was albert einstein": "Albert Einstein was a theoretical physicist famous for developing the theory of relativity.",
    "who was isaac newton": "Isaac Newton was a physicist and mathematician known for his laws of motion and universal gravitation.",
    "who was apj abdul kalam": "Dr. A.P.J. Abdul Kalam was an Indian aerospace scientist and the 11th President of India.",
    "who discovered gravity": "Isaac Newton formulated the law of universal gravitation, although the phenomenon of gravity was known long before him.",
    "when was the first world war": "World War I took place from 1914 to 1918.",
    "when was the second world war": "World War II took place from 1939 to 1945.",
    "who built the taj mahal": "The Mughal emperor Shah Jahan commissioned the Taj Mahal in memory of his wife Mumtaz Mahal.",

    # Creative Questions and Imagination
    "write a short story": "A little girl found a glowing key under an old tree. When she turned it, a hidden door appeared, leading to a magical world where forgotten dreams came alive.",
    "give me a motivational quote": "Great things are not achieved in one day. They are achieved through small efforts repeated every day.",
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
    "give me a creative business idea": "Create personalized digital greeting cards where customers can customize designs, messages and animations.",
    "suggest youtube channel ideas": "You can create educational videos, interesting facts, science experiments, technology explanations, storytelling or AI-generated animations.",
    "give me a story idea": "A student discovers that every book in an abandoned library contains a prediction about someone's future.",
    "write a poem about nature": "The trees stand tall, the rivers flow, The gentle winds begin to blow. The sun brings light, the skies turn blue, Nature creates a beautiful view.",
    "what if humans could fly": "Cities might have flying traffic lanes, buildings could have landing platforms and transportation would become completely different.",
    "what if dinosaurs were alive today": "Humans would need special safety measures, protected habitats and scientific research to coexist with dinosaurs.",
    "give me an invention idea": "A smart dustbin that identifies waste materials and automatically separates recyclable items.",
    "give me a unique app idea": "An AI-powered student planner that organizes assignments, tracks study progress and creates personalized revision schedules.",
    "how to think creatively": "Explore new experiences, ask unusual questions, combine different ideas and experiment without fearing mistakes.",
    "give me a random challenge": "Try explaining your favourite technology in exactly five sentences without using technical terms.",
    "tell me a fun fact": "Octopuses have three hearts and blue blood.",

    # Riddles
    "give me a riddle": "What has keys but cannot open locks? A piano.",
    "what has hands but cannot clap": "A clock has hands but cannot clap.",
    "what gets wetter as it dries": "A towel gets wetter as it dries something else.",
    "what has a head and a tail but no body": "A coin has a head and a tail but no body.",
    "what can travel around the world while staying in one corner": "A postage stamp can travel around the world while staying in one corner of an envelope.",

    # Everyday Questions
    "how to improve english": "Read regularly, learn useful vocabulary, listen to English conversations and practise speaking every day.",
    "how to speak confidently": "Prepare your thoughts, practise speaking regularly, maintain eye contact and do not worry about small mistakes.",
    "how to set goals": "Set clear, realistic and measurable goals, break them into smaller tasks and track your progress.",
    "how to stay motivated": "Focus on your goals, celebrate small achievements and maintain consistent daily habits.",
    "how to reduce stress": "Take breaks, exercise, sleep well, organize your tasks and talk to someone you trust.",
    "what is productivity": "Productivity is the ability to complete useful tasks efficiently using available time and resources.",
    "how to make money online": "People earn online through freelancing, remote jobs, digital products, content creation and other legitimate services.",
    "what is freelancing": "Freelancing is working independently for different clients rather than being employed by one organization.",
    "what is digital marketing": "Digital marketing is the promotion of products or services through online platforms and digital channels.",
    "what is content creation": "Content creation is the process of producing videos, articles, images or other material for an audience.",
    "what is a portfolio": "A portfolio is a collection of projects and work samples that demonstrates your skills and abilities.",

    # General ChatGPT Questions
    "can chatgpt write code": "Yes. ChatGPT can generate, explain, debug and improve code in various programming languages.",
    "how does chatgpt work": "ChatGPT uses a large language model trained on large amounts of data to generate responses based on the conversation.",
    "is chatgpt free": "ChatGPT offers a free plan as well as paid plans with additional features and usage limits."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Type your question here...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    normalized_question = question.lower().strip()
    answer = "Sorry, I don't know that answer yet. Please try asking a different question."

    for keyword, response in faqs.items():
        if keyword in normalized_question:
            answer = response
            break

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
