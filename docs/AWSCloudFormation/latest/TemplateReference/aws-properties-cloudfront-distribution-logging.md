---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-logging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution Logging
<a name="aws-properties-cloudfront-distribution-logging"></a>

A complex type that specifies whether access logs are written for the distribution.

**Note**
If you already enabled standard logging (legacy) and you want to enable standard logging (v2) to send your access logs to Amazon S3, we recommend that you specify a *different* Amazon S3 bucket or use a *separate path* in the same bucket (for example, use a log prefix or partitioning). This helps you keep track of which log files are associated with which logging subscription and prevents log files from overwriting each other. For more information, see [Standard logging (access logs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-properties-cloudfront-distribution-logging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-logging-syntax.json"></a>

```
{
  "[Bucket](#cfn-cloudfront-distribution-logging-bucket)" : {{String}},
  "[IncludeCookies](#cfn-cloudfront-distribution-logging-includecookies)" : {{Boolean}},
  "[Prefix](#cfn-cloudfront-distribution-logging-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-logging-syntax.yaml"></a>

```
  [Bucket](#cfn-cloudfront-distribution-logging-bucket): {{String}}
  [IncludeCookies](#cfn-cloudfront-distribution-logging-includecookies): {{Boolean}}
  [Prefix](#cfn-cloudfront-distribution-logging-prefix): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-logging-properties"></a>

`Bucket`  <a name="cfn-cloudfront-distribution-logging-bucket"></a>
The Amazon S3 bucket to store the access logs in, for example, `amzn-s3-demo-bucket.s3.amazonaws.com`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeCookies`  <a name="cfn-cloudfront-distribution-logging-includecookies"></a>
Specifies whether you want CloudFront to include cookies in access logs, specify `true` for `IncludeCookies`. If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don't want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify `false` for `IncludeCookies`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-cloudfront-distribution-logging-prefix"></a>
An optional string that you want CloudFront to prefix to the access log `filenames` for this distribution, for example, `myprefix/`. If you want to enable logging, but you don't want to specify a prefix, you still must include an empty `Prefix` element in the `Logging` element.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-logging--seealso"></a>
+ [LoggingConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_LoggingConfig.html) in the *Amazon CloudFront API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
