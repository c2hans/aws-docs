---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codeartifact-package.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeArtifact::Package
<a name="aws-resource-codeartifact-package"></a>

Sets the package origin configuration for a package.

The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see [Editing package origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html) in the *AWS CodeArtifact User Guide*.

`PutPackageOriginConfiguration` can be called on a package that doesn't yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.

## Syntax
<a name="aws-resource-codeartifact-package-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codeartifact-package-syntax.json"></a>

```
{
  "Type" : "AWS::CodeArtifact::Package",
  "Properties" : {
      "[DomainName](#cfn-codeartifact-package-domainname)" : {{String}},
      "[Format](#cfn-codeartifact-package-format)" : {{String}},
      "[Name](#cfn-codeartifact-package-name)" : {{String}},
      "[Namespace](#cfn-codeartifact-package-namespace)" : {{String}},
      "[Repository](#cfn-codeartifact-package-repository)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codeartifact-package-syntax.yaml"></a>

```
Type: AWS::CodeArtifact::Package
Properties:
  [DomainName](#cfn-codeartifact-package-domainname): {{String}}
  [Format](#cfn-codeartifact-package-format): {{String}}
  [Name](#cfn-codeartifact-package-name): {{String}}
  [Namespace](#cfn-codeartifact-package-namespace): {{String}}
  [Repository](#cfn-codeartifact-package-repository): {{String}}
```

## Properties
<a name="aws-resource-codeartifact-package-properties"></a>

`DomainName`  <a name="cfn-codeartifact-package-domainname"></a>
 The name of the domain that contains the package group.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9\-]{0,48}[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Format`  <a name="cfn-codeartifact-package-format"></a>
 The format of the package version.
*Required*: Yes
*Type*: String
*Allowed values*: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-codeartifact-package-name"></a>
The name of the package.
*Required*: Yes
*Type*: String
*Pattern*: `^[^#/\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-codeartifact-package-namespace"></a>
The namespace of the package version. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
*Required*: No
*Type*: String
*Pattern*: `^[^#/\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Repository`  <a name="cfn-codeartifact-package-repository"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9._\-]{1,99}$`
*Minimum*: `2`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codeartifact-package-return-values"></a>

### Ref
<a name="aws-resource-codeartifact-package-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codeartifact-package-return-values-fn--getatt"></a>

####
<a name="aws-resource-codeartifact-package-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The ARN of the package group.
