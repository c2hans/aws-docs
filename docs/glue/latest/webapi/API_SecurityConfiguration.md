---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SecurityConfiguration.html
---

# SecurityConfiguration
<a name="API_SecurityConfiguration"></a>

Specifies a security configuration.

## Contents
<a name="API_SecurityConfiguration_Contents"></a>

 ** CreatedTimeStamp **   <a name="Glue-Type-SecurityConfiguration-CreatedTimeStamp"></a>
The time at which this security configuration was created.
Type: Timestamp
Required: No

 ** EncryptionConfiguration **   <a name="Glue-Type-SecurityConfiguration-EncryptionConfiguration"></a>
The encryption configuration associated with this security configuration.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** Name **   <a name="Glue-Type-SecurityConfiguration-Name"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_SecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SecurityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SecurityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SecurityConfiguration)
