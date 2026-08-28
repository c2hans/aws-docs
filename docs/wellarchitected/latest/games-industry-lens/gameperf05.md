---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf05.html
---

# Compute selection
<a name="gameperf05"></a>

|  GAMEPERF05: How do you select the appropriate compute solution for your game?  |
| --- |
|   |

 Compute performance varies across instance sizes and families. It is beneficial to use multiple compute options that are from separate capacity pools. Develop a fleet composition strategy that gives preference to performance but includes enough diversity to avoid insufficient capacity errors.

**Topics**
+ [GAMEPERF05-BP01 Benchmark your game performance across multiple compute types](gameperf05-bp01.md)
+ [GAMEPERF05-BP02 Move non-latency-sensitive compute tasks to asynchronous workflows](gameperf05-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
