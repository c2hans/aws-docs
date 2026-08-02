---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-osis-pipelineblueprint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::PipelineBlueprint
<a name="aws-resource-osis-pipelineblueprint"></a>

Container for information about an OpenSearch Ingestion blueprint.

## Syntax
<a name="aws-resource-osis-pipelineblueprint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-osis-pipelineblueprint-syntax.json"></a>

```
{
  "Type" : "AWS::OSIS::PipelineBlueprint",
  "Properties" : {
      "[BlueprintName](#cfn-osis-pipelineblueprint-blueprintname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-osis-pipelineblueprint-syntax.yaml"></a>

```
Type: AWS::OSIS::PipelineBlueprint
Properties:
  [BlueprintName](#cfn-osis-pipelineblueprint-blueprintname): {{String}}
```

## Properties
<a name="aws-resource-osis-pipelineblueprint-properties"></a>

`BlueprintName`  <a name="cfn-osis-pipelineblueprint-blueprintname"></a>
The name of the blueprint.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-osis-pipelineblueprint-return-values"></a>

### Ref
<a name="aws-resource-osis-pipelineblueprint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-osis-pipelineblueprint-return-values-fn--getatt"></a>

####
<a name="aws-resource-osis-pipelineblueprint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`DisplayDescription`  <a name="DisplayDescription-fn::getatt"></a>
A description of the blueprint.

`DisplayName`  <a name="DisplayName-fn::getatt"></a>
The display name of the blueprint.

`PipelineConfigurationBody`  <a name="PipelineConfigurationBody-fn::getatt"></a>
The YAML configuration of the blueprint.

`Service`  <a name="Service-fn::getatt"></a>
The name of the service that the blueprint is associated with.

`UseCase`  <a name="UseCase-fn::getatt"></a>
The use case that the blueprint relates to.
