---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-grouppolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::GroupPolicy
<a name="aws-resource-iam-grouppolicy"></a>

Adds or updates an inline policy document that is embedded in the specified IAM group.

A group can also have managed policies attached to it. To attach a managed policy to a group, use [`AWS::IAM::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html). To create a new managed policy, use [`AWS::IAM::ManagedPolicy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

For information about the maximum number of inline policies that you can embed in a group, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.

## Syntax
<a name="aws-resource-iam-grouppolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iam-grouppolicy-syntax.json"></a>

```
{
  "Type" : "AWS::IAM::GroupPolicy",
  "Properties" : {
      "[GroupName](#cfn-iam-grouppolicy-groupname)" : {{String}},
      "[PolicyDocument](#cfn-iam-grouppolicy-policydocument)" : {{Json}},
      "[PolicyName](#cfn-iam-grouppolicy-policyname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iam-grouppolicy-syntax.yaml"></a>

```
Type: AWS::IAM::GroupPolicy
Properties:
  [GroupName](#cfn-iam-grouppolicy-groupname): {{String}}
  [PolicyDocument](#cfn-iam-grouppolicy-policydocument): {{Json}}
  [PolicyName](#cfn-iam-grouppolicy-policyname): {{String}}
```

## Properties
<a name="aws-resource-iam-grouppolicy-properties"></a>

`GroupName`  <a name="cfn-iam-grouppolicy-groupname"></a>
The name of the group to associate the policy with.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-.
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-iam-grouppolicy-policydocument"></a>
The policy document.
You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
*Required*: No
*Type*: Json
*Pattern*: `[\u0009\u000A\u000D\u0020-\u00FF]+`
*Minimum*: `1`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-iam-grouppolicy-policyname"></a>
The name of the policy document.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iam-grouppolicy-return-values"></a>

### Ref
<a name="aws-resource-iam-grouppolicy-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-iam-grouppolicy--examples"></a>

**Topics**
+ [Group embedded inline policy document](#aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document)
+ [Group embedded inline policy document with Ref function](#aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document_with_Ref_function)

### Group embedded inline policy document
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document"></a>

This example shows an inline policy document in `AWS::IAM::GroupPolicy`. The policy will be embedded in the specified IAM user group, `CFNUserGroup`.

#### JSON
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document--json"></a>

```
{
    "Type": "AWS::IAM::GroupPolicy",
    "Properties": {
        "PolicyName": "CFNUsers",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "cloudformation:Describe*",
                        "cloudformation:List*",
                        "cloudformation:Get*"
                    ],
                    "Resource": "*"
                }
            ]
        },
        "GroupName": "CFNUserGroup"
    }
}
```

#### YAML
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document--yaml"></a>

```
Type: 'AWS::IAM::GroupPolicy'
Properties:
  PolicyName: CFNUsers
  PolicyDocument:
    Version: "2012-10-17"
    Statement:
      - Effect: Allow
        Action:
          - 'cloudformation:Describe*'
          - 'cloudformation:List*'
          - 'cloudformation:Get*'
        Resource: '*'
  GroupName: CFNUserGroup
```

### Group embedded inline policy document with Ref function
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document_with_Ref_function"></a>

This example shows an inline policy document in `AWS::IAM::GroupPolicy`. The example uses the `Ref` function in the `GroupName` property to specify the logical ID of a `AWS::IAM::Group` resource. For the logical ID of the `AWS::IAM::Group` resource, `Ref` returns the role name.

#### JSON
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document_with_Ref_function--json"></a>

```
{
    "Type": "AWS::IAM::GroupPolicy",
    "Properties": {
        "PolicyName": "CFNUsers",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "cloudformation:Describe*",
                        "cloudformation:List*",
                        "cloudformation:Get*"
                    ],
                    "Resource": "*"
                }
            ]
        },
        "GroupName": {
            "Ref": "CFNUserGroup"
        }
    }
}
```

#### YAML
<a name="aws-resource-iam-grouppolicy--examples--Group_embedded_inline_policy_document_with_Ref_function--yaml"></a>

```
Type: 'AWS::IAM::GroupPolicy'
Properties:
  PolicyName: CFNUsers
  PolicyDocument:
    Version: "2012-10-17"
    Statement:
      - Effect: Allow
        Action:
          - 'cloudformation:Describe*'
          - 'cloudformation:List*'
          - 'cloudformation:Get*'
        Resource: '*'
  GroupName: !Ref CFNUserGroup
```

## See also
<a name="aws-resource-iam-grouppolicy--seealso"></a>
+ [PutGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutGroupPolicy.html) in the *AWS Identity and Access Management API Reference*
+  [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html)
