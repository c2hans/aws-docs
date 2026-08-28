---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel03.html
---

# Failure management
<a name="gamerel03"></a>

|  GAMEREL03: How do you persist game state during infrastructure disruptions?  |
| --- |
|   |

 As your game infrastructure experiences various operational events over time, your game's architecture should be designed to maintain continuity for player experiences and preserve game state during infrastructure events. To handle these events, implement monitoring, graceful shutdowns, and state persistence mechanisms to verify smooth gameplay experiences for your players.

**Topics**
+ [GAMEREL03-BP01 Monitor game server disruptions, and use the data to improve hosting architecture to achieve reliability goals](gamerel03-bp01.md)
+ [GAMEREL03-BP02 Implement loose coupling of game features to handle failures with minimal impact to player experience](gamerel03-bp02.md)
+ [GAMEREL03-BP03 Monitor infrastructure events over time to measure impact on player behavior](gamerel03-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
