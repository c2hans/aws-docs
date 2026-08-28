---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy SingleHeaderConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig"></a>

Determines which HTTP requests are sent to the staging distribution.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig-syntax.json"></a>

```
{
  "[Header](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-header)" : {{String}},
  "[Value](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig-syntax.yaml"></a>

```
  [Header](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-header): {{String}}
  [Value](#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-value): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig-properties"></a>

`Header`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-header"></a>
The request header name that you want CloudFront to send to your staging distribution. The header must contain the prefix `aws-cf-cd-`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-value"></a>
The request header value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1783`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
