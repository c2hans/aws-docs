---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift_quickstart_customservers_designbackend.html
---

# Build a backend service for Amazon GameLift Servers
<a name="gamelift_quickstart_customservers_designbackend"></a>

We recommend that you implement a game client service that authenticates your players and communicates with the Amazon GameLift Servers API. By implementing a custom game client service, you can:
+ Customize authentication for your players.
+ Control how Amazon GameLift Servers groups players for new game sessions or to add to existing game sessions.
+ Collect information from your own resources to provide game sesplayer attributes such as skill rating for matchmaking instead of trusting the client.

Using a game client service also reduces security risks introduced by game clients interacting directly with your Amazon GameLift Servers API.

## Authenticating your players
<a name="gamelift_quickstart_customservers_designbackend_auth"></a>

You can use Amazon Cognito and player session IDs to authenticate your game clients. To manage the lifecycle and properties of your player identities, use Amazon Cognito user pools.

If you prefer, build a custom identity solution and host it on AWS. You can also use Lambda authorizers for custom authorization logic with API Gateway.

**Additional resources:**
+ [Using identity pools (federated identities)](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) (Amazon Cognito Developer Guide)
+ [Getting started with user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools.html) (Amazon Cognito Developer Guide)
+ [How to Set Up Player Authentication with Amazon Cognito](https://aws.amazon.com/blogs/gametech/how-to-set-up-player-authentication-with-amazon-cognito/) (AWS for Games Blog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
