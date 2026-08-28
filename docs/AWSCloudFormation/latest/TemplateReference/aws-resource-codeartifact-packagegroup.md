---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codeartifact-packagegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeArtifact::PackageGroup
<a name="aws-resource-codeartifact-packagegroup"></a>

 Creates a package group. For more information about creating package groups, including example CLI commands, see [Create a package group](https://docs.aws.amazon.com/codeartifact/latest/ug/create-package-group.html) in the *CodeArtifact User Guide*.

## Syntax
<a name="aws-resource-codeartifact-packagegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codeartifact-packagegroup-syntax.json"></a>

```
{
  "Type" : "AWS::CodeArtifact::PackageGroup",
  "Properties" : {
      "[ContactInfo](#cfn-codeartifact-packagegroup-contactinfo)" : {{String}},
      "[Description](#cfn-codeartifact-packagegroup-description)" : {{String}},
      "[DomainName](#cfn-codeartifact-packagegroup-domainname)" : {{String}},
      "[DomainOwner](#cfn-codeartifact-packagegroup-domainowner)" : {{String}},
      "[OriginConfiguration](#cfn-codeartifact-packagegroup-originconfiguration)" : {{OriginConfiguration}},
      "[Pattern](#cfn-codeartifact-packagegroup-pattern)" : {{String}},
      "[Tags](#cfn-codeartifact-packagegroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-codeartifact-packagegroup-syntax.yaml"></a>

```
Type: AWS::CodeArtifact::PackageGroup
Properties:
  [ContactInfo](#cfn-codeartifact-packagegroup-contactinfo): {{String}}
  [Description](#cfn-codeartifact-packagegroup-description): {{String}}
  [DomainName](#cfn-codeartifact-packagegroup-domainname): {{String}}
  [DomainOwner](#cfn-codeartifact-packagegroup-domainowner): {{String}}
  [OriginConfiguration](#cfn-codeartifact-packagegroup-originconfiguration): {{
    OriginConfiguration}}
  [Pattern](#cfn-codeartifact-packagegroup-pattern): {{String}}
  [Tags](#cfn-codeartifact-packagegroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-codeartifact-packagegroup-properties"></a>

`ContactInfo`  <a name="cfn-codeartifact-packagegroup-contactinfo"></a>
 The contact information of the package group.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-codeartifact-packagegroup-description"></a>
 The description of the package group.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-codeartifact-packagegroup-domainname"></a>
 The domain that contains the package group.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z][a-z0-9\-]{0,48}[a-z0-9])$`
*Minimum*: `2`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainOwner`  <a name="cfn-codeartifact-packagegroup-domainowner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
*Required*: No
*Type*: String
*Pattern*: `[0-9]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginConfiguration`  <a name="cfn-codeartifact-packagegroup-originconfiguration"></a>
Details about the package origin configuration of a package group.
*Required*: No
*Type*: [OriginConfiguration](aws-properties-codeartifact-packagegroup-originconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pattern`  <a name="cfn-codeartifact-packagegroup-pattern"></a>
 The pattern of the package group. The pattern determines which packages are associated with the package group.
*Required*: Yes
*Type*: String
*Minimum*: `2`
*Maximum*: `520`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-codeartifact-packagegroup-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-codeartifact-packagegroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codeartifact-packagegroup-return-values"></a>

### Ref
<a name="aws-resource-codeartifact-packagegroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codeartifact-packagegroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-codeartifact-packagegroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The ARN of the package group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
