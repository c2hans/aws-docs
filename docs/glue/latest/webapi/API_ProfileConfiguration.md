---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ProfileConfiguration.html
---

# ProfileConfiguration
<a name="API_ProfileConfiguration"></a>

Specifies the job and session values that an admin configures in an AWS Glue usage profile.

## Contents
<a name="API_ProfileConfiguration_Contents"></a>

 ** JobConfiguration **   <a name="Glue-Type-ProfileConfiguration-JobConfiguration"></a>
A key-value map of configuration parameters for AWS Glue jobs.
Type: String to [ConfigurationObject](API_ConfigurationObject.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SessionConfiguration **   <a name="Glue-Type-ProfileConfiguration-SessionConfiguration"></a>
A key-value map of configuration parameters for AWS Glue sessions.
Type: String to [ConfigurationObject](API_ConfigurationObject.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_ProfileConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ProfileConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ProfileConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ProfileConfiguration)
