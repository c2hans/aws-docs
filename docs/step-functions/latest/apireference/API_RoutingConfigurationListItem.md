---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_RoutingConfigurationListItem.html
---

# RoutingConfigurationListItem
<a name="API_RoutingConfigurationListItem"></a>

Contains details about the routing configuration of a state machine alias. In a routing configuration, you define an array of objects that specify up to two state machine versions. You also specify the percentage of traffic to be routed to each version.

## Contents
<a name="API_RoutingConfigurationListItem_Contents"></a>

 ** stateMachineVersionArn **   <a name="StepFunctions-Type-RoutingConfigurationListItem-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.
If you specify the ARN of a second version, it must belong to the same state machine as the first version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** weight **   <a name="StepFunctions-Type-RoutingConfigurationListItem-weight"></a>
The percentage of traffic you want to route to a state machine version. The sum of the weights in the routing configuration must be equal to 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

## See Also
<a name="API_RoutingConfigurationListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/RoutingConfigurationListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/RoutingConfigurationListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/RoutingConfigurationListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
