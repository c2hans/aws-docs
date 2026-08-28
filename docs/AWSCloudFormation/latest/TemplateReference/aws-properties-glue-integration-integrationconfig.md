---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-integration-integrationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Integration IntegrationConfig
<a name="aws-properties-glue-integration-integrationconfig"></a>

Properties associated with the integration.

## Syntax
<a name="aws-properties-glue-integration-integrationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-integration-integrationconfig-syntax.json"></a>

```
{
  "[ContinuousSync](#cfn-glue-integration-integrationconfig-continuoussync)" : {{Boolean}},
  "[RefreshInterval](#cfn-glue-integration-integrationconfig-refreshinterval)" : {{String}},
  "[SourceProperties](#cfn-glue-integration-integrationconfig-sourceproperties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-glue-integration-integrationconfig-syntax.yaml"></a>

```
  [ContinuousSync](#cfn-glue-integration-integrationconfig-continuoussync): {{Boolean}}
  [RefreshInterval](#cfn-glue-integration-integrationconfig-refreshinterval): {{String}}
  [SourceProperties](#cfn-glue-integration-integrationconfig-sourceproperties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-glue-integration-integrationconfig-properties"></a>

`ContinuousSync`  <a name="cfn-glue-integration-integrationconfig-continuoussync"></a>
Enables continuous synchronization for on-demand data extractions from SaaS applications to AWS data services like Amazon Redshift and Amazon S3.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RefreshInterval`  <a name="cfn-glue-integration-integrationconfig-refreshinterval"></a>
Specifies the frequency at which CDC (Change Data Capture) pulls or incremental loads should occur. This parameter provides flexibility to align the refresh rate with your specific data update patterns, system load considerations, and performance optimization goals. Time increment can be set from 15 minutes to 8640 minutes (six days).
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceProperties`  <a name="cfn-glue-integration-integrationconfig-sourceproperties"></a>
 A collection of key-value pairs that specify additional properties for the integration source. These properties provide configuration options that can be used to customize the behavior of the ODB source during data integration operations.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
