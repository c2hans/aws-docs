---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion SourceBundle
<a name="aws-properties-elasticbeanstalk-applicationversion-sourcebundle"></a>

The `SourceBundle` property is an embedded property of the [AWS::ElasticBeanstalk::ApplicationVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html) resource. It specifies the Amazon S3 location of the source bundle for an AWS Elastic Beanstalk application version.

## Syntax
<a name="aws-properties-elasticbeanstalk-applicationversion-sourcebundle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-applicationversion-sourcebundle-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3bucket)" : {{String}},
  "[S3Key](#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3key)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-applicationversion-sourcebundle-syntax.yaml"></a>

```
  [S3Bucket](#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3bucket): {{String}}
  [S3Key](#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3key): {{String}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-applicationversion-sourcebundle-properties"></a>

`S3Bucket`  <a name="cfn-elasticbeanstalk-applicationversion-sourcebundle-s3bucket"></a>
The Amazon S3 bucket where the data is located.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Key`  <a name="cfn-elasticbeanstalk-applicationversion-sourcebundle-s3key"></a>
The Amazon S3 key where the data is located.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
