---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-kmsencryptionstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore KmsEncryptionState
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionstate"></a>

A structure that contains the AWS KMS encryption configuration for the policy store. The encryption state shows what customer-managed KMS key is being used to encrypt all resources within the policy store, and any user-defined context key-value pairs added during encryption processes.

This data type is used as a field that is part of the [EncryptionState](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionState.html) type.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionstate-syntax.json"></a>

```
{
  "[EncryptionContext](#cfn-verifiedpermissions-policystore-kmsencryptionstate-encryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Key](#cfn-verifiedpermissions-policystore-kmsencryptionstate-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionstate-syntax.yaml"></a>

```
  [EncryptionContext](#cfn-verifiedpermissions-policystore-kmsencryptionstate-encryptioncontext): {{
    {{Key}}: {{Value}}}}
  [Key](#cfn-verifiedpermissions-policystore-kmsencryptionstate-key): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-kmsencryptionstate-properties"></a>

`EncryptionContext`  <a name="cfn-verifiedpermissions-policystore-kmsencryptionstate-encryptioncontext"></a>
User-defined, additional context added to encryption processes.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-verifiedpermissions-policystore-kmsencryptionstate-key"></a>
The customer-managed KMS key [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) being used for encryption processes.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
