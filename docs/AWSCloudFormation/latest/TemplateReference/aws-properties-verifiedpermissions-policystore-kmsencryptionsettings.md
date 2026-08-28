---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-kmsencryptionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore KmsEncryptionSettings
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionsettings"></a>

A structure that contains the KMS encryption configuration for the policy store. The encryption settings determine what customer-managed KMS key will be used to encrypt all resources within the policy store, and any user-defined context key-value pairs to append during encryption processes.

This data type is used as a field that is part of the [EncryptionSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionSettings.html) type.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionsettings-syntax.json"></a>

```
{
  "[EncryptionContext](#cfn-verifiedpermissions-policystore-kmsencryptionsettings-encryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Key](#cfn-verifiedpermissions-policystore-kmsencryptionsettings-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionsettings-syntax.yaml"></a>

```
  [EncryptionContext](#cfn-verifiedpermissions-policystore-kmsencryptionsettings-encryptioncontext): {{
    {{Key}}: {{Value}}}}
  [Key](#cfn-verifiedpermissions-policystore-kmsencryptionsettings-key): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionsettings-properties"></a>

`EncryptionContext`  <a name="cfn-verifiedpermissions-policystore-kmsencryptionsettings-encryptioncontext"></a>
User-defined, additional context to be added to encryption processes.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-verifiedpermissions-policystore-kmsencryptionsettings-key"></a>
The customer-managed KMS key [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html), alias or ID to be used for encryption processes.
Users can provide the full KMS key ARN, a KMS key alias, or a KMS key ID, but it will be mapped to the full KMS key ARN after policy store creation, and referenced when encrypting child resources.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
