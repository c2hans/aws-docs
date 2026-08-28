---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-publicrepository-repositorycatalogdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::PublicRepository RepositoryCatalogData
<a name="aws-properties-ecr-publicrepository-repositorycatalogdata"></a>

The details about the repository that are publicly visible in the Amazon ECR Public Gallery. For more information, see [Amazon ECR Public repository catalog data](https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html) in the *Amazon ECR Public User Guide*.

## Syntax
<a name="aws-properties-ecr-publicrepository-repositorycatalogdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-publicrepository-repositorycatalogdata-syntax.json"></a>

```
{
  "[AboutText](#cfn-ecr-publicrepository-repositorycatalogdata-abouttext)" : {{String}},
  "[Architectures](#cfn-ecr-publicrepository-repositorycatalogdata-architectures)" : {{[ String, ... ]}},
  "[OperatingSystems](#cfn-ecr-publicrepository-repositorycatalogdata-operatingsystems)" : {{[ String, ... ]}},
  "[RepositoryDescription](#cfn-ecr-publicrepository-repositorycatalogdata-repositorydescription)" : {{String}},
  "[UsageText](#cfn-ecr-publicrepository-repositorycatalogdata-usagetext)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-publicrepository-repositorycatalogdata-syntax.yaml"></a>

```
  [AboutText](#cfn-ecr-publicrepository-repositorycatalogdata-abouttext): {{String}}
  [Architectures](#cfn-ecr-publicrepository-repositorycatalogdata-architectures): {{
    - String}}
  [OperatingSystems](#cfn-ecr-publicrepository-repositorycatalogdata-operatingsystems): {{
    - String}}
  [RepositoryDescription](#cfn-ecr-publicrepository-repositorycatalogdata-repositorydescription): {{String}}
  [UsageText](#cfn-ecr-publicrepository-repositorycatalogdata-usagetext): {{String}}
```

## Properties
<a name="aws-properties-ecr-publicrepository-repositorycatalogdata-properties"></a>

`AboutText`  <a name="cfn-ecr-publicrepository-repositorycatalogdata-abouttext"></a>
The longform description of the contents of the repository. This text appears in the repository details on the Amazon ECR Public Gallery.
*Required*: No
*Type*: String
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Architectures`  <a name="cfn-ecr-publicrepository-repositorycatalogdata-architectures"></a>
The architecture tags that are associated with the repository.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatingSystems`  <a name="cfn-ecr-publicrepository-repositorycatalogdata-operatingsystems"></a>
The operating system tags that are associated with the repository.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryDescription`  <a name="cfn-ecr-publicrepository-repositorycatalogdata-repositorydescription"></a>
The short description of the repository.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageText`  <a name="cfn-ecr-publicrepository-repositorycatalogdata-usagetext"></a>
The longform usage details of the contents of the repository. The usage text provides context for users of the repository.
*Required*: No
*Type*: String
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
