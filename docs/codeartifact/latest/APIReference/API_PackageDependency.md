---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html
---

# PackageDependency
<a name="API_PackageDependency"></a>

 Details about a package dependency.

## Contents
<a name="API_PackageDependency_Contents"></a>

 ** dependencyType **   <a name="codeartifact-Type-PackageDependency-dependencyType"></a>
 The type of a package dependency. The possible values depend on the package type.
+ npm: `regular`, `dev`, `peer`, `optional`
+ maven: `optional`, `parent`, `compile`, `runtime`, `test`, `system`, `provided`.
**Note**
Note that `parent` is not a regular Maven dependency type; instead this is extracted from the `<parent>` element if one is defined in the package version's POM file.
+ nuget: The `dependencyType` field is never set for NuGet packages.
+ pypi: `Requires-Dist`
Type: String
Required: No

 ** namespace **   <a name="codeartifact-Type-PackageDependency-namespace"></a>
The namespace of the package that this package depends on. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** package **   <a name="codeartifact-Type-PackageDependency-package"></a>
 The name of the package that this package depends on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** versionRequirement **   <a name="codeartifact-Type-PackageDependency-versionRequirement"></a>
 The required version, or version range, of the package that this package depends on. The version format is specific to the package type. For example, the following are possible valid required versions: `1.2.3`, `^2.3.4`, or `4.x`.
Type: String
Required: No

## See Also
<a name="API_PackageDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageDependency)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
