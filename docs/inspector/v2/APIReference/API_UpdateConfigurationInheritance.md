---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfigurationInheritance.html
---

# UpdateConfigurationInheritance
<a name="API_UpdateConfigurationInheritance"></a>

The per-scan-type inheritance reset settings for the `UpdateConfiguration` operation. Each member is independently optional. Including a member in this structure resets that scan type's configuration to inherit from the delegated administrator.

## Contents
<a name="API_UpdateConfigurationInheritance_Contents"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
