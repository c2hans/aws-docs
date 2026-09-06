---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContactMethod.html
---

# ContactMethod
<a name="API_ContactMethod"></a>

Describes a contact method.

A contact method is a way to send you notifications. For more information, see [Notifications in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications).

## Contents
<a name="API_ContactMethod_Contents"></a>

 ** arn **   <a name="Lightsail-Type-ContactMethod-arn"></a>
The Amazon Resource Name (ARN) of the contact method.
Type: String
Pattern: `.*\S.*`
Required: No

 ** contactEndpoint **   <a name="Lightsail-Type-ContactMethod-contactEndpoint"></a>
The destination of the contact method, such as an email address or a mobile phone number.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-ContactMethod-createdAt"></a>
The timestamp when the contact method was created.
Type: Timestamp
Required: No

 ** location **   <a name="Lightsail-Type-ContactMethod-location"></a>
An object that describes the location of the contact method, such as the AWS Region and Availability Zone.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-ContactMethod-name"></a>
The name of the contact method.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** protocol **   <a name="Lightsail-Type-ContactMethod-protocol"></a>
The protocol of the contact method, such as email or SMS (text messaging).
Type: String
Valid Values: `Email | SMS`
Required: No

 ** resourceType **   <a name="Lightsail-Type-ContactMethod-resourceType"></a>
The Lightsail resource type of the contact method.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** status **   <a name="Lightsail-Type-ContactMethod-status"></a>
The current status of the contact method.
A contact method has the following possible status:
+  `PendingVerification` - The contact method has not yet been verified, and the verification has not yet expired.
+  `Valid` - The contact method has been verified.
+  `InValid` - An attempt was made to verify the contact method, but the verification has expired.
Type: String
Valid Values: `PendingVerification | Valid | Invalid`
Required: No

 ** supportCode **   <a name="Lightsail-Type-ContactMethod-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail contact method. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-ContactMethod-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ContactMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContactMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContactMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContactMethod)
