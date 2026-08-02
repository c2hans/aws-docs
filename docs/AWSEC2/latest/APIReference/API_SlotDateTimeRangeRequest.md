---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SlotDateTimeRangeRequest.html
---

# SlotDateTimeRangeRequest
<a name="API_SlotDateTimeRangeRequest"></a>

Describes the time period for a Scheduled Instance to start its first schedule. The time period must span less than one day.

## Contents
<a name="API_SlotDateTimeRangeRequest_Contents"></a>

 ** EarliestTime **
The earliest date and time, in UTC, for the Scheduled Instance to start.
Type: Timestamp
Required: Yes

 ** LatestTime **
The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SlotDateTimeRangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SlotDateTimeRangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SlotDateTimeRangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SlotDateTimeRangeRequest)
