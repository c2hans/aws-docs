---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationtelemetryrule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationTelemetryRule Tag
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-tag"></a>

 A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)

## Syntax
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-observabilityadmin-organizationtelemetryrule-tag-key)" : {{String}},
  "[Value](#cfn-observabilityadmin-organizationtelemetryrule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-tag-syntax.yaml"></a>

```
  [Key](#cfn-observabilityadmin-organizationtelemetryrule-tag-key): {{String}}
  [Value](#cfn-observabilityadmin-organizationtelemetryrule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationtelemetryrule-tag-properties"></a>

`Key`  <a name="cfn-observabilityadmin-organizationtelemetryrule-tag-key"></a>
One part of a key-value pair that makes up a tag associated with the organization's telemetry rule resource. A key is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-observabilityadmin-organizationtelemetryrule-tag-value"></a>
One part of a key-value pair that make up a tag associated with the organization's telemetry rule resource. A value acts as a descriptor within a tag category (key). The value can be empty or null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
