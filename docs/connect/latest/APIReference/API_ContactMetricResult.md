---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactMetricResult.html
---

# ContactMetricResult
<a name="API_ContactMetricResult"></a>

Contains the result of a requested metric for the contact. This object is returned as part of the GetContactMetrics response and includes both the metric name and its calculated value.

## Contents
<a name="API_ContactMetricResult_Contents"></a>

 ** Name **   <a name="connect-Type-ContactMetricResult-Name"></a>
The name of the metric that was retrieved. This corresponds to the metric name specified in the request, such as POSITION\_IN\_QUEUE or ESTIMATED\_WAIT\_TIME.
Type: String
Valid Values: `ESTIMATED_WAIT_TIME | POSITION_IN_QUEUE`
Required: Yes

 ** Value **   <a name="connect-Type-ContactMetricResult-Value"></a>
The calculated value for the requested metric. This object contains the numeric result based on the contact's current state in the queue.
Type: [ContactMetricValue](API_ContactMetricValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ContactMetricResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactMetricResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactMetricResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactMetricResult)
