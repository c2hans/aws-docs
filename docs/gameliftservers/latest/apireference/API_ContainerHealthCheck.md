---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerHealthCheck.html
---

# ContainerHealthCheck
<a name="API_ContainerHealthCheck"></a>

Instructions on when and how to check the health of a support container in a container fleet. These properties override any Docker health checks that are set in the container image. For more information on container health checks, see [HealthCheck command](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HealthCheck.html#ECS-Type-HealthCheck-command) in the *Amazon Elastic Container Service API*. Game server containers don't have a health check parameter; Amazon GameLift Servers automatically handles health checks for these containers.

The following example instructs the container to initiate a health check command every 60 seconds and wait 10 seconds for it to succeed. If it fails, retry the command 3 times before flagging the container as unhealthy. It also tells the container to wait 100 seconds after launch before counting failed health checks.

 `{"Command": [ "CMD-SHELL", "ps cax | grep "processmanager" || exit 1" ], "Interval": 60, "Timeout": 10, "Retries": 3, "StartPeriod": 100 }`

 **Part of:** [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Contents
<a name="API_ContainerHealthCheck_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Command **   <a name="gameliftservers-Type-ContainerHealthCheck-Command"></a>
A string array that specifies the command that the container runs to determine if it's healthy.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Interval **   <a name="gameliftservers-Type-ContainerHealthCheck-Interval"></a>
The time period (in seconds) between each health check.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 300.
Required: No

 ** Retries **   <a name="gameliftservers-Type-ContainerHealthCheck-Retries"></a>
The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 10.
Required: No

 ** StartPeriod **   <a name="gameliftservers-Type-ContainerHealthCheck-StartPeriod"></a>
The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** Timeout **   <a name="gameliftservers-Type-ContainerHealthCheck-Timeout"></a>
The time period (in seconds) to wait for a health check to succeed before counting a failed health check.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 60.
Required: No

## See Also
<a name="API_ContainerHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerHealthCheck)
