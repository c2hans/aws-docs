---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociatedPackage.html
---

# AssociatedPackage
<a name="API_AssociatedPackage"></a>

 A package associated with a package group.

## Contents
<a name="API_AssociatedPackage_Contents"></a>

 ** associationType **   <a name="codeartifact-Type-AssociatedPackage-associationType"></a>
Describes the strength of the association between the package and package group. A strong match can be thought of as an exact match, and a weak match can be thought of as a variation match, for example, the package name matches a variation of the package group pattern. For more information about package group pattern matching, including strong and weak matches, see [Package group definition syntax and matching behavior](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html) in the *CodeArtifact User Guide*.
Type: String
Valid Values: `STRONG | WEAK`
Required: No

 ** format **   <a name="codeartifact-Type-AssociatedPackage-format"></a>
A format that specifies the type of the associated package.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: No

 ** namespace **   <a name="codeartifact-Type-AssociatedPackage-namespace"></a>
The namespace of the associated package. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** package **   <a name="codeartifact-Type-AssociatedPackage-package"></a>
 The name of the associated package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

## See Also
<a name="API_AssociatedPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/AssociatedPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/AssociatedPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/AssociatedPackage)
