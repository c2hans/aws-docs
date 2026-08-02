---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_WaitStartedDetails.html
---

# WaitStartedDetails
<a name="API_WaitStartedDetails"></a>

Details about a wait operation that has started.

## Contents
<a name="API_WaitStartedDetails_Contents"></a>

 ** Duration **   <a name="lambda-Type-WaitStartedDetails-Duration"></a>
The duration to wait, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** ScheduledEndTimestamp **   <a name="lambda-Type-WaitStartedDetails-ScheduledEndTimestamp"></a>
The date and time when the wait operation is scheduled to complete, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

## See Also
<a name="API_WaitStartedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/WaitStartedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/WaitStartedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/WaitStartedDetails)
