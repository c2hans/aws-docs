---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_SessionManagedLoggingConfiguration.html
---

# SessionManagedLoggingConfiguration
<a name="API_SessionManagedLoggingConfiguration"></a>

The Amazon EMR-managed logging configuration for a session.

## Contents
<a name="API_SessionManagedLoggingConfiguration_Contents"></a>

 ** Enabled **   <a name="EMR-Type-SessionManagedLoggingConfiguration-Enabled"></a>
Whether Amazon EMR-managed logging is enabled for the session.
Type: Boolean
Required: No

 ** EncryptionKeyArn **   <a name="EMR-Type-SessionManagedLoggingConfiguration-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the managed logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_SessionManagedLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SessionManagedLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SessionManagedLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SessionManagedLoggingConfiguration)
