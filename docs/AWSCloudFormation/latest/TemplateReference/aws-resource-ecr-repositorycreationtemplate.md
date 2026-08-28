---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-repositorycreationtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::RepositoryCreationTemplate
<a name="aws-resource-ecr-repositorycreationtemplate"></a>

The details of the repository creation template associated with the request.

## Syntax
<a name="aws-resource-ecr-repositorycreationtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecr-repositorycreationtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::ECR::RepositoryCreationTemplate",
  "Properties" : {
      "[AppliedFor](#cfn-ecr-repositorycreationtemplate-appliedfor)" : {{[ String, ... ]}},
      "[CustomRoleArn](#cfn-ecr-repositorycreationtemplate-customrolearn)" : {{String}},
      "[Description](#cfn-ecr-repositorycreationtemplate-description)" : {{String}},
      "[EncryptionConfiguration](#cfn-ecr-repositorycreationtemplate-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[ImageTagMutability](#cfn-ecr-repositorycreationtemplate-imagetagmutability)" : {{String}},
      "[ImageTagMutabilityExclusionFilters](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilters)" : {{[ ImageTagMutabilityExclusionFilter, ... ]}},
      "[LifecyclePolicy](#cfn-ecr-repositorycreationtemplate-lifecyclepolicy)" : {{String}},
      "[Prefix](#cfn-ecr-repositorycreationtemplate-prefix)" : {{String}},
      "[RepositoryPolicy](#cfn-ecr-repositorycreationtemplate-repositorypolicy)" : {{String}},
      "[ResourceTags](#cfn-ecr-repositorycreationtemplate-resourcetags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecr-repositorycreationtemplate-syntax.yaml"></a>

```
Type: AWS::ECR::RepositoryCreationTemplate
Properties:
  [AppliedFor](#cfn-ecr-repositorycreationtemplate-appliedfor): {{
    - String}}
  [CustomRoleArn](#cfn-ecr-repositorycreationtemplate-customrolearn): {{String}}
  [Description](#cfn-ecr-repositorycreationtemplate-description): {{String}}
  [EncryptionConfiguration](#cfn-ecr-repositorycreationtemplate-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [ImageTagMutability](#cfn-ecr-repositorycreationtemplate-imagetagmutability): {{String}}
  [ImageTagMutabilityExclusionFilters](#cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilters): {{
    - ImageTagMutabilityExclusionFilter}}
  [LifecyclePolicy](#cfn-ecr-repositorycreationtemplate-lifecyclepolicy): {{String}}
  [Prefix](#cfn-ecr-repositorycreationtemplate-prefix): {{String}}
  [RepositoryPolicy](#cfn-ecr-repositorycreationtemplate-repositorypolicy): {{String}}
  [ResourceTags](#cfn-ecr-repositorycreationtemplate-resourcetags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ecr-repositorycreationtemplate-properties"></a>

`AppliedFor`  <a name="cfn-ecr-repositorycreationtemplate-appliedfor"></a>
A list of enumerable Strings representing the repository creation scenarios that this template will apply towards. The supported scenarios are PULL\_THROUGH\_CACHE, REPLICATION, and CREATE\_ON\_PUSH
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomRoleArn`  <a name="cfn-ecr-repositorycreationtemplate-customrolearn"></a>
The ARN of the role to be assumed by Amazon ECR. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/[A-Za-z0-9+=,-.@_]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ecr-repositorycreationtemplate-description"></a>
The description associated with the repository creation template.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-ecr-repositorycreationtemplate-encryptionconfiguration"></a>
The encryption configuration associated with the repository creation template.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-ecr-repositorycreationtemplate-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageTagMutability`  <a name="cfn-ecr-repositorycreationtemplate-imagetagmutability"></a>
The tag mutability setting for the repository. If this parameter is omitted, the default setting of `MUTABLE` will be used which will allow image tags to be overwritten. If `IMMUTABLE` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
*Required*: No
*Type*: String
*Allowed values*: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageTagMutabilityExclusionFilters`  <a name="cfn-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilters"></a>
A list of filters that specify which image tags are excluded from the repository creation template's image tag mutability setting.
*Required*: No
*Type*: Array of [ImageTagMutabilityExclusionFilter](aws-properties-ecr-repositorycreationtemplate-imagetagmutabilityexclusionfilter.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecyclePolicy`  <a name="cfn-ecr-repositorycreationtemplate-lifecyclepolicy"></a>
The lifecycle policy to use for repositories created using the template.
*Required*: No
*Type*: String
*Minimum*: `100`
*Maximum*: `30720`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-ecr-repositorycreationtemplate-prefix"></a>
The repository namespace prefix associated with the repository creation template.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryPolicy`  <a name="cfn-ecr-repositorycreationtemplate-repositorypolicy"></a>
The repository policy to apply to repositories created using the template. A repository policy is a permissions policy associated with a repository to control access permissions.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-ecr-repositorycreationtemplate-resourcetags"></a>
The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecr-repositorycreationtemplate-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecr-repositorycreationtemplate-return-values"></a>

### Ref
<a name="aws-resource-ecr-repositorycreationtemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecr-repositorycreationtemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecr-repositorycreationtemplate-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time, in JavaScript date format, when the repository creation template was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time, in JavaScript date format, when the repository creation template was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
