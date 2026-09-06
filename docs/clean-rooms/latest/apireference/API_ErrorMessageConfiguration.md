---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ErrorMessageConfiguration.html
---

# ErrorMessageConfiguration
<a name="API_ErrorMessageConfiguration"></a>

A structure that defines the level of detail included in error messages returned by PySpark jobs. This configuration allows you to control the verbosity of error messages to help with troubleshooting PySpark jobs while maintaining appropriate security controls.

## Contents
<a name="API_ErrorMessageConfiguration_Contents"></a>

 ** type **   <a name="API-Type-ErrorMessageConfiguration-type"></a>
The level of detail for error messages returned by the PySpark job. When set to DETAILED, error messages include more information to help troubleshoot issues with your PySpark job.
Because this setting may expose sensitive data, it is recommended for development and testing environments.
Type: String
Valid Values: `DETAILED`
Required: Yes

## See Also
<a name="API_ErrorMessageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ErrorMessageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ErrorMessageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ErrorMessageConfiguration)
