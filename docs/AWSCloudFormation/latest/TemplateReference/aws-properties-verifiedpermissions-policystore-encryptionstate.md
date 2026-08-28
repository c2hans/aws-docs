---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-encryptionstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore EncryptionState
<a name="aws-properties-verifiedpermissions-policystore-encryptionstate"></a>

A structure that contains the encryption configuration for the policy store and child resources.

This data type is used as a response parameter field for the [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html) operation.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-encryptionstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-encryptionstate-syntax.json"></a>

```
{
  "[Default](#cfn-verifiedpermissions-policystore-encryptionstate-default)" : {{Json}},
  "[KmsEncryptionState](#cfn-verifiedpermissions-policystore-encryptionstate-kmsencryptionstate)" : {{KmsEncryptionState}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-encryptionstate-syntax.yaml"></a>

```
  [Default](#cfn-verifiedpermissions-policystore-encryptionstate-default): {{Json}}
  [KmsEncryptionState](#cfn-verifiedpermissions-policystore-encryptionstate-kmsencryptionstate): {{
    KmsEncryptionState}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-encryptionstate-properties"></a>

`Default`  <a name="cfn-verifiedpermissions-policystore-encryptionstate-default"></a>
This is the default encryption state. The policy store is encrypted using an AWS owned key.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsEncryptionState`  <a name="cfn-verifiedpermissions-policystore-encryptionstate-kmsencryptionstate"></a>
The AWS KMS encryption settings currently configured for this policy store to encrypt data with. It contains the customer-managed KMS key, and a user-defined encryption context.
*Required*: No
*Type*: [KmsEncryptionState](aws-properties-verifiedpermissions-policystore-kmsencryptionstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
