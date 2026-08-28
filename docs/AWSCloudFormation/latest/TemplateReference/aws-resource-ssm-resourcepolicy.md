---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::ResourcePolicy
<a name="aws-resource-ssm-resourcepolicy"></a>

Creates or updates a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an AWS account) that can manage your Systems Manager resources. Currently, `OpsItemGroup` is the only resource that supports Systems Manager resource policies. The resource policy for `OpsItemGroup` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems). OpsCenter is a tool in Systems Manager.

## Syntax
<a name="aws-resource-ssm-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::ResourcePolicy",
  "Properties" : {
      "[Policy](#cfn-ssm-resourcepolicy-policy)" : {{Json}},
      "[ResourceArn](#cfn-ssm-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssm-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::SSM::ResourcePolicy
Properties:
  [Policy](#cfn-ssm-resourcepolicy-policy): {{Json}}
  [ResourceArn](#cfn-ssm-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-ssm-resourcepolicy-properties"></a>

`Policy`  <a name="cfn-ssm-resourcepolicy-policy"></a>
A policy you want to associate with a resource.
*Required*: Yes
*Type*: Json
*Pattern*: `^(?!\s*$).+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-ssm-resourcepolicy-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource to which you want to attach a policy.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ssm-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-ssm-resourcepolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-resourcepolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssm-resourcepolicy-return-values-fn--getatt-fn--getatt"></a>

`PolicyHash`  <a name="PolicyHash-fn::getatt"></a>
ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash and the policy ID when updating or deleting a policy.

`PolicyId`  <a name="PolicyId-fn::getatt"></a>
ID of the current policy version.

## Examples
<a name="aws-resource-ssm-resourcepolicy--examples"></a>

### Create a resource policy for OpsCenter
<a name="aws-resource-ssm-resourcepolicy--examples--Create_a_resource_policy_for_OpsCenter"></a>

The following example specifies the management or delegated administrator account IDs for working with OpsItems across accounts.

#### YAML
<a name="aws-resource-ssm-resourcepolicy--examples--Create_a_resource_policy_for_OpsCenter--yaml"></a>

```
---
AWSTemplateFormatVersion: '2010-09-09'
Description: Creates resources needed for a member account to work with OpsCenter OpsItems across multiple accounts.

Parameters:
  AdminAccountIds:
    Description: Allows one or more accounts to access OpsItems. Specify AWS Organizations management account IDs
                 and delegated administrator account IDs in a comma-separated list.
    Type: CommaDelimitedList
  ParentDeploymentRegion:
    Description: Primary AWS Region used for creating global resources such as IAM roles.
    Type: String

Conditions:
  IsParentDeploymentRegion:
    Fn::Equals:
    - !Ref 'AWS::Region'
    - !Ref ParentDeploymentRegion

Resources:
  OpsItemCrossAccountResourcePolicy:
    Type: AWS::SSM::ResourcePolicy
    Properties:
      Policy: !Sub
        - '{"Version":"2012-10-17",		 	 	 "Statement":[{"Sid":"AllowAdminAccountsToAccessOpsItems2","Effect":"Allow","Principal":{"AWS":["${AdminAccountIdsString}"]},"Action":["ssm:CreateOpsItem","ssm:AddTagsToResource","ssm:GetOpsItem","ssm:UpdateOpsItem"],"Resource":["arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:opsitem/*","arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:opsitemgroup/default"]}]}'
        - AdminAccountIdsString:
            Fn::Join:
            - '\",\"'
            - !Ref AdminAccountIds
      ResourceArn:
        Fn::Sub: arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:opsitemgroup/default

  OpsItemCrossAccountExecutionRole:
    Type: AWS::IAM::Role
    Condition: IsParentDeploymentRegion
    Properties:
      RoleName: OpsItem-CrossAccountExecutionRole
      Description: 'Role used by the management account or delegated administrator to remediate OpsItems'
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Principal:
              AWS: !Ref AdminAccountIds
            Condition:
              StringLike:
                "aws:PrincipalArn": !Split
                  - ','
                  - !Sub
                    - 'arn:*:iam::${inner}:role/OpsItem-*Role*'
                    - inner: !Join
                        - ':role/OpsItem-*Role*,arn:*:iam::'
                        - Ref: AdminAccountIds
            Action:
              - sts:AssumeRole
      Path: '/'
      ManagedPolicyArns:
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/ReadOnlyAccess'
```

## See also
<a name="aws-resource-ssm-resourcepolicy--seealso"></a>
+  [Setting up OpsCenter to work with OpsItems across accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
