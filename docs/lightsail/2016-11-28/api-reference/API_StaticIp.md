---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StaticIp.html
---

# StaticIp
<a name="API_StaticIp"></a>

Describes a static IP.

## Contents
<a name="API_StaticIp_Contents"></a>

 ** arn **   <a name="Lightsail-Type-StaticIp-arn"></a>
The Amazon Resource Name (ARN) of the static IP (`arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** attachedTo **   <a name="Lightsail-Type-StaticIp-attachedTo"></a>
The instance where the static IP is attached (`Amazon_Linux-1GB-Ohio-1`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** createdAt **   <a name="Lightsail-Type-StaticIp-createdAt"></a>
The timestamp when the static IP was created (`1479735304.222`).
Type: Timestamp
Required: No

 ** ipAddress **   <a name="Lightsail-Type-StaticIp-ipAddress"></a>
The static IP address.
Type: String
Pattern: `([0-9]{1,3}\.){3}[0-9]{1,3}`
Required: No

 ** isAttached **   <a name="Lightsail-Type-StaticIp-isAttached"></a>
A Boolean value indicating whether the static IP is attached.
Type: Boolean
Required: No

 ** location **   <a name="Lightsail-Type-StaticIp-location"></a>
The region and Availability Zone where the static IP was created.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-StaticIp-name"></a>
The name of the static IP (`StaticIP-Ohio-EXAMPLE`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-StaticIp-resourceType"></a>
The resource type (usually `StaticIp`).
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** supportCode **   <a name="Lightsail-Type-StaticIp-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

## See Also
<a name="API_StaticIp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/StaticIp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/StaticIp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/StaticIp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
