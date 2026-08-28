---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-verifiedaccessgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessGroup
<a name="aws-resource-ec2-verifiedaccessgroup"></a>

An AWS Verified Access group is a collection of AWS Verified Access endpoints who's associated applications have similar security requirements. Each instance within a Verified Access group shares an Verified Access policy. For example, you can group all Verified Access instances associated with "sales" applications together and use one common Verified Access policy.

## Syntax
<a name="aws-resource-ec2-verifiedaccessgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-verifiedaccessgroup-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VerifiedAccessGroup",
  "Properties" : {
      "[Description](#cfn-ec2-verifiedaccessgroup-description)" : {{String}},
      "[PolicyDocument](#cfn-ec2-verifiedaccessgroup-policydocument)" : {{String}},
      "[PolicyEnabled](#cfn-ec2-verifiedaccessgroup-policyenabled)" : {{Boolean}},
      "[SseSpecification](#cfn-ec2-verifiedaccessgroup-ssespecification)" : {{SseSpecification}},
      "[Tags](#cfn-ec2-verifiedaccessgroup-tags)" : {{[ Tag, ... ]}},
      "[VerifiedAccessInstanceId](#cfn-ec2-verifiedaccessgroup-verifiedaccessinstanceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-verifiedaccessgroup-syntax.yaml"></a>

```
Type: AWS::EC2::VerifiedAccessGroup
Properties:
  [Description](#cfn-ec2-verifiedaccessgroup-description): {{String}}
  [PolicyDocument](#cfn-ec2-verifiedaccessgroup-policydocument): {{String}}
  [PolicyEnabled](#cfn-ec2-verifiedaccessgroup-policyenabled): {{Boolean}}
  [SseSpecification](#cfn-ec2-verifiedaccessgroup-ssespecification): {{
    SseSpecification}}
  [Tags](#cfn-ec2-verifiedaccessgroup-tags): {{
    - Tag}}
  [VerifiedAccessInstanceId](#cfn-ec2-verifiedaccessgroup-verifiedaccessinstanceid): {{String}}
```

## Properties
<a name="aws-resource-ec2-verifiedaccessgroup-properties"></a>

`Description`  <a name="cfn-ec2-verifiedaccessgroup-description"></a>
A description for the AWS Verified Access group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDocument`  <a name="cfn-ec2-verifiedaccessgroup-policydocument"></a>
The Verified Access policy document.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyEnabled`  <a name="cfn-ec2-verifiedaccessgroup-policyenabled"></a>
The status of the Verified Access policy.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SseSpecification`  <a name="cfn-ec2-verifiedaccessgroup-ssespecification"></a>
 The options for additional server side encryption.
*Required*: No
*Type*: [SseSpecification](aws-properties-ec2-verifiedaccessgroup-ssespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-verifiedaccessgroup-tags"></a>
The tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-verifiedaccessgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerifiedAccessInstanceId`  <a name="cfn-ec2-verifiedaccessgroup-verifiedaccessinstanceid"></a>
The ID of the AWS Verified Access instance.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-verifiedaccessgroup-return-values"></a>

### Ref
<a name="aws-resource-ec2-verifiedaccessgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Verified Access group.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-verifiedaccessgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-verifiedaccessgroup-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The last updated time.

`Owner`  <a name="Owner-fn::getatt"></a>
The ID of the AWS account that owns the group.

`VerifiedAccessGroupArn`  <a name="VerifiedAccessGroupArn-fn::getatt"></a>
The ARN of the Verified Access group.

`VerifiedAccessGroupId`  <a name="VerifiedAccessGroupId-fn::getatt"></a>
The ID of the Verified Access group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
