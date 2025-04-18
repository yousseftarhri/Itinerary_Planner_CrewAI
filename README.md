# 🧠 Smart Itinerary Planner with AI Agents using CrewAI

This project is a smart itinerary planner built with [CrewAI](https://github.com/joaomdmoura/crewAI), an open-source Python framework that orchestrates AI agents to collaborate on tasks.

Simply enter the **city** you're traveling to and your **hobbies**, and the AI agents will work together to generate a personalized **7-day itinerary** for your destination.

---

## 🚀 How It Works

The project is powered by multiple specialized AI agents, each responsible for a specific role:

- 🗺️ **Tourism Guide**: Suggests the top places to visit in the city.
- 🧗 **Activities Guide**: Recommends fun and engaging activities.
- 🍽️ **Food Recommender**: Lists the must-try local dishes and food spots.
- 🧳 **Travel Planner**: Combines everything into a clear and structured 7-day itinerary.

CrewAI coordinates these agents to collaborate **sequentially** and produce the final output.

---

## 🧠 Technologies Used

- 🐍 Python 3.10+
- 🤖 [CrewAI](https://github.com/joaomdmoura/crewAI)
- 🧠 OpenAI GPT (via API)

---

## 🔐 Environment Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Itinerary_Planner_CrewAI.git
   cd Itinerary_Planner_CrewAI
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Create a .env file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_key_here

# Run the App

`crewai run`\
You’ll be prompted to enter:\
🌍 The city you're traveling to\
🎯 Your hobbies or interests

The system will generate a personalized travel itinerary just for you.

# 📖 Article & Code Explanation

Curious about how everything works under the hood?\
Read the full breakdown on Medium here:\
👉 Read the full article on Medium