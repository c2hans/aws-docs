---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_LakeFormationConfiguration.html
---

# LakeFormationConfiguration
<a name="API_LakeFormationConfiguration"></a>

Specifies AWS Lake Formation configuration settings for the crawler.

## Contents
<a name="API_LakeFormationConfiguration_Contents"></a>

 ** AccountId **   <a name="Glue-Type-LakeFormationConfiguration-AccountId"></a>
Required for cross account crawls. For same account crawls as the target data, this can be left as null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Required: No

 ** UseLakeFormationCredentials **   <a name="Glue-Type-LakeFormationConfiguration-UseLakeFormationCredentials"></a>
Specifies whether to use AWS Lake Formation credentials for the crawler instead of the IAM role credentials.
Type: Boolean
Required: No

## See Also
<a name="API_LakeFormationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/LakeFormationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/LakeFormationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/LakeFormationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
