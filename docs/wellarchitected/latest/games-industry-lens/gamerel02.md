---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel02.html
---

# Change management
<a name="gamerel02"></a>

|  GAMEREL02: How do you scale your stateful games to accommodate changes in demand?  |
| --- |
|   |

 As your player demand fluctuates over time, your game infrastructure should be able to adaptively scale to handle these changing requirements. While it is difficult to predict the popularity of a game ahead of time, design an architecture approach that allows for addition and removal of infrastructure capacity to accommodate fluctuations in player population.

**Topics**
+ [GAMEREL02-BP01 Implement a scaling strategy that incorporates the state of active player game sessions](gamerel02-bp01.md)
+ [GAMEREL02-BP02 Support the use of multiple EC2 instance types for your game](gamerel02-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
