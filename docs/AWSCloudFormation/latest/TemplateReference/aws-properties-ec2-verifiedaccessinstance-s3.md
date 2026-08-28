---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessinstance-s3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessInstance S3
<a name="aws-properties-ec2-verifiedaccessinstance-s3"></a>

Options for Amazon S3 as a logging destination.

## Syntax
<a name="aws-properties-ec2-verifiedaccessinstance-s3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessinstance-s3-syntax.json"></a>

```
{
  "[BucketName](#cfn-ec2-verifiedaccessinstance-s3-bucketname)" : {{String}},
  "[BucketOwner](#cfn-ec2-verifiedaccessinstance-s3-bucketowner)" : {{String}},
  "[Enabled](#cfn-ec2-verifiedaccessinstance-s3-enabled)" : {{Boolean}},
  "[Prefix](#cfn-ec2-verifiedaccessinstance-s3-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessinstance-s3-syntax.yaml"></a>

```
  [BucketName](#cfn-ec2-verifiedaccessinstance-s3-bucketname): {{String}}
  [BucketOwner](#cfn-ec2-verifiedaccessinstance-s3-bucketowner): {{String}}
  [Enabled](#cfn-ec2-verifiedaccessinstance-s3-enabled): {{Boolean}}
  [Prefix](#cfn-ec2-verifiedaccessinstance-s3-prefix): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessinstance-s3-properties"></a>

`BucketName`  <a name="cfn-ec2-verifiedaccessinstance-s3-bucketname"></a>
The bucket name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-ec2-verifiedaccessinstance-s3-bucketowner"></a>
The AWS account number that owns the bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ec2-verifiedaccessinstance-s3-enabled"></a>
Indicates whether logging is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-ec2-verifiedaccessinstance-s3-prefix"></a>
The bucket prefix.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
