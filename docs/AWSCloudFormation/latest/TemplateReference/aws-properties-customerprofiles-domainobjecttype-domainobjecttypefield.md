---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::DomainObjectType DomainObjectTypeField
<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield"></a>

<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield-description"></a>The `DomainObjectTypeField` property type specifies Property description not available. for an [AWS::CustomerProfiles::DomainObjectType](aws-resource-customerprofiles-domainobjecttype.md).

## Syntax
<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield-syntax.json"></a>

```
{
  "[ContentType](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-contenttype)" : {{String}},
  "[FeatureType](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-featuretype)" : {{String}},
  "[Source](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-source)" : {{String}},
  "[Target](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield-syntax.yaml"></a>

```
  [ContentType](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-contenttype): {{String}}
  [FeatureType](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-featuretype): {{String}}
  [Source](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-source): {{String}}
  [Target](#cfn-customerprofiles-domainobjecttype-domainobjecttypefield-target): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield-properties"></a>

`ContentType`  <a name="cfn-customerprofiles-domainobjecttype-domainobjecttypefield-contenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STRING | NUMBER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FeatureType`  <a name="cfn-customerprofiles-domainobjecttype-domainobjecttypefield-featuretype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `TEXTUAL | CATEGORICAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-customerprofiles-domainobjecttype-domainobjecttypefield-source"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Target`  <a name="cfn-customerprofiles-domainobjecttype-domainobjecttypefield-target"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
