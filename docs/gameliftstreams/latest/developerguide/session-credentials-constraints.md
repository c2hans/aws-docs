---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials-constraints.html
---

# Requirements and constraints
<a name="session-credentials-constraints"></a>
+ **Same account only**: The IAM role must belong to the same AWS account as the stream group. Amazon GameLift Streams does not support cross-account role passing.
+ **Role naming**: The role name must start with `GameLiftStreams-`. Amazon GameLift Streams rejects roles without this prefix.
+ **Session-level only**: Specify the role per session on `StartStreamSession`. Different sessions in the same stream group can use different roles, or no role at all.
+ **No service-linked roles**: [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (identified by ARNs containing `/aws-service-role/`) are not supported.
+ **Stream group compatibility**: Only stream groups created after July 16, 2026 support session credentials. To use this feature with an older stream group, create a new stream group.
+ **Automatic credential refresh**: Credentials are refreshed automatically throughout the session. Your application does not need to handle credential expiration.
+ **All runtimes supported**: Session credentials work on all Amazon GameLift Streams runtime environments, including Windows, Ubuntu, and Proton.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
