---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-schemadefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore SchemaDefinition
<a name="aws-properties-verifiedpermissions-policystore-schemadefinition"></a>

Contains a list of principal types, resource types, and actions that can be specified in policies stored in the same policy store. If the validation mode for the policy store is set to `STRICT`, then policies that can't be validated by this schema are rejected by Verified Permissions and can't be stored in the policy store.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-schemadefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-schemadefinition-syntax.json"></a>

```
{
  "[CedarJson](#cfn-verifiedpermissions-policystore-schemadefinition-cedarjson)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-schemadefinition-syntax.yaml"></a>

```
  [CedarJson](#cfn-verifiedpermissions-policystore-schemadefinition-cedarjson): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-schemadefinition-properties"></a>

`CedarJson`  <a name="cfn-verifiedpermissions-policystore-schemadefinition-cedarjson"></a>
A JSON string representation of the schema supported by applications that use this policy store. For more information, see [Policy store schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html) in the AVP User Guide.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
