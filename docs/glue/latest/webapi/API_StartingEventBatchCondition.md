---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartingEventBatchCondition.html
---

# StartingEventBatchCondition
<a name="API_StartingEventBatchCondition"></a>

The batch condition that started the workflow run. Either the number of events in the batch size arrived, in which case the BatchSize member is non-zero, or the batch window expired, in which case the BatchWindow member is non-zero.

## Contents
<a name="API_StartingEventBatchCondition_Contents"></a>

 ** BatchSize **   <a name="Glue-Type-StartingEventBatchCondition-BatchSize"></a>
Number of events in the batch.
Type: Integer
Required: No

 ** BatchWindow **   <a name="Glue-Type-StartingEventBatchCondition-BatchWindow"></a>
Duration of the batch window in seconds.
Type: Integer
Required: No

## See Also
<a name="API_StartingEventBatchCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartingEventBatchCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartingEventBatchCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartingEventBatchCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
