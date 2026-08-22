import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError(
        "GOOGLE_API_KEY is not set. "
        "Add it to your environment variables or .env file."
    )


llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=google_api_key,
    temperature=0.2
)


# =========================================================
# AGENTS
# =========================================================

skeptic_agent = Agent(
    role="Critical Thinker and Logic Analyst",

    goal=(
        "Identify logical fallacies, unverified claims, "
        "and hype within the provided text."
    ),

    backstory=(
        "You are a detective of truth and critical thinking. "
        "You have experience analyzing scientific claims, "
        "technology hype, and news narratives. "
        "You prioritize evidence, logical consistency, "
        "and careful reasoning."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


supporter_agent = Agent(
    role="Fair Supporter and Context Finder",

    goal=(
        "Identify positive aspects, hidden merits, "
        "and reasonable arguments behind the claim."
    ),

    backstory=(
        "You look for the strongest reasonable interpretation "
        "of an argument. Your role is to identify genuine potential, "
        "supporting context, and plausible aspects of a claim."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


synthesizer_agent = Agent(
    role="Objective Arbiter and Evaluator",

    goal=(
        "Synthesize conflicting perspectives into a balanced, "
        "realistic, and unbiased final evaluation."
    ),

    backstory=(
        "You act as an impartial evaluator. "
        "You compare evidence and reasoning from different perspectives "
        "to distinguish realistic potential from unsupported hype."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =========================================================
# TASKS
# =========================================================

task_skepticism = Task(
    description="""
    Carefully analyze the provided claim.

    Identify:
    - Logical gaps
    - Unsupported assumptions
    - Exaggerated statements
    - Marketing hype
    - Claims requiring stronger evidence

    Input Claim:
    {claim}
    """,

    expected_output="""
    A structured bullet-point list of logical weaknesses,
    unsupported claims, and potential exaggerations.

    Each point should clearly explain the issue identified.
    """,

    agent=skeptic_agent
)


task_support = Task(
    description="""
    Analyze the same claim from a constructive perspective.

    Identify:
    - Valid or plausible aspects
    - Potential benefits
    - Supporting context
    - Reasons why the claim may be worth exploring

    Input Claim:
    {claim}
    """,

    expected_output="""
    A concise report describing the reasonable,
    plausible, and potentially valuable aspects of the claim.
    """,

    agent=supporter_agent
)


task_synthesis = Task(
    description="""
    Review the analyses produced by the Skeptic Agent
    and the Supporter Agent.

    Compare their perspectives and produce a balanced evaluation.

    Determine which parts of the original claim are:

    - Well-supported
    - Plausible but uncertain
    - Exaggerated or unsupported
    """,

    expected_output="""
    A structured Markdown report containing:

    ## Executive Summary

    ## Strengths and Plausible Arguments

    ## Weaknesses and Unsupported Claims

    ## Final Verdict

    The final verdict should clearly distinguish
    realistic potential from exaggeration or hype.
    """,

    agent=synthesizer_agent
)


# =========================================================
# CREW
# =========================================================

crew = Crew(
    agents=[
        skeptic_agent,
        supporter_agent,
        synthesizer_agent
    ],

    tasks=[
        task_skepticism,
        task_support,
        task_synthesis
    ],

    verbose=True
)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    input_claim = {
        "claim": """
        Using AI in schools will completely eliminate
        the need for human teachers by 2030,
        increasing student learning efficiency by 300%.
        """
    }

    print(
        "\n########## Starting Multi-Agent Process ##########\n"
    )

    result = crew.kickoff(
        inputs=input_claim
    )

    print(
        "\n########## Final Result ##########\n"
    )

    print(result)
