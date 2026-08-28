---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RuntimeConfiguration.html
---

# RuntimeConfiguration
<a name="API_RuntimeConfiguration"></a>

A set of instructions that define the set of server processes to run on computes in a fleet. Server processes run either an executable in a custom game build or a Amazon GameLift Servers Realtime script. Amazon GameLift Servers launches the processes, manages their life cycle, and replaces them as needed. Computes check regularly for an updated runtime configuration.

An Amazon GameLift Servers instance is limited to 50 processes running concurrently. To calculate the total number of processes defined in a runtime configuration, add the values of the `ConcurrentExecutions` parameter for each server process. Learn more about [ Running Multiple Processes on a Fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html).

## Contents
<a name="API_RuntimeConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GameSessionActivationTimeoutSeconds **   <a name="gameliftservers-Type-RuntimeConfiguration-GameSessionActivationTimeoutSeconds"></a>
The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status `ACTIVATING`. If the game session does not become active before the timeout, it is ended and the game session status is changed to `TERMINATED`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** MaxConcurrentGameSessionActivations **   <a name="gameliftservers-Type-RuntimeConfiguration-MaxConcurrentGameSessionActivations"></a>
The number of game sessions in status `ACTIVATING` to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** ServerProcesses **   <a name="gameliftservers-Type-RuntimeConfiguration-ServerProcesses"></a>
A collection of server process configurations that identify what server processes to run on fleet computes.
Type: Array of [ServerProcess](API_ServerProcess.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_RuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/RuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/RuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/RuntimeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
