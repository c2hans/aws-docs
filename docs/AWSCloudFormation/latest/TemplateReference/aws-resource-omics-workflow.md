---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-workflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow
<a name="aws-resource-omics-workflow"></a>

Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:
+ *Workflow definition file:* A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in `.zip` format. For more information, see [Workflow definition files](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html) in AWS HealthOmics.
  + You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see [Example prompts for Amazon Q CLI](https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts) and the [AWS HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai) on GitHub.
+ *(Optional) Parameter template file:* A parameter template file written in JSON. Create the file to define the run parameters, or AWS HealthOmics generates the parameter template for you. For more information, see [Parameter template files for HealthOmics workflows](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html).
+ *ECR container images:* Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.
+ *(Optional) Sentieon licenses:* Request a Sentieon license to use the Sentieon software in private workflows.

For more information, see [Creating or updating a private workflow in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html) in the *AWS HealthOmics User Guide*.

## Syntax
<a name="aws-resource-omics-workflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-workflow-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::Workflow",
  "Properties" : {
      "[Accelerators](#cfn-omics-workflow-accelerators)" : {{String}},
      "[ContainerRegistryMap](#cfn-omics-workflow-containerregistrymap)" : {{ContainerRegistryMap}},
      "[ContainerRegistryMapUri](#cfn-omics-workflow-containerregistrymapuri)" : {{String}},
      "[DefinitionRepository](#cfn-omics-workflow-definitionrepository)" : {{DefinitionRepository}},
      "[DefinitionUri](#cfn-omics-workflow-definitionuri)" : {{String}},
      "[Description](#cfn-omics-workflow-description)" : {{String}},
      "[Engine](#cfn-omics-workflow-engine)" : {{String}},
      "[Main](#cfn-omics-workflow-main)" : {{String}},
      "[Name](#cfn-omics-workflow-name)" : {{String}},
      "[ParameterTemplate](#cfn-omics-workflow-parametertemplate)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ParameterTemplatePath](#cfn-omics-workflow-parametertemplatepath)" : {{String}},
      "[readmeMarkdown](#cfn-omics-workflow-readmemarkdown)" : {{String}},
      "[readmePath](#cfn-omics-workflow-readmepath)" : {{String}},
      "[readmeUri](#cfn-omics-workflow-readmeuri)" : {{String}},
      "[StorageCapacity](#cfn-omics-workflow-storagecapacity)" : {{Number}},
      "[StorageType](#cfn-omics-workflow-storagetype)" : {{String}},
      "[Tags](#cfn-omics-workflow-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[WorkflowBucketOwnerId](#cfn-omics-workflow-workflowbucketownerid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-omics-workflow-syntax.yaml"></a>

```
Type: AWS::Omics::Workflow
Properties:
  [Accelerators](#cfn-omics-workflow-accelerators): {{String}}
  [ContainerRegistryMap](#cfn-omics-workflow-containerregistrymap): {{
    ContainerRegistryMap}}
  [ContainerRegistryMapUri](#cfn-omics-workflow-containerregistrymapuri): {{String}}
  [DefinitionRepository](#cfn-omics-workflow-definitionrepository): {{
    DefinitionRepository}}
  [DefinitionUri](#cfn-omics-workflow-definitionuri): {{String}}
  [Description](#cfn-omics-workflow-description): {{String}}
  [Engine](#cfn-omics-workflow-engine): {{String}}
  [Main](#cfn-omics-workflow-main): {{String}}
  [Name](#cfn-omics-workflow-name): {{String}}
  [ParameterTemplate](#cfn-omics-workflow-parametertemplate): {{
    {{Key}}: {{Value}}}}
  [ParameterTemplatePath](#cfn-omics-workflow-parametertemplatepath): {{String}}
  [readmeMarkdown](#cfn-omics-workflow-readmemarkdown): {{String}}
  [readmePath](#cfn-omics-workflow-readmepath): {{String}}
  [readmeUri](#cfn-omics-workflow-readmeuri): {{String}}
  [StorageCapacity](#cfn-omics-workflow-storagecapacity): {{Number}}
  [StorageType](#cfn-omics-workflow-storagetype): {{String}}
  [Tags](#cfn-omics-workflow-tags): {{
    {{Key}}: {{Value}}}}
  [WorkflowBucketOwnerId](#cfn-omics-workflow-workflowbucketownerid): {{String}}
```

## Properties
<a name="aws-resource-omics-workflow-properties"></a>

`Accelerators`  <a name="cfn-omics-workflow-accelerators"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GPU`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerRegistryMap`  <a name="cfn-omics-workflow-containerregistrymap"></a>
Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the *AWS HealthOmics User Guide*.
*Required*: No
*Type*: [ContainerRegistryMap](aws-properties-omics-workflow-containerregistrymap.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerRegistryMapUri`  <a name="cfn-omics-workflow-containerregistrymapuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefinitionRepository`  <a name="cfn-omics-workflow-definitionrepository"></a>
Contains information about a source code repository that hosts the workflow definition files.
*Required*: No
*Type*: [DefinitionRepository](aws-properties-omics-workflow-definitionrepository.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefinitionUri`  <a name="cfn-omics-workflow-definitionuri"></a>
The URI of a definition for the workflow.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-omics-workflow-description"></a>
The parameter's description.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-omics-workflow-engine"></a>
An engine for the workflow.
*Required*: No
*Type*: String
*Allowed values*: `WDL | NEXTFLOW | CWL`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Main`  <a name="cfn-omics-workflow-main"></a>
The path of the main definition file for the workflow.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-omics-workflow-name"></a>
The workflow's name.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterTemplate`  <a name="cfn-omics-workflow-parametertemplate"></a>
The workflow's parameter template.
*Required*: No
*Type*: Object of [WorkflowParameter](aws-properties-omics-workflow-workflowparameter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterTemplatePath`  <a name="cfn-omics-workflow-parametertemplatepath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\S]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`readmeMarkdown`  <a name="cfn-omics-workflow-readmemarkdown"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`readmePath`  <a name="cfn-omics-workflow-readmepath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`readmeUri`  <a name="cfn-omics-workflow-readmeuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/((.{1,1024}))$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCapacity`  <a name="cfn-omics-workflow-storagecapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The `storageCapacity` can be overwritten at run time. The storage capacity is not required for runs with a `DYNAMIC` storage type.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageType`  <a name="cfn-omics-workflow-storagetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STATIC | DYNAMIC`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-omics-workflow-tags"></a>
Tags for the workflow.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowBucketOwnerId`  <a name="cfn-omics-workflow-workflowbucketownerid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-workflow-return-values"></a>

### Ref
<a name="aws-resource-omics-workflow-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the details of this resource. For example:

`{ "Ref": "Workflow.Type" }``Ref` returns the type of workflow.

### Fn::GetAtt
<a name="aws-resource-omics-workflow-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-omics-workflow-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN for the workflow.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the workflow was created.

`Id`  <a name="Id-fn::getatt"></a>
The workflow's ID.

`Status`  <a name="Status-fn::getatt"></a>
The workflow's status.

`Type`  <a name="Type-fn::getatt"></a>
The workflow's type.

`Uuid`  <a name="Uuid-fn::getatt"></a>
Property description not available.
