---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-redirectallrequeststo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket RedirectAllRequestsTo
<a name="aws-properties-s3-bucket-redirectallrequeststo"></a>

Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

## Syntax
<a name="aws-properties-s3-bucket-redirectallrequeststo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-redirectallrequeststo-syntax.json"></a>

```
{
  "[HostName](#cfn-s3-bucket-redirectallrequeststo-hostname)" : {{String}},
  "[Protocol](#cfn-s3-bucket-redirectallrequeststo-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-redirectallrequeststo-syntax.yaml"></a>

```
  [HostName](#cfn-s3-bucket-redirectallrequeststo-hostname): {{String}}
  [Protocol](#cfn-s3-bucket-redirectallrequeststo-protocol): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-redirectallrequeststo-properties"></a>

`HostName`  <a name="cfn-s3-bucket-redirectallrequeststo-hostname"></a>
Name of the host where requests are redirected.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-s3-bucket-redirectallrequeststo-protocol"></a>
Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
*Required*: No
*Type*: String
*Allowed values*: `http | https`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
