---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-artifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Artifact
<a name="aws-resource-securityagent-artifact"></a>

Uploads an artifact to an agent space. Artifacts provide additional context for security testing, such as architecture diagrams, API specifications, or configuration files.

## Syntax
<a name="aws-resource-securityagent-artifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-artifact-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::Artifact",
  "Properties" : {
      "[AgentSpaceId](#cfn-securityagent-artifact-agentspaceid)" : {{String}},
      "[ArtifactContent](#cfn-securityagent-artifact-artifactcontent)" : {{String}},
      "[ArtifactType](#cfn-securityagent-artifact-artifacttype)" : {{String}},
      "[FileName](#cfn-securityagent-artifact-filename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-artifact-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::Artifact
Properties:
  [AgentSpaceId](#cfn-securityagent-artifact-agentspaceid): {{String}}
  [ArtifactContent](#cfn-securityagent-artifact-artifactcontent): {{String}}
  [ArtifactType](#cfn-securityagent-artifact-artifacttype): {{String}}
  [FileName](#cfn-securityagent-artifact-filename): {{String}}
```

## Properties
<a name="aws-resource-securityagent-artifact-properties"></a>

`AgentSpaceId`  <a name="cfn-securityagent-artifact-agentspaceid"></a>
The unique identifier of the agent space that contains the artifact.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ArtifactContent`  <a name="cfn-securityagent-artifact-artifactcontent"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ArtifactType`  <a name="cfn-securityagent-artifact-artifacttype"></a>
The file type of the artifact.
*Required*: Yes
*Type*: String
*Allowed values*: `TXT | PNG | JPEG | MD | PDF | DOCX | DOC | JSON | YAML`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileName`  <a name="cfn-securityagent-artifact-filename"></a>
The file name of the artifact.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securityagent-artifact-return-values"></a>

### Ref
<a name="aws-resource-securityagent-artifact-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityagent-artifact-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityagent-artifact-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`ArtifactId`  <a name="ArtifactId-fn::getatt"></a>
The unique identifier of the artifact.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the artifact was last updated, in UTC format.
