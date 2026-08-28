---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

 An AWS resource event. AWS resource events and metrics are analyzed by DevOps Guru to find anomalous behavior and provide recommendations to improve your operational solutions.

## Contents
<a name="API_Event_Contents"></a>

 ** DataSource **   <a name="DevOpsGuru-Type-Event-DataSource"></a>
 The source, `AWS_CLOUD_TRAIL` or `AWS_CODE_DEPLOY`, where DevOps Guru analysis found the event.
Type: String
Valid Values: `AWS_CLOUD_TRAIL | AWS_CODE_DEPLOY`
Required: No

 ** EventClass **   <a name="DevOpsGuru-Type-Event-EventClass"></a>
 The class of the event. The class specifies what the event is related to, such as an infrastructure change, a deployment, or a schema change.
Type: String
Valid Values: `INFRASTRUCTURE | DEPLOYMENT | SECURITY_CHANGE | CONFIG_CHANGE | SCHEMA_CHANGE`
Required: No

 ** EventSource **   <a name="DevOpsGuru-Type-Event-EventSource"></a>
 The AWS source that emitted the event.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 50.
Pattern: `^[a-z]+[a-z0-9]*\.amazonaws\.com|aws\.events$`
Required: No

 ** Id **   <a name="DevOpsGuru-Type-Event-Id"></a>
 The ID of the event.
Type: String
Required: No

 ** Name **   <a name="DevOpsGuru-Type-Event-Name"></a>
 The name of the event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-Event-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** Resources **   <a name="DevOpsGuru-Type-Event-Resources"></a>
 An `EventResource` object that contains information about the resource that emitted the event.
Type: Array of [EventResource](API_EventResource.md) objects
Required: No

 ** Time **   <a name="DevOpsGuru-Type-Event-Time"></a>
 A `Timestamp` that specifies the time the event occurred.
Type: Timestamp
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
