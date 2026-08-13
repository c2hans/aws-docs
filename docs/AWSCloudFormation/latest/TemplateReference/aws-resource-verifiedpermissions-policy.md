---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::Policy
<a name="aws-resource-verifiedpermissions-policy"></a>

Creates or updates a Cedar policy and saves it in the specified policy store. You can create either a static policy or a policy linked to a policy template.

You can directly update only static policies. To update a template-linked policy, you must update its linked policy template instead.
+ To create a static policy, in the `Definition` include a `Static` element that includes the Cedar policy text in the `Statement` element.
+ To create a policy that is dynamically linked to a policy template, in the `Definition` include a `Templatelinked` element that specifies the policy template ID and the principal and resource to associate with this policy. If the policy template is ever updated, any policies linked to the policy template automatically use the updated template.

**Note**
If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesn't pass validation, the operation fails and the update isn't stored.
When you edit a static policy, You can change only certain elements of a static policy:
The action referenced by the policy.
A condition clause, such as when and unless.
You can't change these elements of a static policy:
Changing a policy from a static policy to a template-linked policy.
Changing the effect of a static policy from permit or forbid.
The principal referenced by a static policy.
The resource referenced by a static policy.
To update a template-linked policy, you must update the template instead.

## Syntax
<a name="aws-resource-verifiedpermissions-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-verifiedpermissions-policy-syntax.json"></a>

