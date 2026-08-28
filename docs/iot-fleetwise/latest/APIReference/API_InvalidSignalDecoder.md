---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_InvalidSignalDecoder.html
---

# InvalidSignalDecoder
<a name="API_InvalidSignalDecoder"></a>

A reason that a signal decoder isn't valid.

## Contents
<a name="API_InvalidSignalDecoder_Contents"></a>

 ** hint **   <a name="iotfleetwise-Type-InvalidSignalDecoder-hint"></a>
The possible cause for the invalid signal decoder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** name **   <a name="iotfleetwise-Type-InvalidSignalDecoder-name"></a>
The name of a signal decoder that isn't valid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** reason **   <a name="iotfleetwise-Type-InvalidSignalDecoder-reason"></a>
A message about why the signal decoder isn't valid.
Type: String
Valid Values: `DUPLICATE_SIGNAL | CONFLICTING_SIGNAL | SIGNAL_TO_ADD_ALREADY_EXISTS | SIGNAL_NOT_ASSOCIATED_WITH_NETWORK_INTERFACE | NETWORK_INTERFACE_TYPE_INCOMPATIBLE_WITH_SIGNAL_DECODER_TYPE | SIGNAL_NOT_IN_MODEL | CAN_SIGNAL_INFO_IS_NULL | OBD_SIGNAL_INFO_IS_NULL | NO_DECODER_INFO_FOR_SIGNAL_IN_MODEL | MESSAGE_SIGNAL_INFO_IS_NULL | SIGNAL_DECODER_TYPE_INCOMPATIBLE_WITH_MESSAGE_SIGNAL_TYPE | STRUCT_SIZE_MISMATCH | NO_SIGNAL_IN_CATALOG_FOR_DECODER_SIGNAL | SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG | EMPTY_MESSAGE_SIGNAL | CUSTOM_DECODING_SIGNAL_INFO_IS_NULL`
Required: No

## See Also
<a name="API_InvalidSignalDecoder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/InvalidSignalDecoder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/InvalidSignalDecoder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/InvalidSignalDecoder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
