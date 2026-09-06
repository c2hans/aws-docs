---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Instance.html
---

# Instance
<a name="API_Instance"></a>

Describes an instance (a virtual private server).

## Contents
<a name="API_Instance_Contents"></a>

 ** addOns **   <a name="Lightsail-Type-Instance-addOns"></a>
An array of objects representing the add-ons enabled on the instance.
Type: Array of [AddOn](API_AddOn.md) objects
Required: No

 ** arn **   <a name="Lightsail-Type-Instance-arn"></a>
The Amazon Resource Name (ARN) of the instance (`arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** blueprintId **   <a name="Lightsail-Type-Instance-blueprintId"></a>
The blueprint ID (`amazon_linux_2023`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** blueprintName **   <a name="Lightsail-Type-Instance-blueprintName"></a>
The friendly name of the blueprint (`Amazon Linux 2023`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** bundleId **   <a name="Lightsail-Type-Instance-bundleId"></a>
The bundle for the instance (`micro_x_x`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-Instance-createdAt"></a>
The timestamp when the instance was created (`1479734909.17`) in Unix time format.
Type: Timestamp
Required: No

 ** hardware **   <a name="Lightsail-Type-Instance-hardware"></a>
The size of the vCPU and the amount of RAM for the instance.
Type: [InstanceHardware](API_InstanceHardware.md) object
Required: No

 ** ipAddressType **   <a name="Lightsail-Type-Instance-ipAddressType"></a>
The IP address type of the instance.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** ipv6Addresses **   <a name="Lightsail-Type-Instance-ipv6Addresses"></a>
The IPv6 addresses of the instance.
Type: Array of strings
Pattern: `([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}`
Required: No

 ** isStaticIp **   <a name="Lightsail-Type-Instance-isStaticIp"></a>
A Boolean value indicating whether this instance has a static IP assigned to it.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-Instance-location"></a>
The region name and Availability Zone where the instance is located.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** metadataOptions **   <a name="Lightsail-Type-Instance-metadataOptions"></a>
The metadata options for the Amazon Lightsail instance.
Type: [InstanceMetadataOptions](API_InstanceMetadataOptions.md) object
Required: No

 ** name **   <a name="Lightsail-Type-Instance-name"></a>
The name the user gave the instance (`Amazon_Linux_2023-1`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** networking **   <a name="Lightsail-Type-Instance-networking"></a>
Information about the public ports and monthly data transfer rates for the instance.
Type: [InstanceNetworking](API_InstanceNetworking.md) object
Required: No

 ** privateIpAddress **   <a name="Lightsail-Type-Instance-privateIpAddress"></a>
The private IP address of the instance.
Type: String
Pattern: `([0-9]{1,3}\.){3}[0-9]{1,3}`
Required: No

 ** publicIpAddress **   <a name="Lightsail-Type-Instance-publicIpAddress"></a>
The public IP address of the instance.
Type: String
Pattern: `([0-9]{1,3}\.){3}[0-9]{1,3}`
Required: No

 ** resourceType **   <a name="Lightsail-Type-Instance-resourceType"></a>
The type of resource (usually `Instance`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sshKeyName **   <a name="Lightsail-Type-Instance-sshKeyName"></a>
The name of the SSH key being used to connect to the instance (`LightsailDefaultKeyPair`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** state **   <a name="Lightsail-Type-Instance-state"></a>
The status code and the state (`running`) for the instance.
Type: [InstanceState](API_InstanceState.md) object
Required: No

 ** supportCode **   <a name="Lightsail-Type-Instance-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Instance-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** username **   <a name="Lightsail-Type-Instance-username"></a>
The user name for connecting to the instance (`ec2-user`).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Instance)
