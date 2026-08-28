---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterEventSummary.html
---

# ClusterEventSummary
<a name="API_ClusterEventSummary"></a>

A summary of an event in a HyperPod cluster.

## Contents
<a name="API_ClusterEventSummary_Contents"></a>

 ** ClusterArn **   <a name="sagemaker-Type-ClusterEventSummary-ClusterArn"></a>
The Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** ClusterName **   <a name="sagemaker-Type-ClusterEventSummary-ClusterName"></a>
The name of the HyperPod cluster associated with the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** EventId **   <a name="sagemaker-Type-ClusterEventSummary-EventId"></a>
The unique identifier (UUID) of the event.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** EventTime **   <a name="sagemaker-Type-ClusterEventSummary-EventTime"></a>
The timestamp when the event occurred.
Type: Timestamp
Required: Yes

 ** ResourceType **   <a name="sagemaker-Type-ClusterEventSummary-ResourceType"></a>
The type of resource associated with the event. Valid values are `Cluster`, `InstanceGroup`, or `Instance`.
Type: String
Valid Values: `Cluster | InstanceGroup | Instance`
Required: Yes

 ** Description **   <a name="sagemaker-Type-ClusterEventSummary-Description"></a>
A brief, human-readable description of the event.
Type: String
Required: No

 ** EventLevel **   <a name="sagemaker-Type-ClusterEventSummary-EventLevel"></a>
The severity level of the event. Valid values are `Info`, `Warn`, and `Error`.
Type: String
Valid Values: `Info | Warn | Error`
Required: No

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterEventSummary-InstanceGroupName"></a>
The name of the instance group associated with the event, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** InstanceId **   <a name="sagemaker-Type-ClusterEventSummary-InstanceId"></a>
The Amazon Elastic Compute Cloud (EC2) instance ID associated with the event, if applicable.
Type: String
Required: No

## See Also
<a name="API_ClusterEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
