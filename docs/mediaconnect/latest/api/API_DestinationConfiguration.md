---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationConfiguration.html
---

# DestinationConfiguration
<a name="API_DestinationConfiguration"></a>

 The transport parameters that you want to associate with an outbound media stream.

## Contents
<a name="API_DestinationConfiguration_Contents"></a>

 ** destinationIp **   <a name="mediaconnect-Type-DestinationConfiguration-destinationIp"></a>
The IP address where you want MediaConnect to send contents of the media stream.
Type: String
Required: Yes

 ** destinationPort **   <a name="mediaconnect-Type-DestinationConfiguration-destinationPort"></a>
 The port that you want MediaConnect to use when it distributes the media stream to the output.
Type: Integer
Required: Yes

 ** interface **   <a name="mediaconnect-Type-DestinationConfiguration-interface"></a>
 The VPC interface that you want to use for the media stream associated with the output.
Type: [Interface](API_Interface.md) object
Required: Yes

 ** outboundIp **   <a name="mediaconnect-Type-DestinationConfiguration-outboundIp"></a>
The IP address that the receiver requires in order to establish a connection with the flow. This value is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the CDI or ST 2110 JPEG XS or protocol.
Type: String
Required: Yes

## See Also
<a name="API_DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
