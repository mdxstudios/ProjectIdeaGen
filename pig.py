 import random

def useful_project_generator():
    """
    This function generates a random project idea and returns a string description of the project.
    
    Returns:
    str: A string description of a randomly generated project idea
    """
    try:
        # List of project ideas
        project_ideas = [
            "A web app that recommends recipes based on ingredients you have on hand",
            "A mobile game that helps you learn a new language",
            "A desktop app that generates random workout routines",
            "A chatbot that helps you find local events",
            "A website that connects volunteers with local charities",
            "A tool that generates random writing prompts",
            "A program that generates random art pieces",
            "A web app that helps you plan your next vacation",
            "A mobile app that helps you track your daily water intake",
            "A desktop app that generates random music playlists"
        ]
        
        # Generate a random project idea
        project_idea = random.choice(project_ideas)
        
        # Return the project idea
        return project_idea
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return 0
