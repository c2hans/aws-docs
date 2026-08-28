---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Workflow.html
---

# Workflow
<a name="API_Workflow"></a>

A workflow is a collection of multiple dependent AWS Glue jobs and crawlers that are run to complete a complex ETL task. A workflow manages the execution and monitoring of all its jobs and crawlers.

## Contents
<a name="API_Workflow_Contents"></a>

 ** BlueprintDetails **   <a name="Glue-Type-Workflow-BlueprintDetails"></a>
This structure indicates the details of the blueprint that this particular workflow is created from.
Type: [BlueprintDetails](API_BlueprintDetails.md) object
Required: No

 ** CreatedOn **   <a name="Glue-Type-Workflow-CreatedOn"></a>
The date and time when the workflow was created.
Type: Timestamp
Required: No

 ** DefaultRunProperties **   <a name="Glue-Type-Workflow-DefaultRunProperties"></a>
A collection of properties to be used as part of each execution of the workflow. The run properties are made available to each job in the workflow. A job can modify the properties for the next jobs in the flow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Description **   <a name="Glue-Type-Workflow-Description"></a>
A description of the workflow.
Type: String
Required: No

 ** Graph **   <a name="Glue-Type-Workflow-Graph"></a>
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.
Type: [WorkflowGraph](API_WorkflowGraph.md) object
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-Workflow-LastModifiedOn"></a>
The date and time when the workflow was last modified.
Type: Timestamp
Required: No

 ** LastRun **   <a name="Glue-Type-Workflow-LastRun"></a>
The information about the last execution of the workflow.
Type: [WorkflowRun](API_WorkflowRun.md) object
Required: No

 ** MaxConcurrentRuns **   <a name="Glue-Type-Workflow-MaxConcurrentRuns"></a>
You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
Type: Integer
Required: No

 ** Name **   <a name="Glue-Type-Workflow-Name"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Workflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Workflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Workflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Workflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
