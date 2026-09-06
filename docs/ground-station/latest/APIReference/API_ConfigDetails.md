---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigDetails.html
---

# ConfigDetails
<a name="API_ConfigDetails"></a>

Details for certain `Config` object types in a contact.

## Contents
<a name="API_ConfigDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** antennaDemodDecodeDetails **   <a name="groundstation-Type-ConfigDetails-antennaDemodDecodeDetails"></a>
Details for antenna demod decode `Config` in a contact.
Type: [AntennaDemodDecodeDetails](API_AntennaDemodDecodeDetails.md) object
Required: No

 ** endpointDetails **   <a name="groundstation-Type-ConfigDetails-endpointDetails"></a>
Information about the endpoint details.
Type: [EndpointDetails](API_EndpointDetails.md) object
Required: No

 ** s3RecordingDetails **   <a name="groundstation-Type-ConfigDetails-s3RecordingDetails"></a>
Details for an S3 recording `Config` in a contact.
Type: [S3RecordingDetails](API_S3RecordingDetails.md) object
Required: No

## See Also
<a name="API_ConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ConfigDetails)
