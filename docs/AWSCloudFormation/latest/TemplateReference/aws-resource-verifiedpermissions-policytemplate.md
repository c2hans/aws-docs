---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policytemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyTemplate
<a name="aws-resource-verifiedpermissions-policytemplate"></a>

Creates a policy template. A template can use placeholders for the principal and resource. A template must be instantiated into a policy by associating it with specific principals and resources to use for the placeholders. That instantiated policy can then be considered in authorization decisions. The instantiated policy works identically to any other policy, except that it is dynamically linked to the template. If the template changes, then any policies that are linked to that template are immediately updated as well.

## Syntax
<a name="aws-resource-verifiedpermissions-policytemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-verifiedpermissions-policytemplate-syntax.json"></a>

```
{
  "Type" : "AWS::VerifiedPermissions::PolicyTemplate",
  "Properties" : {
      "[Description](#cfn-verifiedpermissions-policytemplate-description)" : {{String}},
      "[Name](#cfn-verifiedpermissions-policytemplate-name)" : {{String}},
      "[PolicyStoreId](#cfn-verifiedpermissions-policytemplate-policystoreid)" : {{String}},
      "[Statement](#cfn-verifiedpermissions-policytemplate-statement)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-verifiedpermissions-policytemplate-syntax.yaml"></a>

```
Type: AWS::VerifiedPermissions::PolicyTemplate
Properties:
  [Description](#cfn-verifiedpermissions-policytemplate-description): {{String}}
  [Name](#cfn-verifiedpermissions-policytemplate-name): {{String}}
  [PolicyStoreId](#cfn-verifiedpermissions-policytemplate-policystoreid): {{String}}
  [Statement](#cfn-verifiedpermissions-policytemplate-statement): {{String}}
```

## Properties
<a name="aws-resource-verifiedpermissions-policytemplate-properties"></a>

`Description`  <a name="cfn-verifiedpermissions-policytemplate-description"></a>
The description to attach to the new or updated policy template.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-verifiedpermissions-policytemplate-name"></a>
The name of the policy template, if one was assigned when the policy template was created or last updated.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-/_]*$`
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyStoreId`  <a name="cfn-verifiedpermissions-policytemplate-policystoreid"></a>
The unique identifier of the policy store that contains the template.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Statement`  <a name="cfn-verifiedpermissions-policytemplate-statement"></a>
Specifies the content that you want to use for the new policy template, written in the Cedar policy language.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-verifiedpermissions-policytemplate-return-values"></a>

### Ref
<a name="aws-resource-verifiedpermissions-policytemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique id of the policy store followed by '\|' and the unique id of the new or updated policy template. For example:

 `{ "Ref": "POLICYSTOREabcde111111|POLICYTEMPLATEab111111" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-verifiedpermissions-policytemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-verifiedpermissions-policytemplate-return-values-fn--getatt-fn--getatt"></a>

`PolicyTemplateId`  <a name="PolicyTemplateId-fn::getatt"></a>
The unique identifier of the new or modified policy template.

## Examples
<a name="aws-resource-verifiedpermissions-policytemplate--examples"></a>

### Creating a policy template
<a name="aws-resource-verifiedpermissions-policytemplate--examples--Creating_a_policy_template"></a>

The following example creates a policy template with the specified statement.

#### JSON
<a name="aws-resource-verifiedpermissions-policytemplate--examples--Creating_a_policy_template--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation sample template for creating a policy template for Verified Permissions.",
    "Parameters": {
        "PolicyStoreId": {
            "Type": "String"
        },
        "Description": {
            "Type": "String"
        },
        "Statement": {
            "Type": "String"
        }
    },
    "Resources": {
        "PolicyTemplate": {
            "Type": "AWS::VerifiedPermissions::PolicyTemplate",
            "Properties": {
                "PolicyStoreId": {
                    "Ref": "PolicyStoreId"
                },
                "Description": {
                    "Ref": "Description"
                },
                "Statement": {
                    "Ref": "Statement"
                }
            }
        }
    },
    "Outputs": {
        "PolicyTemplateId": {
            "Value": {
                "Fn::GetAtt": [
                    "PolicyTemplate",
                    "PolicyTemplateId"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-verifiedpermissions-policytemplate--examples--Creating_a_policy_template--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  Description": "AWS CloudFormation sample template for creating a policy template for Verified Permissions."
Parameters:
  PolicyStoreId:
    Type: String
  Description:
    Type: String
  Statement:
    Type: String
Resources:
  PolicyTemplate:
    Type: AWS::VerifiedPermissions::PolicyTemplate
    Properties:
      PolicyStoreId: !Ref PolicyStoreId
      Description: !Ref Description
      Statement: !Ref Statement
Outputs:
  PolicyTemplateId:
    Value: !GetAtt PolicyTemplate.PolicyTemplateId
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
