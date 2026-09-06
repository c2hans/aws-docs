---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codeartifact-packagegroup-restrictiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeArtifact::PackageGroup RestrictionType
<a name="aws-properties-codeartifact-packagegroup-restrictiontype"></a>

<a name="aws-properties-codeartifact-packagegroup-restrictiontype-description"></a>The `RestrictionType` property type specifies Property description not available. for an [AWS::CodeArtifact::PackageGroup](aws-resource-codeartifact-packagegroup.md).

## Syntax
<a name="aws-properties-codeartifact-packagegroup-restrictiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codeartifact-packagegroup-restrictiontype-syntax.json"></a>

```
{
  "[Repositories](#cfn-codeartifact-packagegroup-restrictiontype-repositories)" : {{[ String, ... ]}},
  "[RestrictionMode](#cfn-codeartifact-packagegroup-restrictiontype-restrictionmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-codeartifact-packagegroup-restrictiontype-syntax.yaml"></a>

```
  [Repositories](#cfn-codeartifact-packagegroup-restrictiontype-repositories): {{
    - String}}
  [RestrictionMode](#cfn-codeartifact-packagegroup-restrictiontype-restrictionmode): {{String}}
```

## Properties
<a name="aws-properties-codeartifact-packagegroup-restrictiontype-properties"></a>

`Repositories`  <a name="cfn-codeartifact-packagegroup-restrictiontype-repositories"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictionMode`  <a name="cfn-codeartifact-packagegroup-restrictiontype-restrictionmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | BLOCK | ALLOW_SPECIFIC_REPOSITORIES | INHERIT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
