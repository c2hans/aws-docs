---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_JobDependency.html
---

# JobDependency
<a name="API_JobDependency"></a>

An object that represents an AWS Batch job dependency.

## Contents
<a name="API_JobDependency_Contents"></a>

 ** jobId **   <a name="Batch-Type-JobDependency-jobId"></a>
The job ID of the AWS Batch job that's associated with this dependency.
Type: String
Required: No

 ** type **   <a name="Batch-Type-JobDependency-type"></a>
The type of the job dependency.
Type: String
Valid Values: `N_TO_N | SEQUENTIAL`
Required: No

## See Also
<a name="API_JobDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobDependency)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
