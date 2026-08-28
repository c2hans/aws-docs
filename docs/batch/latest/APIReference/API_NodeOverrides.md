---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_NodeOverrides.html
---

# NodeOverrides
<a name="API_NodeOverrides"></a>

An object that represents any node overrides to a job definition that's used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

**Note**
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs. Rather, use `containerOverrides` instead.

## Contents
<a name="API_NodeOverrides_Contents"></a>

 ** nodePropertyOverrides **   <a name="Batch-Type-NodeOverrides-nodePropertyOverrides"></a>
The node property overrides for the job.
Type: Array of [NodePropertyOverride](API_NodePropertyOverride.md) objects
Required: No

 ** numNodes **   <a name="Batch-Type-NodeOverrides-numNodes"></a>
The number of nodes to use with a multi-node parallel job. This value overrides the number of nodes that are specified in the job definition. To use this override, you must meet the following conditions:
+ There must be at least one node range in your job definition that has an open upper boundary, such as `:` or `n:`.
+ The lower boundary of the node range that's specified in the job definition must be fewer than the number of nodes specified in the override.
+ The main node index that's specified in the job definition must be fewer than the number of nodes specified in the override.
Type: Integer
Required: No

## See Also
<a name="API_NodeOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
