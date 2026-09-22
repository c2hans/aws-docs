---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanState.html
---

# ImageScanState
<a name="API_ImageScanState"></a>

Shows the vulnerability scan status for a specific image, and the reason for that status.

## Contents
<a name="API_ImageScanState_Contents"></a>

 ** reason **   <a name="imagebuilder-Type-ImageScanState-reason"></a>
The reason for the scan status for the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-ImageScanState-status"></a>
The current state of vulnerability scans for the image. The scan starts as `PENDING` and moves through `SCANNING` and `COLLECTING` to `COMPLETED`. Image Builder sets the status to `ABANDONED` if the image reaches a terminal state before the scan finding collection completes. A scan can also end as `FAILED` or `TIMED_OUT`.
Type: String
Valid Values: `PENDING | SCANNING | COLLECTING | COMPLETED | ABANDONED | FAILED | TIMED_OUT`
Required: No

## See Also
<a name="API_ImageScanState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanState)
