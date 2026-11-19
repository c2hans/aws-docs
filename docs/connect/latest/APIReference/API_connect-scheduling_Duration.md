---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_Duration.html
---

# Duration

A length of time, expressed as a value and the unit it is counted in.

## Contents
<a name="API_connect-scheduling_Duration_Contents"></a>

 ** Unit **   <a name="connect-Type-connect-scheduling_Duration-Unit"></a>
The unit the value is counted in.
Type: String
Valid Values: `MINUTES | HOURS | DAYS`
Required: Yes

 ** Value **   <a name="connect-Type-connect-scheduling_Duration-Value"></a>
The number of units of time. You can use a negative value to report an overdrawn balance. The value must be within 876,000 hours (100 years) of zero: at most 52,560,000 `MINUTES`, 876,000 `HOURS`, or 36,500 `DAYS`.
Type: Integer
Valid Range: Minimum value of -52560000. Maximum value of 52560000.
Required: Yes

## See Also
<a name="API_connect-scheduling_Duration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/Duration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/Duration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/Duration)
