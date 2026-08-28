---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-registryscanningconfiguration-scanningrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RegistryScanningConfiguration ScanningRule
<a name="aws-properties-ecr-registryscanningconfiguration-scanningrule"></a>

The scanning rules associated with the registry.

## Syntax
<a name="aws-properties-ecr-registryscanningconfiguration-scanningrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-registryscanningconfiguration-scanningrule-syntax.json"></a>

```
{
  "[RepositoryFilters](#cfn-ecr-registryscanningconfiguration-scanningrule-repositoryfilters)" : {{[ RepositoryFilter, ... ]}},
  "[ScanFrequency](#cfn-ecr-registryscanningconfiguration-scanningrule-scanfrequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-registryscanningconfiguration-scanningrule-syntax.yaml"></a>

```
  [RepositoryFilters](#cfn-ecr-registryscanningconfiguration-scanningrule-repositoryfilters): {{
    - RepositoryFilter}}
  [ScanFrequency](#cfn-ecr-registryscanningconfiguration-scanningrule-scanfrequency): {{String}}
```

## Properties
<a name="aws-properties-ecr-registryscanningconfiguration-scanningrule-properties"></a>

`RepositoryFilters`  <a name="cfn-ecr-registryscanningconfiguration-scanningrule-repositoryfilters"></a>
The details of a scanning repository filter. For more information on how to use filters, see [Using filters](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html#image-scanning-filters) in the *Amazon Elastic Container Registry User Guide*.
*Required*: Yes
*Type*: Array of [RepositoryFilter](aws-properties-ecr-registryscanningconfiguration-repositoryfilter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanFrequency`  <a name="cfn-ecr-registryscanningconfiguration-scanningrule-scanfrequency"></a>
The frequency that scans are performed at for a private registry. When the `ENHANCED` scan type is specified, the supported scan frequencies are `CONTINUOUS_SCAN` and `SCAN_ON_PUSH`. When the `BASIC` scan type is specified, the `SCAN_ON_PUSH` scan frequency is supported. If scan on push is not specified, then the `MANUAL` scan frequency is set by default.
*Required*: Yes
*Type*: String
*Allowed values*: `SCAN_ON_PUSH | CONTINUOUS_SCAN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
