---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EventBatchingCondition.html
---

# EventBatchingCondition
<a name="API_EventBatchingCondition"></a>

Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

## Contents
<a name="API_EventBatchingCondition_Contents"></a>

 ** BatchSize **   <a name="Glue-Type-EventBatchingCondition-BatchSize"></a>
Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** BatchWindow **   <a name="Glue-Type-EventBatchingCondition-BatchWindow"></a>
Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: No

## See Also
<a name="API_EventBatchingCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EventBatchingCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EventBatchingCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EventBatchingCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
