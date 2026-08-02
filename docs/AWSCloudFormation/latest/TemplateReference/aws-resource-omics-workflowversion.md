---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-workflowversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::WorkflowVersion
<a name="aws-resource-omics-workflowversion"></a>

Creates a new workflow version for the workflow that you specify with the `workflowId` parameter.

When you create a new version of a workflow, you need to specify the configuration for the new version. It doesn't inherit any configuration values from the workflow.

Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.

**Note**
Don't include any personally identifiable information (PII) in the version name. Version names appear in the workflow version ARN.

For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the *AWS HealthOmics User Guide*.

## Syntax
<a name="aws-resource-omics-workflowversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-workflowversion-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::WorkflowVersion",
  "Properties" : {
      "[Accelerators](#cfn-omics-workflowversion-accelerators)" : {{String}},
      "[ContainerRegistryMap](#cfn-omics-workflowversion-containerregistrymap)" : {{ContainerRegistryMap}},
      "[ContainerRegistryMapUri](#cfn-omics-workflowversion-containerregistrymapuri)" : {{String}},
      "[DefinitionRepository](#cfn-omics-workflowversion-definitionrepository)" : {{DefinitionRepository}},
      "[DefinitionUri](#cfn-omics-workflowversion-definitionuri)" : {{String}},
      "[Description](#cfn-omics-workflowversion-description)" : {{String}},
      "[Engine](#cfn-omics-workflowversion-engine)" : {{String}},
      "[Main](#cfn-omics-workflowversion-main)" : {{String}},
      "[ParameterTemplate](#cfn-omics-workflowversion-parametertemplate)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ParameterTemplatePath](#cfn-omics-workflowversion-parametertemplatepath)" : {{String}},
      "[readmeMarkdown](#cfn-omics-workflowversion-readmemarkdown)" : {{String}},
      "[readmePath](#cfn-omics-workflowversion-readmepath)" : {{String}},
      "[readmeUri](#cfn-omics-workflowversion-readmeuri)" : {{String}},
      "[StorageCapacity](#cfn-omics-workflowversion-storagecapacity)" : {{Number}},
      "[StorageType](#cfn-omics-workflowversion-storagetype)" : {{String}},
      "[Tags](#cfn-omics-workflowversion-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[VersionName](#cfn-omics-workflowversion-versionname)" : {{String}},
      "[WorkflowBucketOwnerId](#cfn-omics-workflowversion-workflowbucketownerid)" : {{String}},
      "[WorkflowId](#cfn-omics-workflowversion-workflowid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-omics-workflowversion-syntax.yaml"></a>

```
Type: AWS::Omics::WorkflowVersion
Properties:
  [Accelerators](#cfn-omics-workflowversion-accelerators): {{String}}
  [ContainerRegistryMap](#cfn-omics-workflowversion-containerregistrymap): {{
    ContainerRegistryMap}}
  [ContainerRegistryMapUri](#cfn-omics-workflowversion-containerregistrymapuri): {{String}}
  [DefinitionRepository](#cfn-omics-workflowversion-definitionrepository): {{
    DefinitionRepository}}
  [DefinitionUri](#cfn-omics-workflowversion-definitionuri): {{String}}
  [Description](#cfn-omics-workflowversion-description): {{String}}
  [Engine](#cfn-omics-workflowversion-engine): {{String}}
  [Main](#cfn-omics-workflowversion-main): {{String}}
  [ParameterTemplate](#cfn-omics-workflowversion-parametertemplate): {{
    {{Key}}: {{Value}}}}
  [ParameterTemplatePath](#cfn-omics-workflowversion-parametertemplatepath): {{String}}
  [readmeMarkdown](#cfn-omics-workflowversion-readmemarkdown): {{String}}
  [readmePath](#cfn-omics-workflowversion-readmepath): {{String}}
  [readmeUri](#cfn-omics-workflowversion-readmeuri): {{String}}
  [StorageCapacity](#cfn-omics-workflowversion-storagecapacity): {{Number}}
  [StorageType](#cfn-omics-workflowversion-storagetype): {{String}}
  [Tags](#cfn-omics-workflowversion-tags): {{
    {{Key}}: {{Value}}}}
  [VersionName](#cfn-omics-workflowversion-versionname): {{String}}
  [WorkflowBucketOwnerId](#cfn-omics-workflowversion-workflowbucketownerid): {{String}}
  [WorkflowId](#cfn-omics-workflowversion-workflowid): {{String}}
```

## Properties
<a name="aws-resource-omics-workflowversion-properties"></a>

`Accelerators`  <a name="cfn-omics-workflowversion-accelerators"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GPU`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerRegistryMap`  <a name="cfn-omics-workflowversion-containerregistrymap"></a>
Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the *AWS HealthOmics User Guide*.
*Required*: No
*Type*: [ContainerRegistryMap](aws-properties-omics-workflowversion-containerregistrymap.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerRegistryMapUri`  <a name="cfn-omics-workflowversion-containerregistrymapuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefinitionRepository`  <a name="cfn-omics-workflowversion-definitionrepository"></a>
Contains information about a source code repository that hosts the workflow definition files.
*Required*: No
*Type*: [DefinitionRepository](aws-properties-omics-workflowversion-definitionrepository.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefinitionUri`  <a name="cfn-omics-workflowversion-definitionuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-omics-workflowversion-description"></a>
The description of the workflow version.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-omics-workflowversion-engine"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `WDL | NEXTFLOW | CWL`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Main`  <a name="cfn-omics-workflowversion-main"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterTemplate`  <a name="cfn-omics-workflowversion-parametertemplate"></a>
Property description not available.
*Required*: No
*Type*: Object of [WorkflowParameter](aws-properties-omics-workflowversion-workflowparameter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterTemplatePath`  <a name="cfn-omics-workflowversion-parametertemplatepath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\S]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`readmeMarkdown`  <a name="cfn-omics-workflowversion-readmemarkdown"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`readmePath`  <a name="cfn-omics-workflowversion-readmepath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`readmeUri`  <a name="cfn-omics-workflowversion-readmeuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/((.{1,1024}))$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCapacity`  <a name="cfn-omics-workflowversion-storagecapacity"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-omics-workflowversion-storagetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STATIC | DYNAMIC`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-omics-workflowversion-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionName`  <a name="cfn-omics-workflowversion-versionname"></a>
The name of the workflow version.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9\-\._]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkflowBucketOwnerId`  <a name="cfn-omics-workflowversion-workflowbucketownerid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkflowId`  <a name="cfn-omics-workflowversion-workflowid"></a>
The workflow's ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-workflowversion-return-values"></a>

### Ref
<a name="aws-resource-omics-workflowversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-workflowversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-workflowversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
ARN of the workflow version.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of the workflow version.

`Status`  <a name="Status-fn::getatt"></a>
The status of the workflow version.

`Type`  <a name="Type-fn::getatt"></a>
The type of the workflow version.

`Uuid`  <a name="Uuid-fn::getatt"></a>
Property description not available.
