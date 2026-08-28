---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Organizations::Policy
<a name="aws-resource-organizations-policy"></a>

Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.

For more information about policies and their use, see [Managing AWS Organizations policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

If the request includes tags, then the requester must have the `organizations:TagResource` permission.

This operation can be called only from the organization's management account or a member account designated as a delegated administrator.

**Note**
Before you can create a policy of a given type, you must first [enable that policy type](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html) in your organization.

## Syntax
<a name="aws-resource-organizations-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-organizations-policy-syntax.json"></a>

```
{
  "Type" : "AWS::Organizations::Policy",
  "Properties" : {
      "[Content](#cfn-organizations-policy-content)" : {{Json}},
      "[Description](#cfn-organizations-policy-description)" : {{String}},
      "[Name](#cfn-organizations-policy-name)" : {{String}},
      "[Tags](#cfn-organizations-policy-tags)" : {{[ Tag, ... ]}},
      "[TargetIds](#cfn-organizations-policy-targetids)" : {{[ String, ... ]}},
      "[Type](#cfn-organizations-policy-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-organizations-policy-syntax.yaml"></a>

```
Type: AWS::Organizations::Policy
Properties:
  [Content](#cfn-organizations-policy-content): {{Json}}
  [Description](#cfn-organizations-policy-description): {{String}}
  [Name](#cfn-organizations-policy-name): {{String}}
  [Tags](#cfn-organizations-policy-tags): {{
    - Tag}}
  [TargetIds](#cfn-organizations-policy-targetids): {{
    - String}}
  [Type](#cfn-organizations-policy-type): {{String}}
```

## Properties
<a name="aws-resource-organizations-policy-properties"></a>

`Content`  <a name="cfn-organizations-policy-content"></a>
The policy text content. You can specify the policy content as a JSON object or a JSON string.
When you specify the policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the policy content as a JSON object instead.
The text that you supply must adhere to the rules of the policy type you specify in the `Type` parameter. The following AWS Organizations quotas are enforced for the maximum size of a policy document:
+ Service control policies: 5,120 characters
+ Resource control policies: 5,120 characters
+ Declarative policies: 10,000 characters
+ Backup policies: 10,000 characters
+ Tag policies: 10,000 characters
+ Chat applications policies: 10,000 characters
+ AI services opt-out policies: 2,500 characters
+ Security Hub policies: 10,000 characters
+ Amazon Inspector policies: 10,000 characters
+ Amazon Bedrock policies: 10,000 characters
+ Upgrade rollout policies: 10,000 characters
For more information about Organizations service quotas, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the *AWS Organizations User Guide*.
*Required*: Yes
*Type*: Json
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-organizations-policy-description"></a>
Human readable description of the policy.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-organizations-policy-name"></a>
Name of the policy.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-organizations-policy-tags"></a>
A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to `null`. For more information about tagging, see [Tagging AWS Organizations resources](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html) in the AWS Organizations User Guide.
If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created.
*Required*: No
*Type*: Array of [Tag](aws-properties-organizations-policy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIds`  <a name="cfn-organizations-policy-targetids"></a>
List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html), [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html), or [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html) operations. If you don't specify this parameter, the policy is created but not attached to any organization resource.
The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string requires one of the following:
+ **Root** - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
+ **Account** - A string that consists of exactly 12 digits.
+ **Organizational unit (OU)** - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
*Required*: No
*Type*: Array of String
*Pattern*: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-organizations-policy-type"></a>
The type of policy to create.
*Required*: Yes
*Type*: String
*Allowed values*: `AISERVICES_OPT_OUT_POLICY | BACKUP_POLICY | BEDROCK_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | INSPECTOR_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY | RESOURCE_CONTROL_POLICY | S3_POLICY | SECURITYHUB_POLICY | SERVICE_CONTROL_POLICY | TAG_POLICY | UPGRADE_ROLLOUT_POLICY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-organizations-policy-return-values"></a>

### Ref
<a name="aws-resource-organizations-policy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Id`. For example: `p-examplepolicyid111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-organizations-policy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-organizations-policy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the policy. For example: `arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111`.

`AwsManaged`  <a name="AwsManaged-fn::getatt"></a>
Returns a boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it. For example: `true | false`.

`Id`  <a name="Id-fn::getatt"></a>
Returns the unique identifier (ID) of the policy. For example: `p-examplepolicyid111`.

## Examples
<a name="aws-resource-organizations-policy--examples"></a>

**Topics**
+ [Organization Policy Content Specified as a JSON Object](#aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_Object)
+ [Organization Policy Content Specified as a JSON String](#aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_String)

### Organization Policy Content Specified as a JSON Object
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_Object"></a>

This example illustrates how to specify the organization policy content as a JSON object in `AWS::Organizations::Policy`. The organization policy is specified inline as a JSON object in the `Content` property of `AWS::Organizations::Policy`.

#### JSON
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_Object--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "PolicyTestTemplate": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Policy",
      "Properties": {
        "Type": "SERVICE_CONTROL_POLICY",
        "Name": "SCPDenyLeaveOrganization",
        "Content": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "SCPDenyLeaveOrganization",
              "Effect": "Deny",
              "Action": [
                "organizations:LeaveOrganization"
              ],
              "Resource": "*"
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_Object--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content:
        Version: 2012-10-17
        Statement:
          - Sid: SCPDenyLeaveOrganization
            Effect: Deny
            Action:
              - 'organizations:LeaveOrganization'
            Resource: '*'
```

### Organization Policy Content Specified as a JSON String
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_String"></a>

This example illustrates how to specify the organization policy content as a JSON string in `AWS::Organizations::Policy`. The organization policy is specified inline as a JSON string in the `Content` property of `AWS::Organizations::Policy`.

#### JSON
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_String--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "PolicyTestTemplate": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Policy",
      "Properties": {
        "Type": "SERVICE_CONTROL_POLICY",
        "Name": "SCPDenyLeaveOrganization",
        "Content": "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"SCPDenyLeaveOrganization\",\"Effect\":\"Deny\",\"Action\":[\"organizations:LeaveOrganization\"],\"Resource\":\"*\"}]}"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_String--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content: >-
        {"Version":"2012-10-17",		 	 	 "Statement":[{"Sid":"SCPDenyLeaveOrganization","Effect":"Deny","Action":["organizations:LeaveOrganization"],"Resource":"*"}]}
```

#### YAML
<a name="aws-resource-organizations-policy--examples--Organization_Policy_Content_Specified_as_a_JSON_String--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content: >-
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "SCPDenyLeaveOrganization",
              "Effect": "Deny",
              "Action": [
                "organizations:LeaveOrganization"
              ],
              "Resource": "*"
            }
          ]
        }
```

## See also
<a name="aws-resource-organizations-policy--seealso"></a>
+ [Managing AWS Organizations policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) in the *AWS Organizations User Guide*.
+ [CreatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreatePolicy.html) in the *AWS Organizations API Reference Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
