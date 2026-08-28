---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskCredentials.html
---

# TaskCredentials
<a name="API_TaskCredentials"></a>

Contains details about the credentials that Step Functions uses for a task.

## Contents
<a name="API_TaskCredentials_Contents"></a>

 ** roleArn **   <a name="StepFunctions-Type-TaskCredentials-roleArn"></a>
The ARN of an IAM role that Step Functions assumes for the task. The role can allow cross-account access to resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## See Also
<a name="API_TaskCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TaskCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TaskCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TaskCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
