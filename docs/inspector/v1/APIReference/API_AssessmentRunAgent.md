---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunAgent.html
---

# AssessmentRunAgent
<a name="API_AssessmentRunAgent"></a>

Contains information about an Amazon Inspector Classic agent. This data type is used as a response element in the [ListAssessmentRunAgents](API_ListAssessmentRunAgents.md) action.

## Contents
<a name="API_AssessmentRunAgent_Contents"></a>

 ** agentHealth **   <a name="Inspector-Type-AssessmentRunAgent-agentHealth"></a>
The current health state of the agent.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: Yes

 ** agentHealthCode **   <a name="Inspector-Type-AssessmentRunAgent-agentHealthCode"></a>
The detailed health state of the agent.
Type: String
Valid Values: `IDLE | RUNNING | SHUTDOWN | UNHEALTHY | THROTTLED | UNKNOWN`
Required: Yes

 ** agentId **   <a name="Inspector-Type-AssessmentRunAgent-agentId"></a>
The AWS account of the EC2 instance where the agent is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** assessmentRunArn **   <a name="Inspector-Type-AssessmentRunAgent-assessmentRunArn"></a>
The ARN of the assessment run that is associated with the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** telemetryMetadata **   <a name="Inspector-Type-AssessmentRunAgent-telemetryMetadata"></a>
The Amazon Inspector Classic application data metrics that are collected by the agent.
Type: Array of [TelemetryMetadata](API_TelemetryMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5000 items.
Required: Yes

 ** agentHealthDetails **   <a name="Inspector-Type-AssessmentRunAgent-agentHealthDetails"></a>
The description for the agent health code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** autoScalingGroup **   <a name="Inspector-Type-AssessmentRunAgent-autoScalingGroup"></a>
The Auto Scaling group of the EC2 instance that is specified by the agent ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AssessmentRunAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentRunAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentRunAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentRunAgent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
