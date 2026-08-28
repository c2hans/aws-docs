---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerContainerGroupCounts.html
---

# GameServerContainerGroupCounts
<a name="API_GameServerContainerGroupCounts"></a>

The number and status of game server container groups that are deployed across a container fleet. Combine this count with the number of server processes that each game server container group runs to learn how many game sessions the fleet is capable of hosting concurrently. For example, if a fleet has 50 game server container groups, and the game server container in each group runs 1 game server process, then the fleet has the capacity to run host 50 game sessions at a time.

 **Returned by:** [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html), [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html)

## Contents
<a name="API_GameServerContainerGroupCounts_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ACTIVE **   <a name="gameliftservers-Type-GameServerContainerGroupCounts-ACTIVE"></a>
 The number of container groups that have active game sessions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** IDLE **   <a name="gameliftservers-Type-GameServerContainerGroupCounts-IDLE"></a>
 The number of container groups that have no active game sessions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PENDING **   <a name="gameliftservers-Type-GameServerContainerGroupCounts-PENDING"></a>
 The number of container groups that are starting up but haven't yet registered.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TERMINATING **   <a name="gameliftservers-Type-GameServerContainerGroupCounts-TERMINATING"></a>
 The number of container groups that are in the process of shutting down.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_GameServerContainerGroupCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerContainerGroupCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerContainerGroupCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerContainerGroupCounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
