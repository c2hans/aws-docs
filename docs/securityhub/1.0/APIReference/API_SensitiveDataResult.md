---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SensitiveDataResult.html
---

# SensitiveDataResult
<a name="API_SensitiveDataResult"></a>

Contains a detected instance of sensitive data that are based on built-in identifiers.

## Contents
<a name="API_SensitiveDataResult_Contents"></a>

 ** Category **   <a name="securityhub-Type-SensitiveDataResult-Category"></a>
The category of sensitive data that was detected. For example, the category can indicate that the sensitive data involved credentials, financial information, or personal information.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Detections **   <a name="securityhub-Type-SensitiveDataResult-Detections"></a>
The list of detected instances of sensitive data.
Type: Array of [SensitiveDataDetections](API_SensitiveDataDetections.md) objects
Required: No

 ** TotalCount **   <a name="securityhub-Type-SensitiveDataResult-TotalCount"></a>
The total number of occurrences of sensitive data.
Type: Long
Required: No

## See Also
<a name="API_SensitiveDataResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SensitiveDataResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SensitiveDataResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SensitiveDataResult)
