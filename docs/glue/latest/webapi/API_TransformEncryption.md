---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TransformEncryption.html
---

# TransformEncryption
<a name="API_TransformEncryption"></a>

The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.

Additionally, imported labels and trained transforms can now be encrypted using a customer provided KMS key.

## Contents
<a name="API_TransformEncryption_Contents"></a>

 ** MlUserDataEncryption **   <a name="Glue-Type-TransformEncryption-MlUserDataEncryption"></a>
An `MLUserDataEncryption` object containing the encryption mode and customer-provided KMS key ID.
Type: [MLUserDataEncryption](API_MLUserDataEncryption.md) object
Required: No

 ** TaskRunSecurityConfigurationName **   <a name="Glue-Type-TransformEncryption-TaskRunSecurityConfigurationName"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TransformEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TransformEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TransformEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TransformEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
