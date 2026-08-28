---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListEventsFilters.html
---

# ListEventsFilters
<a name="API_ListEventsFilters"></a>

 Filters you can use to specify which events are returned when `ListEvents` is called.

## Contents
<a name="API_ListEventsFilters_Contents"></a>

 ** DataSource **   <a name="DevOpsGuru-Type-ListEventsFilters-DataSource"></a>
 The source, `AWS_CLOUD_TRAIL` or `AWS_CODE_DEPLOY`, of the events you want returned.
Type: String
Valid Values: `AWS_CLOUD_TRAIL | AWS_CODE_DEPLOY`
Required: No

 ** EventClass **   <a name="DevOpsGuru-Type-ListEventsFilters-EventClass"></a>
 The class of the events you want to filter for, such as an infrastructure change, a deployment, or a schema change.
Type: String
Valid Values: `INFRASTRUCTURE | DEPLOYMENT | SECURITY_CHANGE | CONFIG_CHANGE | SCHEMA_CHANGE`
Required: No

 ** EventSource **   <a name="DevOpsGuru-Type-ListEventsFilters-EventSource"></a>
 The AWS source that emitted the events you want to filter for.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 50.
Pattern: `^[a-z]+[a-z0-9]*\.amazonaws\.com|aws\.events$`
Required: No

 ** EventTimeRange **   <a name="DevOpsGuru-Type-ListEventsFilters-EventTimeRange"></a>
 A time range during which you want the filtered events to have occurred.
Type: [EventTimeRange](API_EventTimeRange.md) object
Required: No

 ** InsightId **   <a name="DevOpsGuru-Type-ListEventsFilters-InsightId"></a>
 An ID of an insight that is related to the events you want to filter for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-ListEventsFilters-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

## See Also
<a name="API_ListEventsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListEventsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListEventsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListEventsFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
