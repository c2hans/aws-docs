---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_AWSSessionCredentials.html
---

# AWSSessionCredentials
<a name="API_AWSSessionCredentials"></a>

Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifact for the pipeline in CodePipeline.

## Contents
<a name="API_AWSSessionCredentials_Contents"></a>

 ** accessKeyId **   <a name="CodePipeline-Type-AWSSessionCredentials-accessKeyId"></a>
The access key for the session.
Type: String
Required: Yes

 ** secretAccessKey **   <a name="CodePipeline-Type-AWSSessionCredentials-secretAccessKey"></a>
The secret access key for the session.
Type: String
Required: Yes

 ** sessionToken **   <a name="CodePipeline-Type-AWSSessionCredentials-sessionToken"></a>
The token for the session.
Type: String
Required: Yes

## See Also
<a name="API_AWSSessionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/AWSSessionCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/AWSSessionCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/AWSSessionCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
