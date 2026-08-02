---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactMetricValue.html
---

# ContactMetricValue
<a name="API_ContactMetricValue"></a>

Contains the numeric value of a contact metric result.

## Contents
<a name="API_ContactMetricValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Number **   <a name="connect-Type-ContactMetricValue-Number"></a>
The numeric value of the metric result. For POSITION\_IN\_QUEUE, this represents the contact's current position in the queue (e.g., 3.00 means third in line). For ESTIMATED\_WAIT\_TIME, this represents the predicted wait time in seconds (e.g., 120.00 means approximately 2 minutes).
Type: Double
Required: No

## See Also
<a name="API_ContactMetricValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactMetricValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactMetricValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactMetricValue)
