---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Goal.html
---

# Goal
<a name="API_Goal"></a>

This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.

## Contents
<a name="API_Goal_Contents"></a>

 ** AttainmentGoal **   <a name="applicationsignals-Type-Goal-AttainmentGoal"></a>
The threshold that determines if the goal is being met.
If this is a period-based SLO, the attainment goal is the percentage of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.
If this is a request-based SLO, the attainment goal is the percentage of requests that must be successful to meet the attainment goal.
If you omit this parameter, 99 is used to represent 99% as the attainment goal.
Type: Double
Required: No

 ** Interval **   <a name="applicationsignals-Type-Goal-Interval"></a>
The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.
If you omit this parameter, a rolling interval of 7 days is used.
Type: [Interval](API_Interval.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** WarningThreshold **   <a name="applicationsignals-Type-Goal-WarningThreshold"></a>
The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used.
Type: Double
Required: No

## See Also
<a name="API_Goal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Goal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Goal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Goal)
