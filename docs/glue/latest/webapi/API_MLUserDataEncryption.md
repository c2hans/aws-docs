---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MLUserDataEncryption.html
---

# MLUserDataEncryption
<a name="API_MLUserDataEncryption"></a>

The encryption-at-rest settings of the transform that apply to accessing user data.

## Contents
<a name="API_MLUserDataEncryption_Contents"></a>

 ** MlUserDataEncryptionMode **   <a name="Glue-Type-MLUserDataEncryption-MlUserDataEncryptionMode"></a>
The encryption mode applied to user data. Valid values are:
+ DISABLED: encryption is disabled
+ SSEKMS: use of server-side encryption with AWS Key Management Service (SSE-KMS) for user data stored in Amazon S3.
Type: String
Valid Values: `DISABLED | SSE-KMS`
Required: Yes

 ** KmsKeyId **   <a name="Glue-Type-MLUserDataEncryption-KmsKeyId"></a>
The ID for the customer-provided KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_MLUserDataEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MLUserDataEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MLUserDataEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MLUserDataEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
