---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_IncrementalScanDetails.html
---

# IncrementalScanDetails
<a name="API_IncrementalScanDetails"></a>

Contains information about the incremental scan configuration.

## Contents
<a name="API_IncrementalScanDetails_Contents"></a>

 ** baselineResourceArn **   <a name="guardduty-Type-IncrementalScanDetails-baselineResourceArn"></a>
Amazon Resource Name (ARN) of the baseline resource used for incremental scanning. The scan will only process changes since this baseline resource was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_IncrementalScanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/IncrementalScanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/IncrementalScanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/IncrementalScanDetails)
