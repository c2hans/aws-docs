---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-transition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket Transition
<a name="aws-properties-s3-bucket-transition"></a>

Specifies when an object transitions to a specified storage class. For more information about Amazon S3 lifecycle configuration rules, see [Transitioning Objects Using Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-transition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-transition-syntax.json"></a>

```
{
  "[StorageClass](#cfn-s3-bucket-transition-storageclass)" : {{String}},
  "[TransitionDate](#cfn-s3-bucket-transition-transitiondate)" : {{String}},
  "[TransitionInDays](#cfn-s3-bucket-transition-transitionindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3-bucket-transition-syntax.yaml"></a>

```
  [StorageClass](#cfn-s3-bucket-transition-storageclass): {{String}}
  [TransitionDate](#cfn-s3-bucket-transition-transitiondate): {{String}}
  [TransitionInDays](#cfn-s3-bucket-transition-transitionindays): {{Integer}}
```

## Properties
<a name="aws-properties-s3-bucket-transition-properties"></a>

`StorageClass`  <a name="cfn-s3-bucket-transition-storageclass"></a>
The storage class to which you want the object to transition.
*Required*: Yes
*Type*: String
*Allowed values*: `DEEP_ARCHIVE | GLACIER | Glacier | GLACIER_IR | INTELLIGENT_TIERING | ONEZONE_IA | STANDARD_IA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitionDate`  <a name="cfn-s3-bucket-transition-transitiondate"></a>
Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
*Required*: Conditional
*Type*: String
*Pattern*: `^(\d{4})-(0[0-9]|1[0-2])-([0-2]\d|3[01])T([01]\d|2[0-4]):([0-5]\d):([0-6]\d)((\.\d{3})?)Z$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitionInDays`  <a name="cfn-s3-bucket-transition-transitionindays"></a>
Indicates the number of days after creation when objects are transitioned to the specified storage class. The value can be `0` or any positive integer. Be aware that some storage classes have a minimum storage duration and that you're charged for transitioning objects before their minimum storage duration. For more information, see [ Constraints and considerations for transitions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-configuration-constraints) in the *Amazon S3 User Guide*.
*Required*: Conditional
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-s3-bucket-transition--seealso"></a>
+ AWS::S3::Bucket [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#aws-properties-s3-bucket--examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
