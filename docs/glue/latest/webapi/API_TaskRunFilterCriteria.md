---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TaskRunFilterCriteria.html
---

# TaskRunFilterCriteria
<a name="API_TaskRunFilterCriteria"></a>

The criteria that are used to filter the task runs for the machine learning transform.

## Contents
<a name="API_TaskRunFilterCriteria_Contents"></a>

 ** StartedAfter **   <a name="Glue-Type-TaskRunFilterCriteria-StartedAfter"></a>
Filter on task runs started after this date.
Type: Timestamp
Required: No

 ** StartedBefore **   <a name="Glue-Type-TaskRunFilterCriteria-StartedBefore"></a>
Filter on task runs started before this date.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-TaskRunFilterCriteria-Status"></a>
The current status of the task run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

 ** TaskRunType **   <a name="Glue-Type-TaskRunFilterCriteria-TaskRunType"></a>
The type of task run.
Type: String
Valid Values: `EVALUATION | LABELING_SET_GENERATION | IMPORT_LABELS | EXPORT_LABELS | FIND_MATCHES`
Required: No

## See Also
<a name="API_TaskRunFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TaskRunFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TaskRunFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TaskRunFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
