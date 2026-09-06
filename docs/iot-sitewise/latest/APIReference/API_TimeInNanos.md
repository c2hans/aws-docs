---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeInNanos.html
---

# TimeInNanos
<a name="API_TimeInNanos"></a>

Contains a timestamp with optional nanosecond granularity.

## Contents
<a name="API_TimeInNanos_Contents"></a>

 ** timeInSeconds **   <a name="iotsitewise-Type-TimeInNanos-timeInSeconds"></a>
The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by `offsetInNanos`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 9223372036854774.
Required: Yes

 ** offsetInNanos **   <a name="iotsitewise-Type-TimeInNanos-offsetInNanos"></a>
The nanosecond offset from `timeInSeconds`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999999999.
Required: No

## See Also
<a name="API_TimeInNanos_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TimeInNanos)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TimeInNanos)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TimeInNanos)
