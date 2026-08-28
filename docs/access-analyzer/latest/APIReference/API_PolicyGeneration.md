---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PolicyGeneration.html
---

# PolicyGeneration
<a name="API_PolicyGeneration"></a>

Contains details about the policy generation status and properties.

## Contents
<a name="API_PolicyGeneration_Contents"></a>

 ** jobId **   <a name="accessanalyzer-Type-PolicyGeneration-jobId"></a>
The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.
Type: String
Required: Yes

 ** principalArn **   <a name="accessanalyzer-Type-PolicyGeneration-principalArn"></a>
The ARN of the IAM entity (user or role) for which you are generating a policy.
Type: String
Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`
Required: Yes

 ** startedOn **   <a name="accessanalyzer-Type-PolicyGeneration-startedOn"></a>
A timestamp of when the policy generation started.
Type: Timestamp
Required: Yes

 ** status **   <a name="accessanalyzer-Type-PolicyGeneration-status"></a>
The status of the policy generation request.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED | CANCELED`
Required: Yes

 ** completedOn **   <a name="accessanalyzer-Type-PolicyGeneration-completedOn"></a>
A timestamp of when the policy generation was completed.
Type: Timestamp
Required: No

## See Also
<a name="API_PolicyGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PolicyGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PolicyGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PolicyGeneration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
