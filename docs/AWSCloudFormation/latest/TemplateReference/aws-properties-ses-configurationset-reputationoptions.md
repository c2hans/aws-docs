---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-reputationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet ReputationOptions
<a name="aws-properties-ses-configurationset-reputationoptions"></a>

Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.

## Syntax
<a name="aws-properties-ses-configurationset-reputationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-reputationoptions-syntax.json"></a>

```
{
  "[ReputationMetricsEnabled](#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-reputationoptions-syntax.yaml"></a>

```
  [ReputationMetricsEnabled](#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ses-configurationset-reputationoptions-properties"></a>

`ReputationMetricsEnabled`  <a name="cfn-ses-configurationset-reputationoptions-reputationmetricsenabled"></a>
If `true`, tracking of reputation metrics is enabled for the configuration set. If `false`, tracking of reputation metrics is disabled for the configuration set.
*Required*: No
*Type*: Boolean
*Pattern*: `true|false`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
