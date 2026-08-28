---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CrossAccountConfiguration.html
---

# CrossAccountConfiguration
<a name="API_CrossAccountConfiguration"></a>

This structure contains information about the cross-account configuration in the account.

## Contents
<a name="API_CrossAccountConfiguration_Contents"></a>

 ** sourceRoleArn **   <a name="cloudwatchinvestigations-Type-CrossAccountConfiguration-sourceRoleArn"></a>
The ARN of an existing role which will be used to do investigations on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_CrossAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/CrossAccountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/CrossAccountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/CrossAccountConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch investigations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchinvestigations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
