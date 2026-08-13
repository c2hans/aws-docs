---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob CodegenFeatureFlags
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags"></a>

Describes the feature flags that you can specify for a code generation job.

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags-syntax.json"></a>

```
{
  "[IsNonModelSupported](#cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isnonmodelsupported)" : {{Boolean}},
  "[IsRelationshipSupported](#cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isrelationshipsupported)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags-syntax.yaml"></a>

```
  [IsNonModelSupported](#cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isnonmodelsupported): {{Boolean}}
  [IsRelationshipSupported](#cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isrelationshipsupported): {{Boolean}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags-properties"></a>

`IsNonModelSupported`  <a name="cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isnonmodelsupported"></a>
Specifies whether a code generation job supports non models.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsRelationshipSupported`  <a name="cfn-amplifyuibuilder-codegenjob-codegenfeatureflags-isrelationshipsupported"></a>
Specifes whether a code generation job supports data relationships.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
