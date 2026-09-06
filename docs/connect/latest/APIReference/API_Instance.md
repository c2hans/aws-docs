---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Instance.html
---

# Instance
<a name="API_Instance"></a>

The Connect Customer instance.

## Contents
<a name="API_Instance_Contents"></a>

 ** Arn **   <a name="connect-Type-Instance-Arn"></a>
The Amazon Resource Name (ARN) of the instance.
Type: String
Required: No

 ** CreatedTime **   <a name="connect-Type-Instance-CreatedTime"></a>
When the instance was created.
Type: Timestamp
Required: No

 ** Id **   <a name="connect-Type-Instance-Id"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IdentityManagementType **   <a name="connect-Type-Instance-IdentityManagementType"></a>
The identity management type.
Type: String
Valid Values: `SAML | CONNECT_MANAGED | EXISTING_DIRECTORY`
Required: No

 ** InboundCallsEnabled **   <a name="connect-Type-Instance-InboundCallsEnabled"></a>
Whether inbound calls are enabled.
Type: Boolean
Required: No

 ** InstanceAccessUrl **   <a name="connect-Type-Instance-InstanceAccessUrl"></a>
This URL allows contact center users to access the Connect Customer admin website.
Type: String
Required: No

 ** InstanceAlias **   <a name="connect-Type-Instance-InstanceAlias"></a>
The alias of instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `^(?!d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*$`
Required: No

 ** InstanceStatus **   <a name="connect-Type-Instance-InstanceStatus"></a>
The state of the instance.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED`
Required: No

 ** OutboundCallsEnabled **   <a name="connect-Type-Instance-OutboundCallsEnabled"></a>
Whether outbound calls are enabled.
Type: Boolean
Required: No

 ** ServiceRole **   <a name="connect-Type-Instance-ServiceRole"></a>
The service role of the instance.
Type: String
Required: No

 ** StatusReason **   <a name="connect-Type-Instance-StatusReason"></a>
Relevant details why the instance was not successfully created.
Type: [InstanceStatusReason](API_InstanceStatusReason.md) object
Required: No

 ** Tags **   <a name="connect-Type-Instance-Tags"></a>
The tags of an instance.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Instance)
