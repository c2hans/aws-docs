---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CanInterface.html
---

# CanInterface
<a name="API_CanInterface"></a>

A single controller area network (CAN) device interface.

## Contents
<a name="API_CanInterface_Contents"></a>

 ** name **   <a name="iotfleetwise-Type-CanInterface-name"></a>
The unique name of the interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** protocolName **   <a name="iotfleetwise-Type-CanInterface-protocolName"></a>
The name of the communication protocol for the interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** protocolVersion **   <a name="iotfleetwise-Type-CanInterface-protocolVersion"></a>
The version of the communication protocol for the interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

## See Also
<a name="API_CanInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CanInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CanInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CanInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