```
{
  "Type" : "AWS::VerifiedPermissions::Policy",
  "Properties" : {
      "[Definition](#cfn-verifiedpermissions-policy-definition)" : {{PolicyDefinition}},
      "[Name](#cfn-verifiedpermissions-policy-name)" : {{String}},
      "[PolicyStoreId](#cfn-verifiedpermissions-policy-policystoreid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-verifiedpermissions-policy-syntax.yaml"></a>

```
Type: AWS::VerifiedPermissions::Policy
Properties:
  [Definition](#cfn-verifiedpermissions-policy-definition): {{
    PolicyDefinition}}
  [Name](#cfn-verifiedpermissions-policy-name): {{String}}
  [PolicyStoreId](#cfn-verifiedpermissions-policy-policystoreid): {{String}}
```

## Properties
<a name="aws-resource-verifiedpermissions-policy-properties"></a>

`Definition`  <a name="cfn-verifiedpermissions-policy-definition"></a>
Specifies the policy type and content to use for the new or updated policy. The definition structure must include either a `Static` or a `TemplateLinked` element.
*Required*: Yes
*Type*: [PolicyDefinition](aws-properties-verifiedpermissions-policy-policydefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-verifiedpermissions-policy-name"></a>
The name of the policy, if one was assigned when the policy was created or last updated.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-/_]*$`
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyStoreId`  <a name="cfn-verifiedpermissions-policy-policystoreid"></a>
Specifies the `PolicyStoreId` of the policy store you want to store the policy in.
To specify a policy store, use its ID or alias name. When using an alias name, prefix it with `policy-store-alias/`. For example:
+ ID: `PSEXAMPLEabcdefg111111`
+ Alias name: `policy-store-alias/example-policy-store`
To view aliases, use [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-verifiedpermissions-policy-return-values"></a>

### Ref
<a name="aws-resource-verifiedpermissions-policy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique id of the new or updated policy. For example:

 `{ "Ref": "SPEXAMPLEabcdefg111111" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-verifiedpermissions-policy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-verifiedpermissions-policy-return-values-fn--getatt-fn--getatt"></a>

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
The unique ID of the new or updated policy.

`PolicyType`  <a name="PolicyType-fn::getatt"></a>
The type of the policy. This is one of the following values:
+ Static
+ TemplateLinked

## Examples
<a name="aws-resource-verifiedpermissions-policy--examples"></a>

**Topics**
+ [Creating a static policy](#aws-resource-verifiedpermissions-policy--examples--Creating_a_static_policy)
+ [Creating a template-linked policy](#aws-resource-verifiedpermissions-policy--examples--Creating_a_template-linked_policy)

### Creating a static policy
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_static_policy"></a>

The following example creates a static policy in the specified policy store with the specified policy statement.

#### JSON
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_static_policy--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation sample template for creating a static policy for Verified Permissions",
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
        "StaticPolicy": {
            "Type": "AWS::VerifiedPermissions::Policy",
            "Properties": {
                "PolicyStoreId": {
                    "Ref": "PolicyStoreId"
                },
                "Definition": {
                    "Static": {
                        "Description": {
                            "Ref": "Description"
                        },
                        "Statement": {
                            "Ref": "Statement"
                        }
                    }
                }
            }
        }
    },
    "Outputs": {
        "PolicyId": {
            "Value": {
                "Fn::GetAtt": [
                    "StaticPolicy",
                    "PolicyId"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_static_policy--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  Description": "AWS CloudFormation sample template for creating a static policy for Verified Permissions."
Parameters:
  PolicyStoreId:
    Type: String
  Description:
    Type: String
  Statement:
    Type: String
Resources:
  StaticPolicy:
    Type: AWS::VerifiedPermissions::Policy
    Properties:
      PolicyStoreId: !Ref PolicyStoreId
      Definition:
        Static:
          Description: !Ref Description
          Statement: !Ref Statement
Outputs:
  PolicyId:
    Value: !GetAtt StaticPolicy.PolicyId
```

### Creating a template-linked policy
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_template-linked_policy"></a>

The following example creates a policy that is linked to the specified policy template. You must specify the type and ID for the placeholders in your template.

#### JSON
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_template-linked_policy--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation sample template for creating a template-linked policy for Verified Permissions.",
    "Parameters": {
        "PolicyStoreId": {
            "Type": "String"
        },
        "PolicyTemplateId": {
            "Type": "String"
        },
        "PrincipalType": {
            "Type": "String"
        },
        "PrincipalId": {
            "Type": "String"
        },
        "ResourceType": {
            "Type": "String"
        },
        "ResourceId": {
            "Type": "String"
        }
    },
    "Resources": {
        "TemplateLinkedPolicy": {
            "Type": "AWS::VerifiedPermissions::Policy",
            "Properties": {
                "PolicyStoreId": {
                    "Ref": "PolicyStoreId"
                },
                "Definition": {
                    "TemplateLinked": {
                        "PolicyTemplateId": {
                            "Ref": "PolicyTemplateId"
                        },
                        "Principal": {
                            "EntityType": {
                                "Ref": "PrincipalType"
                            },
                            "EntityId": {
                                "Ref": "PrincipalId"
                            }
                        },
                        "Resource": {
                            "EntityType": {
                                "Ref": "ResourceType"
                            },
                            "EntityId": {
                                "Ref": "ResourceId"
                            }
                        }
                    }
                }
            }
        }
    },
    "Outputs": {
        "PolicyId": {
            "Value": {
                "Fn::GetAtt": [
                    "TemplateLinkedPolicy",
                    "PolicyId"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-verifiedpermissions-policy--examples--Creating_a_template-linked_policy--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  Description": "AWS CloudFormation sample template for creating a template-linked policy for Verified Permissions."
Parameters:
  PolicyStoreId:
    Type: String
  PolicyTemplateId:
    Type: String
  PrincipalType:
    Type: String
  PrincipalId:
    Type: String
  ResourceType:
    Type: String
  ResourceId:
    Type: String
Resources:
  TemplateLinkedPolicy:
    Type: AWS::VerifiedPermissions::Policy
    Properties:
      PolicyStoreId: !Ref PolicyStoreId
      Definition:
        TemplateLinked:
          PolicyTemplateId: !Ref PolicyTemplateId
          Principal:
            EntityType: !Ref PrincipalType
            EntityId: !Ref PrincipalId
          Resource:
            EntityType: !Ref ResourceType
            EntityId: !Ref ResourceId
Outputs:
  PolicyId:
    Value: !GetAtt TemplateLinkedPolicy.PolicyId
```
