---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_RollingInterval.html
---

# RollingInterval
<a name="API_RollingInterval"></a>

If the interval for this SLO is a rolling interval, this structure contains the interval specifications.

## Contents
<a name="API_RollingInterval_Contents"></a>

 ** Duration **   <a name="applicationsignals-Type-RollingInterval-Duration"></a>
Specifies the duration of each rolling interval. For example, if `Duration` is `7` and `DurationUnit` is `DAY`, each rolling interval is seven days.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** DurationUnit **   <a name="applicationsignals-Type-RollingInterval-DurationUnit"></a>
Specifies the rolling interval unit.
Type: String
Valid Values: `MINUTE | HOUR | DAY | MONTH`
Required: Yes

## See Also
<a name="API_RollingInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/RollingInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/RollingInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/RollingInterval)
