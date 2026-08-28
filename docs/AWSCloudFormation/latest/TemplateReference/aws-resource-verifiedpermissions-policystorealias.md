---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policystorealias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStoreAlias
<a name="aws-resource-verifiedpermissions-policystorealias"></a>

Creates a policy store alias for the specified policy store. A policy store alias is an alternative identifier that you can use to reference a policy store in API operations.

This operation is idempotent. If multiple CreatePolicyStoreAlias requests are made where the `aliasName` and `policyStoreId` fields are the same between the requests, subsequent requests will be ignored. For each duplicate CreatePolicyStoreAlias request, a Success response will be returned and a new policy store alias will not be created.

**Note**
Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) *. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

## Syntax
<a name="aws-resource-verifiedpermissions-policystorealias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-verifiedpermissions-policystorealias-syntax.json"></a>

```
{
  "Type" : "AWS::VerifiedPermissions::PolicyStoreAlias",
  "Properties" : {
      "[AliasName](#cfn-verifiedpermissions-policystorealias-aliasname)" : {{String}},
      "[PolicyStoreId](#cfn-verifiedpermissions-policystorealias-policystoreid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-verifiedpermissions-policystorealias-syntax.yaml"></a>

```
Type: AWS::VerifiedPermissions::PolicyStoreAlias
Properties:
  [AliasName](#cfn-verifiedpermissions-policystorealias-aliasname): {{String}}
  [PolicyStoreId](#cfn-verifiedpermissions-policystorealias-policystoreid): {{String}}
```

## Properties
<a name="aws-resource-verifiedpermissions-policystorealias-properties"></a>

`AliasName`  <a name="cfn-verifiedpermissions-policystorealias-aliasname"></a>
The name of the policy store alias.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_/]*$`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyStoreId`  <a name="cfn-verifiedpermissions-policystorealias-policystoreid"></a>
The ID of the policy store associated with the alias.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-verifiedpermissions-policystorealias-return-values"></a>

### Ref
<a name="aws-resource-verifiedpermissions-policystorealias-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
