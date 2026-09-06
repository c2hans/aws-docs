---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AcquiredLimit.html
---

# AcquiredLimit
<a name="API_AcquiredLimit"></a>

Provides information about the number of resources used.

## Contents
<a name="API_AcquiredLimit_Contents"></a>

 ** count **   <a name="deadlinecloud-Type-AcquiredLimit-count"></a>
The number of limit resources used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: Yes

 ** limitId **   <a name="deadlinecloud-Type-AcquiredLimit-limitId"></a>
The unique identifier of the limit.
Type: String
Pattern: `limit-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_AcquiredLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcquiredLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcquiredLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcquiredLimit)
