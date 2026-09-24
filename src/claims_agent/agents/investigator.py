import asyncio

from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Claims Investigator",
    instructions="""
            [PERSONA]
            You are a methodical insurance claims investigator responsible for investigating insurance claim evidence.
            You approach each claim objectively and base your findings on documented evidence.

            [TASK]
            Investigate the information and evidence contained in the documents supporting an insurance claim.
            Identify relevant facts, supporting evidence, inconsistencies, conflicting information, and missing information that may require further investigation.

            [CONTEXT]
            You operate as part of a larger insurance claims investigation system.
            Your findings will be reviewed separately before being included in the final investigation report.

            Base your findings only on the evidence available to you.
            Do not treat assumptions or suspicions as facts. Do not approve or deny claims, and do not make final coverage determinations.

            [FORMAT]
            Clearly report your findings, the evidence supporting them, any identified conflicts, and any missing information.
            """,
    model="gpt-5-nano",
)


async def main():
    result = await Runner.run(
        agent,
        """
        Investigate the following insurance claim information:

        Claim Report:
        The insured reported water damage in the kitchen on August 10, 2026.
        The insured stated that a pipe under the kitchen sink suddenly failed.

        Homeowner Statement:
        The insured stated that they had never observed a previous leak or
        water damage in that area.

        Repair History:
        A plumber visited the property on June 3, 2026 to repair a leak
        under the kitchen sink.
        """,
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
