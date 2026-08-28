---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-singleheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule SingleHeader
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-singleheader"></a>

 Structure containing a name field limited to 64 characters for header or query parameter identification.

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-singleheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-singleheader-syntax.json"></a>

```
{
  "[Name](#cfn-observabilityadmin-organizationtelemetryrule-singleheader-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-singleheader-syntax.yaml"></a>

```
  [Name](#cfn-observabilityadmin-organizationtelemetryrule-singleheader-name): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-singleheader-properties"></a>

`Name`  <a name="cfn-observabilityadmin-organizationtelemetryrule-singleheader-name"></a>
 The name value, limited to 64 characters.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
