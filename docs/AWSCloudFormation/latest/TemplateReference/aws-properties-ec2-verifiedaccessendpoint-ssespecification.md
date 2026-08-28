---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-ssespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint SseSpecification
<a name="aws-properties-ec2-verifiedaccessendpoint-ssespecification"></a>

AWS Verified Access provides server side encryption by default to data at rest using AWS-owned KMS keys. You also have the option of using customer managed KMS keys, which can be specified using the options below.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-ssespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-ssespecification-syntax.json"></a>

```
{
  "[CustomerManagedKeyEnabled](#cfn-ec2-verifiedaccessendpoint-ssespecification-customermanagedkeyenabled)" : {{Boolean}},
  "[KmsKeyArn](#cfn-ec2-verifiedaccessendpoint-ssespecification-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-ssespecification-syntax.yaml"></a>

```
  [CustomerManagedKeyEnabled](#cfn-ec2-verifiedaccessendpoint-ssespecification-customermanagedkeyenabled): {{Boolean}}
  [KmsKeyArn](#cfn-ec2-verifiedaccessendpoint-ssespecification-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-ssespecification-properties"></a>

`CustomerManagedKeyEnabled`  <a name="cfn-ec2-verifiedaccessendpoint-ssespecification-customermanagedkeyenabled"></a>
 Enable or disable the use of customer managed KMS keys for server side encryption.
Valid values: `True` \| `False`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-ec2-verifiedaccessendpoint-ssespecification-kmskeyarn"></a>
 The ARN of the KMS key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
