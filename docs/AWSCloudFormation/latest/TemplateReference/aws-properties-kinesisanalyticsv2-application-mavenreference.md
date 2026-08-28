---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-mavenreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application MavenReference
<a name="aws-properties-kinesisanalyticsv2-application-mavenreference"></a>

The information required to specify a Maven reference. You can use Maven references to specify dependency JAR files.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-mavenreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-mavenreference-syntax.json"></a>

```
{
  "[ArtifactId](#cfn-kinesisanalyticsv2-application-mavenreference-artifactid)" : {{String}},
  "[GroupId](#cfn-kinesisanalyticsv2-application-mavenreference-groupid)" : {{String}},
  "[Version](#cfn-kinesisanalyticsv2-application-mavenreference-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-mavenreference-syntax.yaml"></a>

```
  [ArtifactId](#cfn-kinesisanalyticsv2-application-mavenreference-artifactid): {{String}}
  [GroupId](#cfn-kinesisanalyticsv2-application-mavenreference-groupid): {{String}}
  [Version](#cfn-kinesisanalyticsv2-application-mavenreference-version): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-mavenreference-properties"></a>

`ArtifactId`  <a name="cfn-kinesisanalyticsv2-application-mavenreference-artifactid"></a>
The artifact ID of the Maven reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupId`  <a name="cfn-kinesisanalyticsv2-application-mavenreference-groupid"></a>
The group ID of the Maven reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-kinesisanalyticsv2-application-mavenreference-version"></a>
The version of the Maven reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
