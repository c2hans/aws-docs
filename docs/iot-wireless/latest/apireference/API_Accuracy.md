---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Accuracy.html
---

# Accuracy
<a name="API_Accuracy"></a>

The accuracy of the estimated position in meters. An empty value indicates that no position data is available. A value of ‘0.0’ value indicates that position data is available. This data corresponds to the position information that you specified instead of the position computed by solver.

## Contents
<a name="API_Accuracy_Contents"></a>

 ** HorizontalAccuracy **   <a name="iotwireless-Type-Accuracy-HorizontalAccuracy"></a>
The horizontal accuracy of the estimated position, which is the difference between the estimated location and the actual device location.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** VerticalAccuracy **   <a name="iotwireless-Type-Accuracy-VerticalAccuracy"></a>
The vertical accuracy of the estimated position, which is the difference between the estimated altitude and actual device latitude in meters.
Type: Float
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Accuracy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/Accuracy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/Accuracy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/Accuracy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
