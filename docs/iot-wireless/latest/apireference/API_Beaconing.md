---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Beaconing.html
---

# Beaconing
<a name="API_Beaconing"></a>

Beaconing parameters for configuring the wireless gateways.

## Contents
<a name="API_Beaconing_Contents"></a>

 ** DataRate **   <a name="iotwireless-Type-Beaconing-DataRate"></a>
The data rate for gateways that are sending the beacons.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** Frequencies **   <a name="iotwireless-Type-Beaconing-Frequencies"></a>
The frequency list for the gateways to send the beacons.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Range: Minimum value of 100000000. Maximum value of 1000000000.
Required: No

## See Also
<a name="API_Beaconing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/Beaconing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/Beaconing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/Beaconing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
