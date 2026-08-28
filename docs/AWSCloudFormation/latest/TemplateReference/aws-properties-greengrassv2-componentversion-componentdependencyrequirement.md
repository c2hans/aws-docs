---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::ComponentVersion ComponentDependencyRequirement
<a name="aws-properties-greengrassv2-componentversion-componentdependencyrequirement"></a>

Contains information about a component dependency for a Lambda function component.

## Syntax
<a name="aws-properties-greengrassv2-componentversion-componentdependencyrequirement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-componentversion-componentdependencyrequirement-syntax.json"></a>

```
{
  "[DependencyType](#cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype)" : {{String}},
  "[VersionRequirement](#cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrassv2-componentversion-componentdependencyrequirement-syntax.yaml"></a>

```
  [DependencyType](#cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype): {{String}}
  [VersionRequirement](#cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement): {{String}}
```

## Properties
<a name="aws-properties-greengrassv2-componentversion-componentdependencyrequirement-properties"></a>

`DependencyType`  <a name="cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype"></a>
The type of this dependency. Choose from the following options:
+ `SOFT` – The component doesn't restart if the dependency changes state.
+ `HARD` – The component restarts if the dependency changes state.
Default: `HARD`
*Required*: No
*Type*: String
*Allowed values*: `SOFT | HARD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VersionRequirement`  <a name="cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement"></a>
The component version requirement for the component dependency.
AWS IoT Greengrass uses semantic version constraints. For more information, see [Semantic Versioning](https://semver.org/).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
