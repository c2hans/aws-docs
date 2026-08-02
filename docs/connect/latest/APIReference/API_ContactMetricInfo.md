---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactMetricInfo.html
---

# ContactMetricInfo
<a name="API_ContactMetricInfo"></a>

Contains the details of a metric to be retrieved for a contact. Use this object to specify which contact level metrics you want to include in your GetContactMetrics request.

## Contents
<a name="API_ContactMetricInfo_Contents"></a>

 ** Name **   <a name="connect-Type-ContactMetricInfo-Name"></a>
The name of the metric to retrieve. Supported values are POSITION\_IN\_QUEUE (returns the contact's current position in the queue) and ESTIMATED\_WAIT\_TIME (returns the predicted wait time in seconds).
Type: String
Valid Values: `ESTIMATED_WAIT_TIME | POSITION_IN_QUEUE`
Required: Yes

## See Also
<a name="API_ContactMetricInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactMetricInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactMetricInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactMetricInfo)
