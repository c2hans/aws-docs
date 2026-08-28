---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf08-bp02.html
---

# GAMEPERF08-BP02 Align solution selection with engineering team skills and expertise
<a name="gameperf08-bp02"></a>

 Assess your team's skills and expertise in managing and optimizing game server performance when choosing your hosting option. Self-hosted solutions like EC2 and containers require more knowledge of infrastructure management, performance tuning, and scaling. If your team lacks these skills, a managed service like GameLift may be more suitable, as it abstracts away many of the complexities and allows your team to focus on game-specific optimizations.

 **Level of risk exposed if this best practice is not established: High**

## Implementation guidance
<a name="implementation-guidance-67"></a>

 By evaluating these factors and conducting performance tests across different hosting options, you can select the most appropriate solution that meets your game's specific requirements while optimizing for performance efficiency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
