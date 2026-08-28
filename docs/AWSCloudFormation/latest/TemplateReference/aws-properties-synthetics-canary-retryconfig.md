---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-retryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary RetryConfig
<a name="aws-properties-synthetics-canary-retryconfig"></a>

The canary's retry configuration information.

## Syntax
<a name="aws-properties-synthetics-canary-retryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-retryconfig-syntax.json"></a>

```
{
  "[MaxRetries](#cfn-synthetics-canary-retryconfig-maxretries)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-retryconfig-syntax.yaml"></a>

```
  [MaxRetries](#cfn-synthetics-canary-retryconfig-maxretries): {{Integer}}
```

## Properties
<a name="aws-properties-synthetics-canary-retryconfig-properties"></a>

`MaxRetries`  <a name="cfn-synthetics-canary-retryconfig-maxretries"></a>
The maximum number of retries. The value must be less than or equal to two.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
