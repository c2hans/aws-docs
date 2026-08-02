---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Domain.html
---

# Domain
<a name="API_Domain"></a>

Describes a domain where you are storing recordsets.

## Contents
<a name="API_Domain_Contents"></a>

 ** arn **   <a name="Lightsail-Type-Domain-arn"></a>
The Amazon Resource Name (ARN) of the domain recordset (`arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-Domain-createdAt"></a>
The date when the domain recordset was created.
Type: Timestamp
Required: No

 ** domainEntries **   <a name="Lightsail-Type-Domain-domainEntries"></a>
An array of key-value pairs containing information about the domain entries.
Type: Array of [DomainEntry](API_DomainEntry.md) objects
Required: No

 ** location **   <a name="Lightsail-Type-Domain-location"></a>
The AWS Region and Availability Zones where the domain recordset was created.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-Domain-name"></a>
The name of the domain.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** registeredDomainDelegationInfo **   <a name="Lightsail-Type-Domain-registeredDomainDelegationInfo"></a>
An object that describes the state of the Route 53 domain delegation to a Lightsail DNS zone.
Type: [RegisteredDomainDelegationInfo](API_RegisteredDomainDelegationInfo.md) object
Required: No

 ** resourceType **   <a name="Lightsail-Type-Domain-resourceType"></a>
The resource type.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** supportCode **   <a name="Lightsail-Type-Domain-supportCode"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Domain-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Domain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Domain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Domain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Domain)
