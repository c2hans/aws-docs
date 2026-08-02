---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Attachment.html
---

# Attachment
<a name="API_Attachment"></a>

An object representing a container instance or task attachment.

## Contents
<a name="API_Attachment_Contents"></a>

 ** details **   <a name="ECS-Type-Attachment-details"></a>
Details of the attachment.
For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
For Service Connect services, this includes `portName`, `clientAliases`, `discoveryName`, and `ingressPortOverride`.
For Elastic Block Storage, this includes `roleArn`, `deleteOnTermination`, `volumeName`, `volumeId`, and `statusReason` (only when the attachment fails to create or attach).
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** id **   <a name="ECS-Type-Attachment-id"></a>
The unique identifier for the attachment.
Type: String
Required: No

 ** status **   <a name="ECS-Type-Attachment-status"></a>
 The status of the attachment. Valid values are `PRECREATED`, `CREATED`, `ATTACHING`, `ATTACHED`, `DETACHING`, `DETACHED`, `DELETED`, and `FAILED`.
Type: String
Required: No

 ** type **   <a name="ECS-Type-Attachment-type"></a>
The type of the attachment, such as `ElasticNetworkInterface`, `Service Connect`, and `AmazonElasticBlockStorage`.
Type: String
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Attachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Attachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Attachment)
