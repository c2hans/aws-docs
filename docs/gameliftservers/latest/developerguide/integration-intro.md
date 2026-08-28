---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-intro.html
---

# Prepare a game for hosting with Amazon GameLift Servers
<a name="integration-intro"></a>

Before you can deploy your game for hosting on Amazon GameLift Servers, you need to prepare both your game server and game client components. This involves integrating your game server with the Amazon GameLift Servers Server SDK and building a backend service that handles player authentication and game session management.

The Server SDK integration enables your game server to communicate with the Amazon GameLift Servers service, report its health status, and manage game sessions. The backend service acts as an intermediary between your game clients and the Amazon GameLift Servers service, handling player requests and coordinating game session placement.

**Topics**
+ [Prepare your Unreal or Unity game with the Amazon GameLift Servers plugin](getting-started-plugin.md)
+ [Integrate a game server with Amazon GameLift Servers](gamelift-sdk-server.md)
+ [Package a game server build for deployment](gamelift-build-intro.md)
+ [Game client/server interactions with Amazon GameLift Servers](gamelift-sdk-interactions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
