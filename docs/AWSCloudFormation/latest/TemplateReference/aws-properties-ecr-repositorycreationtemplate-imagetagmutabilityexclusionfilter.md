---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RepositoryCreationTemplate ImageTagMutabilityExclusionFilter
<a name="aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter"></a>

A filter that specifies which image tags should be excluded from the repository's image tag mutability setting.

## Syntax
<a name="aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-syntax.json"></a>

```
{
  "[ImageTagMutabilityExclusionFilterType](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltertype)" : {{String}},
  "[ImageTagMutabilityExclusionFilterValue](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-syntax.yaml"></a>

```
  [ImageTagMutabilityExclusionFilterType](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltertype): {{String}}
  [ImageTagMutabilityExclusionFilterValue](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltervalue): {{String}}
```

## Properties
<a name="aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-properties"></a>

`ImageTagMutabilityExclusionFilterType`  <a name="cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltertype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `WILDCARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageTagMutabilityExclusionFilterValue`  <a name="cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter-imagetagmutabilityexclusionfiltervalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z._*-]{1,128}`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
