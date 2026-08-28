---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-encryptionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore EncryptionSettings
<a name="aws-properties-verifiedpermissions-policystore-encryptionsettings"></a>

A structure that contains the encryption configuration for the policy store and child resources.

This data type is used as a request parameter in the [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html) operation.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-encryptionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-encryptionsettings-syntax.json"></a>

```
{
  "[Default](#cfn-verifiedpermissions-policystore-encryptionsettings-default)" : {{Json}},
  "[KmsEncryptionSettings](#cfn-verifiedpermissions-policystore-encryptionsettings-kmsencryptionsettings)" : {{KmsEncryptionSettings}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-encryptionsettings-syntax.yaml"></a>

```
  [Default](#cfn-verifiedpermissions-policystore-encryptionsettings-default): {{Json}}
  [KmsEncryptionSettings](#cfn-verifiedpermissions-policystore-encryptionsettings-kmsencryptionsettings): {{
    KmsEncryptionSettings}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-encryptionsettings-properties"></a>

`Default`  <a name="cfn-verifiedpermissions-policystore-encryptionsettings-default"></a>
This is the default encryption setting. The policy store uses an AWS owned key for encrypting data.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsEncryptionSettings`  <a name="cfn-verifiedpermissions-policystore-encryptionsettings-kmsencryptionsettings"></a>
The AWS KMS encryption settings for this policy store to encrypt data with. It will contain the customer-managed KMS key, and a user-defined encryption context.
*Required*: No
*Type*: [KmsEncryptionSettings](aws-properties-verifiedpermissions-policystore-kmsencryptionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
