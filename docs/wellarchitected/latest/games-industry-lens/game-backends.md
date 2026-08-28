---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/game-backends.html
---

# Game backends
<a name="game-backends"></a>

 Game backends are used to manage game and player state, as well as integrate social and system-level features into the game that support the gaming experience. Player profile management, item and inventory storage, and stats and leaderboards are examples of services hosted in game backends.

 Game backends are typically built as REST APIs that are accessed by clients using HTTPS. However, other approaches are also common, such as WebSockets that provide bidirectional channels for use cases such as client notifications for in-game chat and presence. Game backends can be deployed using a variety of different deployment architectures, including using instances, containers, or a serverless architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
