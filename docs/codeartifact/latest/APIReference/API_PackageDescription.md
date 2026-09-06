---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html
---

# PackageDescription
<a name="API_PackageDescription"></a>

Details about a package.

## Contents
<a name="API_PackageDescription_Contents"></a>

 ** format **   <a name="codeartifact-Type-PackageDescription-format"></a>
A format that specifies the type of the package.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: No

 ** name **   <a name="codeartifact-Type-PackageDescription-name"></a>
The name of the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** namespace **   <a name="codeartifact-Type-PackageDescription-namespace"></a>
The namespace of the package. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** originConfiguration **   <a name="codeartifact-Type-PackageDescription-originConfiguration"></a>
The package origin configuration for the package.
Type: [PackageOriginConfiguration](API_PackageOriginConfiguration.md) object
Required: No

## See Also
<a name="API_PackageDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageDescription)
