---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfigurationInheritance.html
---

# UpdateConfigurationInheritance

The per-scan-type inheritance reset settings for the `UpdateConfiguration` operation. Each member is independently optional. Including a member in this structure resets that scan type's configuration to inherit from the delegated administrator.

## Contents
<a name="API_UpdateConfigurationInheritance_Contents"></a>

 ** amiConfiguration **   <a name="inspector2-Type-UpdateConfigurationInheritance-amiConfiguration"></a>
The inheritance behavior for a scan-type configuration. Used with `UpdateConfigurationInheritance` to reset a member account's configuration to inherit from the delegated administrator. The only valid value is `INHERIT_FROM_ADMIN`, which resets the member account's configuration so that it inherits scan settings from the delegated administrator.
Type: String
Valid Values: `INHERIT_FROM_ADMIN`
Required: No

 ** ec2Configuration **   <a name="inspector2-Type-UpdateConfigurationInheritance-ec2Configuration"></a>
The inheritance mode for Amazon EC2 scan configuration. Set to `INHERIT_FROM_ADMIN` to reset the member account's Amazon EC2 scan configuration to inherit from the delegated administrator. If omitted, the member account's existing Amazon EC2 scan configuration is not changed.
Type: String
Valid Values: `INHERIT_FROM_ADMIN`
Required: No

 ** ecrConfiguration **   <a name="inspector2-Type-UpdateConfigurationInheritance-ecrConfiguration"></a>
The inheritance mode for Amazon ECR scan configuration. Set to `INHERIT_FROM_ADMIN` to reset the member account's Amazon ECR scan configuration to inherit from the delegated administrator. If omitted, the member account's existing Amazon ECR scan configuration is not changed.
Type: String
Valid Values: `INHERIT_FROM_ADMIN`
Required: No

## See Also
<a name="API_UpdateConfigurationInheritance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateConfigurationInheritance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateConfigurationInheritance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateConfigurationInheritance)
