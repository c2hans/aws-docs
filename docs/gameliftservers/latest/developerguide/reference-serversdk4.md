---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/reference-serversdk4.html
---

# Server SDK for Amazon GameLift Servers version 4 and earlier
<a name="reference-serversdk4"></a>

This reference documents the server SDK for Amazon GameLift Servers, version 4.x and earlier. The server SDK provides core functionality that your game servers use to communicate with the Amazon GameLift Servers service. For example, your game server receives prompts from the service to start and stop game sessions and it provides regular game session status updates to the service. Integrate your game servers with the server SDK before you deploy them for hosting.

Use this server SDK reference to integrate your custom multiplayer game servers for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md).

For SDK version 4.0.2, you can download it from the [official GitHub releases](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/releases). The complete SDK package including GameLiftLocal.jar is available in the GameLift-CSharp-ServerSDK-4.0.2.zip artifact.

The latest major version of the server SDK for Amazon GameLift Servers is 5.x. The following hosting features require updates to version 5.x:
+ Amazon GameLift Servers Anywhere
+ Amazon GameLift Servers managed containers
+ Amazon GameLift Servers plugin for Unreal Engine and Unity

**Topics**
+ [C\+\+ server SDK for Amazon GameLift Servers 4.x -- Actions](integration-server-sdk-cpp-ref-actions.md)
+ [C\# server SDK for Amazon GameLift Servers 4.x -- Actions](integration-server-sdk-csharp-ref-actions.md)
+ [Server SDK (Unreal) for Amazon GameLift Servers -- Actions](integration-server-sdk-unreal-ref-actions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
