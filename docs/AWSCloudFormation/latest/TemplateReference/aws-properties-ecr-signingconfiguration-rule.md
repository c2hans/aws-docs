---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-signingconfiguration-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::SigningConfiguration Rule
<a name="aws-properties-ecr-signingconfiguration-rule"></a>

A signing rule that specifies a signing profile and optional repository filters. When an image is pushed to a matching repository, a signing job is created using the specified profile.

## Syntax
<a name="aws-properties-ecr-signingconfiguration-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-signingconfiguration-rule-syntax.json"></a>

```
{
  "[RepositoryFilters](#cfn-ecr-signingconfiguration-rule-repositoryfilters)" : {{[ RepositoryFilter, ... ]}},
  "[SigningProfileArn](#cfn-ecr-signingconfiguration-rule-signingprofilearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-signingconfiguration-rule-syntax.yaml"></a>

```
  [RepositoryFilters](#cfn-ecr-signingconfiguration-rule-repositoryfilters): {{
    - RepositoryFilter}}
  [SigningProfileArn](#cfn-ecr-signingconfiguration-rule-signingprofilearn): {{String}}
```

## Properties
<a name="aws-properties-ecr-signingconfiguration-rule-properties"></a>

`RepositoryFilters`  <a name="cfn-ecr-signingconfiguration-rule-repositoryfilters"></a>
A list of repository filters that determine which repositories have their images signed on push. If no filters are specified, all images pushed to the registry are signed using the rule's signing profile. Maximum of 100 filters per rule.
*Required*: No
*Type*: Array of [RepositoryFilter](aws-properties-ecr-signingconfiguration-repositoryfilter.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SigningProfileArn`  <a name="cfn-ecr-signingconfiguration-rule-signingprofilearn"></a>
The ARN of the AWS Signer signing profile to use for signing images that match this rule. For more information about signing profiles, see [Signing profiles](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html) in the *AWS Signer Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:signer:[a-z0-9-]+:[0-9]{12}:\/signing-profiles\/[a-zA-Z0-9_]{2,}$`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
