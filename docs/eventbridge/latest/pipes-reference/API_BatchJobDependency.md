---
source_url: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchJobDependency.html
---

# BatchJobDependency
<a name="API_BatchJobDependency"></a>

An object that represents an AWS Batch job dependency.

## Contents
<a name="API_BatchJobDependency_Contents"></a>

 ** JobId **   <a name="eventbridge-Type-BatchJobDependency-JobId"></a>
The job ID of the AWS Batch job that's associated with this dependency.
Type: String
Required: No

 ** Type **   <a name="eventbridge-Type-BatchJobDependency-Type"></a>
The type of the job dependency.
Type: String
Valid Values: `N_TO_N | SEQUENTIAL`
Required: No

## See Also
<a name="API_BatchJobDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/BatchJobDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/BatchJobDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/BatchJobDependency)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge Pipes. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
