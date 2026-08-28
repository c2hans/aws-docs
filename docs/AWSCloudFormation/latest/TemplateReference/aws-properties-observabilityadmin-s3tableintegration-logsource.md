---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-s3tableintegration-logsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::S3TableIntegration LogSource
<a name="aws-properties-observabilityadmin-s3tableintegration-logsource"></a>

A data source with an S3 Table integration for query access in the `logs` namespace.

## Syntax
<a name="aws-properties-observabilityadmin-s3tableintegration-logsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-s3tableintegration-logsource-syntax.json"></a>

```
{
  "[Identifier](#cfn-observabilityadmin-s3tableintegration-logsource-identifier)" : {{String}},
  "[Name](#cfn-observabilityadmin-s3tableintegration-logsource-name)" : {{String}},
  "[Type](#cfn-observabilityadmin-s3tableintegration-logsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-s3tableintegration-logsource-syntax.yaml"></a>

```
  [Identifier](#cfn-observabilityadmin-s3tableintegration-logsource-identifier): {{String}}
  [Name](#cfn-observabilityadmin-s3tableintegration-logsource-name): {{String}}
  [Type](#cfn-observabilityadmin-s3tableintegration-logsource-type): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-s3tableintegration-logsource-properties"></a>

`Identifier`  <a name="cfn-observabilityadmin-s3tableintegration-logsource-identifier"></a>
The unique identifier for the association between the data source and S3 Table integration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-observabilityadmin-s3tableintegration-logsource-name"></a>
The name of the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-observabilityadmin-s3tableintegration-logsource-type"></a>
The type of the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
