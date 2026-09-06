---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iam-user-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::User Policy
<a name="aws-properties-iam-user-policy"></a>

Contains information about an attached policy.

An attached policy is a managed policy that has been attached to a user, group, or role.

For more information about managed policies, refer to [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

## Syntax
<a name="aws-properties-iam-user-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iam-user-policy-syntax.json"></a>

```
{
  "[PolicyDocument](#cfn-iam-user-policy-policydocument)" : {{Json}},
  "[PolicyName](#cfn-iam-user-policy-policyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iam-user-policy-syntax.yaml"></a>

```
  [PolicyDocument](#cfn-iam-user-policy-policydocument): {{Json}}
  [PolicyName](#cfn-iam-user-policy-policyname): {{String}}
```

## Properties
<a name="aws-properties-iam-user-policy-properties"></a>

`PolicyDocument`  <a name="cfn-iam-user-policy-policydocument"></a>
The entire contents of the policy that defines permissions. For more information, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-iam-user-policy-policyname"></a>
The friendly name (not ARN) identifying the policy.
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-iam-user-policy--examples"></a>

### IAM User Policy
<a name="aws-properties-iam-user-policy--examples--IAM_User_Policy"></a>

This example shows how the policy document is declared.

#### JSON
<a name="aws-properties-iam-user-policy--examples--IAM_User_Policy--json"></a>

```
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```

#### YAML
<a name="aws-properties-iam-user-policy--examples--IAM_User_Policy--yaml"></a>

```
PolicyName: root
PolicyDocument:
   Version: 2012-10-17
   Statement:
      - Sid: IamListAccess
        Effect: Allow
        Action:
         - 'iam:ListRoles'
         - 'iam:ListUsers'
        Resource: '*'
```

## See also
<a name="aws-properties-iam-user-policy--seealso"></a>
+ [PolicyDetail](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyDetail.html) in the *AWS Identity and Access Management API Reference*
