---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanStatus.html
---

# ImageScanStatus
<a name="API_ImageScanStatus"></a>

The current status of an image scan.

## Contents
<a name="API_ImageScanStatus_Contents"></a>

 ** description **   <a name="ECR-Type-ImageScanStatus-description"></a>
The description of the image scan status.
Type: String
Required: No

 ** status **   <a name="ECR-Type-ImageScanStatus-status"></a>
The current state of an image scan.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED | UNSUPPORTED_IMAGE | ACTIVE | PENDING | SCAN_ELIGIBILITY_EXPIRED | FINDINGS_UNAVAILABLE | LIMIT_EXCEEDED | IMAGE_ARCHIVED`
Required: No

## See Also
<a name="API_ImageScanStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageScanStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageScanStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageScanStatus)
