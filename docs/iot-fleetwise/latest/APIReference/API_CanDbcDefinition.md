---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CanDbcDefinition.html
---

# CanDbcDefinition
<a name="API_CanDbcDefinition"></a>

Configurations used to create a decoder manifest.

## Contents
<a name="API_CanDbcDefinition_Contents"></a>

 ** canDbcFiles **   <a name="iotfleetwise-Type-CanDbcDefinition-canDbcFiles"></a>
A list of DBC files. You can upload only one DBC file for each network interface and specify up to five (inclusive) files in the list. The DBC file can be a maximum size of 200 MB.
Type: Array of Base64-encoded binary data objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 200000000.
Required: Yes

 ** networkInterface **   <a name="iotfleetwise-Type-CanDbcDefinition-networkInterface"></a>
Contains information about a network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[-a-zA-Z0-9_.]+`
Required: Yes

 ** signalsMap **   <a name="iotfleetwise-Type-CanDbcDefinition-signalsMap"></a>
Pairs every signal specified in your vehicle model with a signal decoder.
Type: String to string map
Required: No

## See Also
<a name="API_CanDbcDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CanDbcDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CanDbcDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CanDbcDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
