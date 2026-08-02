---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_RuntimeVersion.html
---

# RuntimeVersion
<a name="API_RuntimeVersion"></a>

This structure contains information about one canary runtime version. For more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).

## Contents
<a name="API_RuntimeVersion_Contents"></a>

 ** DeprecationDate **   <a name="synthetics-Type-RuntimeVersion-DeprecationDate"></a>
If this runtime version is deprecated, this value is the date of deprecation.
Type: Timestamp
Required: No

 ** Description **   <a name="synthetics-Type-RuntimeVersion-Description"></a>
A description of the runtime version, created by Amazon.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ReleaseDate **   <a name="synthetics-Type-RuntimeVersion-ReleaseDate"></a>
The date that the runtime version was released.
Type: Timestamp
Required: No

 ** VersionName **   <a name="synthetics-Type-RuntimeVersion-VersionName"></a>
The name of the runtime version. For a list of valid runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_RuntimeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/RuntimeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/RuntimeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/RuntimeVersion)
