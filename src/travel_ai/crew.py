from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")


@CrewBase
class TravelAi():
    """TravelAi crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def tourism_guide(self) -> Agent:
        return Agent(
            config=self.agents_config['tourism_guide'],
            verbose=True
        )

    @task
    def tourism_task(self) -> Task:
        return Task(
            config=self.tasks_config['tourism_task'],
        )

    @agent
    def activities_guide(self) -> Agent:
        return Agent(
            config=self.agents_config['activities_guide'],
            verbose=True
        )

    @task
    def activities_task(self) -> Task:
        return Task(
            config=self.tasks_config['activities_task'],
            context=[],
        )

    @agent
    def food_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['food_recommender'],
            verbose=True,
        )

    @task
    def food_recommender_task(self) -> Task:
        return Task(
            config=self.tasks_config['food_recommender_task'],
            context=[],
        )

    @agent
    def travel_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_planner'],
            verbose=True,
        )

    @task
    def travel_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['travel_planner_task'],
            context=[self.tourism_task(),self.activities_task(),self.food_recommender_task()],
            output_file="report.md"
        )
    @crew
    def crew(self) -> Crew:
        """Creates the TravelAi crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
