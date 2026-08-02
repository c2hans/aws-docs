---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ClassificationResult.html
---

# ClassificationResult
<a name="API_ClassificationResult"></a>

Details about the sensitive data that was detected on the resource.

## Contents
<a name="API_ClassificationResult_Contents"></a>

 ** AdditionalOccurrences **   <a name="securityhub-Type-ClassificationResult-AdditionalOccurrences"></a>
Indicates whether there are additional occurrences of sensitive data that are not included in the finding. This occurs when the number of occurrences exceeds the maximum that can be included.
Type: Boolean
Required: No

 ** CustomDataIdentifiers **   <a name="securityhub-Type-ClassificationResult-CustomDataIdentifiers"></a>
Provides details about sensitive data that was identified based on customer-defined configuration.
Type: [CustomDataIdentifiersResult](API_CustomDataIdentifiersResult.md) object
Required: No

 ** MimeType **   <a name="securityhub-Type-ClassificationResult-MimeType"></a>
The type of content that the finding applies to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SensitiveData **   <a name="securityhub-Type-ClassificationResult-SensitiveData"></a>
Provides details about sensitive data that was identified based on built-in configuration.
Type: Array of [SensitiveDataResult](API_SensitiveDataResult.md) objects
Required: No

 ** SizeClassified **   <a name="securityhub-Type-ClassificationResult-SizeClassified"></a>
The total size in bytes of the affected data.
Type: Long
Required: No

 ** Status **   <a name="securityhub-Type-ClassificationResult-Status"></a>
The current status of the sensitive data detection.
Type: [ClassificationStatus](API_ClassificationStatus.md) object
Required: No

## See Also
<a name="API_ClassificationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ClassificationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ClassificationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ClassificationResult)
