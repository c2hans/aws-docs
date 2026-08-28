---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ConnectivityInfo.html
---

# ConnectivityInfo
<a name="API_ConnectivityInfo"></a>

Contains information about an endpoint and port where client devices can connect to an MQTT broker on a Greengrass core device.

## Contents
<a name="API_ConnectivityInfo_Contents"></a>

 ** HostAddress **   <a name="greengrassv2-Type-ConnectivityInfo-HostAddress"></a>
The IP address or DNS address where client devices can connect to an MQTT broker on the Greengrass core device.
Type: String
Required: No

 ** Id **   <a name="greengrassv2-Type-ConnectivityInfo-Id"></a>
An ID for the connectivity information.
Type: String
Required: No

 ** Metadata **   <a name="greengrassv2-Type-ConnectivityInfo-Metadata"></a>
Additional metadata to provide to client devices that connect to this core device.
Type: String
Required: No

 ** PortNumber **   <a name="greengrassv2-Type-ConnectivityInfo-PortNumber"></a>
The port where the MQTT broker operates on the core device. This port is typically 8883, which is the default port for the MQTT broker component that runs on core devices.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_ConnectivityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ConnectivityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ConnectivityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ConnectivityInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
