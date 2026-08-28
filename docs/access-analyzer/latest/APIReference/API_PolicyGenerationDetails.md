---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PolicyGenerationDetails.html
---

# PolicyGenerationDetails
<a name="API_PolicyGenerationDetails"></a>

Contains the ARN details about the IAM entity for which the policy is generated.

## Contents
<a name="API_PolicyGenerationDetails_Contents"></a>

 ** principalArn **   <a name="accessanalyzer-Type-PolicyGenerationDetails-principalArn"></a>
The ARN of the IAM entity (user or role) for which you are generating a policy.
Type: String
Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`
Required: Yes

## See Also
<a name="API_PolicyGenerationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PolicyGenerationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PolicyGenerationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PolicyGenerationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
