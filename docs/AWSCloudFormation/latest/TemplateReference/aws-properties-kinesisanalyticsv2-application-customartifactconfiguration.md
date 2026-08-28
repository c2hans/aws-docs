---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application CustomArtifactConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-customartifactconfiguration"></a>

The configuration of connectors and user-defined functions.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-customartifactconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-customartifactconfiguration-syntax.json"></a>

```
{
  "[ArtifactType](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype)" : {{String}},
  "[MavenReference](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference)" : {{MavenReference}},
  "[S3ContentLocation](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation)" : {{S3ContentLocation}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-customartifactconfiguration-syntax.yaml"></a>

```
  [ArtifactType](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype): {{String}}
  [MavenReference](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference): {{
    MavenReference}}
  [S3ContentLocation](#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation): {{
    S3ContentLocation}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-customartifactconfiguration-properties"></a>

`ArtifactType`  <a name="cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype"></a>
 Set this to either `UDF` or `DEPENDENCY_JAR`. `UDF` stands for user-defined functions. This type of artifact must be in an S3 bucket. A `DEPENDENCY_JAR` can be in either Maven or an S3 bucket.
*Required*: Yes
*Type*: String
*Allowed values*: `DEPENDENCY_JAR | UDF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MavenReference`  <a name="cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference"></a>
The parameters required to fully specify a Maven reference.
*Required*: No
*Type*: [MavenReference](aws-properties-kinesisanalyticsv2-application-mavenreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ContentLocation`  <a name="cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation"></a>
The location of the custom artifacts.
*Required*: No
*Type*: [S3ContentLocation](aws-properties-kinesisanalyticsv2-application-s3contentlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
