---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ServerProcess.html
---

# ServerProcess
<a name="API_ServerProcess"></a>

A set of instructions for launching server processes on fleet computes. Server processes run either an executable in a custom game build or a Amazon GameLift Servers Realtime script. Server process configurations are part of a fleet's runtime configuration.

## Contents
<a name="API_ServerProcess_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConcurrentExecutions **   <a name="gameliftservers-Type-ServerProcess-ConcurrentExecutions"></a>
The number of server processes using this configuration that run concurrently on each instance or compute.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** LaunchPath **   <a name="gameliftservers-Type-ServerProcess-LaunchPath"></a>
The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root:
+ Windows (custom game builds only): `C:\game`. Example: "`C:\game\MyGame\server.exe`"
+ Linux: `/local/game`. Examples: "`/local/game/MyGame/server.exe`" or "`/local/game/MyRealtimeScript.js`"
Amazon GameLift Servers doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations `initSDK()` and `ProcessReady()`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- ]+`
Required: Yes

 ** Parameters **   <a name="gameliftservers-Type-ServerProcess-Parameters"></a>
An optional list of parameters to pass to the server executable or Realtime script on launch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_:.+\/\\\- =@{},?'\[\]"]+`
Required: No

## See Also
<a name="API_ServerProcess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ServerProcess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ServerProcess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ServerProcess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
