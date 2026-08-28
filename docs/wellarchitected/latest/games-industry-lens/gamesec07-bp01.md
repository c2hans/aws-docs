---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec07-bp01.html
---

# GAMESEC07-BP01 Implement an incident response plan to handle bad actors and abusive behavior
<a name="gamesec07-bp01"></a>

 Create a plan of action for responding to bad actors and abusive behavior in your game.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-33"></a>

 Consider factors such as when to temporarily suspend or permanently ban players and how long to disable credentials for temporarily suspended players.

 **Customer example**

 AnyCompany Games creates a tiered incident response system in which minor infractions like inappropriate chat messages result in automatic 24-hour account suspensions, while more severe violations such as cheating or harassment trigger immediate 7-day suspensions with mandatory review by human moderators.

 Additionally, AnyCompany Games establishes escalation procedures in which repeat offenders face progressively longer suspensions. They create appeal processes that allow falsely flagged players to contest automated actions while maintaining security through identity verification requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
