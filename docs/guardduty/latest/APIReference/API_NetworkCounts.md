---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_NetworkCounts.html
---

# NetworkCounts
<a name="API_NetworkCounts"></a>

Contains counts that describe network activity, such as the number of requests or connection attempts.

## Contents
<a name="API_NetworkCounts_Contents"></a>

 ** requestCount **   <a name="guardduty-Type-NetworkCounts-requestCount"></a>
The number of requests.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** resetAttempts **   <a name="guardduty-Type-NetworkCounts-resetAttempts"></a>
The number of connection attempts that were reset.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** suspiciousAttempts **   <a name="guardduty-Type-NetworkCounts-suspiciousAttempts"></a>
The number of connection attempts that were suspicious.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** totalAttempts **   <a name="guardduty-Type-NetworkCounts-totalAttempts"></a>
The total number of connection attempts.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_NetworkCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/NetworkCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/NetworkCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/NetworkCounts)
