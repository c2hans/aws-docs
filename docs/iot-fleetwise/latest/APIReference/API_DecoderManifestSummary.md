---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DecoderManifestSummary.html
---

# DecoderManifestSummary
<a name="API_DecoderManifestSummary"></a>

Information about a created decoder manifest. You can use the [ListDecoderManifests](API_ListDecoderManifests.md) API operation to return this information about multiple decoder manifests.

## Contents
<a name="API_DecoderManifestSummary_Contents"></a>

 ** creationTime **   <a name="iotfleetwise-Type-DecoderManifestSummary-creationTime"></a>
The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: Yes

 ** lastModificationTime **   <a name="iotfleetwise-Type-DecoderManifestSummary-lastModificationTime"></a>
The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: Yes

 ** arn **   <a name="iotfleetwise-Type-DecoderManifestSummary-arn"></a>
The ARN of a vehicle model (model manifest) associated with the decoder manifest.
Type: String
Required: No

 ** description **   <a name="iotfleetwise-Type-DecoderManifestSummary-description"></a>
A brief description of the decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** message **   <a name="iotfleetwise-Type-DecoderManifestSummary-message"></a>
The detailed message for the decoder manifest. When a decoder manifest is in an `INVALID` status, the message contains detailed reason and help information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** modelManifestArn **   <a name="iotfleetwise-Type-DecoderManifestSummary-modelManifestArn"></a>
The ARN of a vehicle model (model manifest) associated with the decoder manifest.
Type: String
Required: No

 ** name **   <a name="iotfleetwise-Type-DecoderManifestSummary-name"></a>
The name of the decoder manifest.
Type: String
Required: No

 ** status **   <a name="iotfleetwise-Type-DecoderManifestSummary-status"></a>
The state of the decoder manifest. If the status is `ACTIVE`, the decoder manifest can't be edited. If the status is marked `DRAFT`, you can edit the decoder manifest.
Type: String
Valid Values: `ACTIVE | DRAFT | INVALID | VALIDATING`
Required: No

## See Also
<a name="API_DecoderManifestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/DecoderManifestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/DecoderManifestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/DecoderManifestSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
