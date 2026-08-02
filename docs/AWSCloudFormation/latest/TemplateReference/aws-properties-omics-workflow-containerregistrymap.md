---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflow-containerregistrymap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow ContainerRegistryMap
<a name="aws-properties-omics-workflow-containerregistrymap"></a>

Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the *AWS HealthOmics User Guide*.

## Syntax
<a name="aws-properties-omics-workflow-containerregistrymap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflow-containerregistrymap-syntax.json"></a>

```
{
  "[ImageMappings](#cfn-omics-workflow-containerregistrymap-imagemappings)" : {{[ ImageMapping, ... ]}},
  "[RegistryMappings](#cfn-omics-workflow-containerregistrymap-registrymappings)" : {{[ RegistryMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-omics-workflow-containerregistrymap-syntax.yaml"></a>

```
  [ImageMappings](#cfn-omics-workflow-containerregistrymap-imagemappings): {{
    - ImageMapping}}
  [RegistryMappings](#cfn-omics-workflow-containerregistrymap-registrymappings): {{
    - RegistryMapping}}
```

## Properties
<a name="aws-properties-omics-workflow-containerregistrymap-properties"></a>

`ImageMappings`  <a name="cfn-omics-workflow-containerregistrymap-imagemappings"></a>
Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.
*Required*: No
*Type*: Array of [ImageMapping](aws-properties-omics-workflow-imagemapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RegistryMappings`  <a name="cfn-omics-workflow-containerregistrymap-registrymappings"></a>
Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.
*Required*: No
*Type*: Array of [RegistryMapping](aws-properties-omics-workflow-registrymapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
