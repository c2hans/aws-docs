---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-registryscanningconfiguration-repositoryfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RegistryScanningConfiguration RepositoryFilter
<a name="aws-properties-ecr-registryscanningconfiguration-repositoryfilter"></a>

The filter settings used with image replication. Specifying a repository filter to a replication rule provides a method for controlling which repositories in a private registry are replicated. If no filters are added, the contents of all repositories are replicated.

## Syntax
<a name="aws-properties-ecr-registryscanningconfiguration-repositoryfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-registryscanningconfiguration-repositoryfilter-syntax.json"></a>

```
{
  "[Filter](#cfn-ecr-registryscanningconfiguration-repositoryfilter-filter)" : {{String}},
  "[FilterType](#cfn-ecr-registryscanningconfiguration-repositoryfilter-filtertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-registryscanningconfiguration-repositoryfilter-syntax.yaml"></a>

```
  [Filter](#cfn-ecr-registryscanningconfiguration-repositoryfilter-filter): {{String}}
  [FilterType](#cfn-ecr-registryscanningconfiguration-repositoryfilter-filtertype): {{String}}
```

## Properties
<a name="aws-properties-ecr-registryscanningconfiguration-repositoryfilter-properties"></a>

`Filter`  <a name="cfn-ecr-registryscanningconfiguration-repositoryfilter-filter"></a>
The filter to use when scanning.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9*](?:[._\-/a-z0-9*]?[a-z0-9*]+)*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterType`  <a name="cfn-ecr-registryscanningconfiguration-repositoryfilter-filtertype"></a>
The type associated with the filter.
*Required*: Yes
*Type*: String
*Allowed values*: `WILDCARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
