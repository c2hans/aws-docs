---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Dimensions.html
---

# Dimensions
<a name="API_Dimensions"></a>

Contains information about the dimensions for a set of metrics.

## Contents
<a name="API_Dimensions_Contents"></a>

 ** AgentStatus **   <a name="connect-Type-Dimensions-AgentStatus"></a>
Information about the agent status assigned to the user.
Type: [AgentStatusIdentifier](API_AgentStatusIdentifier.md) object
Required: No

 ** Channel **   <a name="connect-Type-Dimensions-Channel"></a>
The channel used for grouping and filters.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** Queue **   <a name="connect-Type-Dimensions-Queue"></a>
Information about the queue for which metrics are returned.
Type: [QueueReference](API_QueueReference.md) object
Required: No

 ** RoutingProfile **   <a name="connect-Type-Dimensions-RoutingProfile"></a>
Information about the routing profile assigned to the user.
Type: [RoutingProfileReference](API_RoutingProfileReference.md) object
Required: No

 ** RoutingStepExpression **   <a name="connect-Type-Dimensions-RoutingStepExpression"></a>
The expression of a step in a routing criteria.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** Subtype **   <a name="connect-Type-Dimensions-Subtype"></a>
The subtype of the channel used for the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ValidationTestType **   <a name="connect-Type-Dimensions-ValidationTestType"></a>
The testing and simulation type
Type: String
Required: No

## See Also
<a name="API_Dimensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Dimensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Dimensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Dimensions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
