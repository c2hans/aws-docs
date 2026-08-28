---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html
---

# PackageVersionDescription
<a name="API_PackageVersionDescription"></a>

 Details about a package version.

## Contents
<a name="API_PackageVersionDescription_Contents"></a>

 ** displayName **   <a name="codeartifact-Type-PackageVersionDescription-displayName"></a>
 The name of the package that is displayed. The `displayName` varies depending on the package version's format. For example, if an npm package is named `ui`, is in the namespace `vue`, and has the format `npm`, then the `displayName` is `@vue/ui`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** format **   <a name="codeartifact-Type-PackageVersionDescription-format"></a>
 The format of the package version.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: No

 ** homePage **   <a name="codeartifact-Type-PackageVersionDescription-homePage"></a>
 The homepage associated with the package.
Type: String
Required: No

 ** licenses **   <a name="codeartifact-Type-PackageVersionDescription-licenses"></a>
 Information about licenses associated with the package version.
Type: Array of [LicenseInfo](API_LicenseInfo.md) objects
Required: No

 ** namespace **   <a name="codeartifact-Type-PackageVersionDescription-namespace"></a>
The namespace of the package version. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** origin **   <a name="codeartifact-Type-PackageVersionDescription-origin"></a>
A [PackageVersionOrigin](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html) object that contains information about how the package version was added to the repository.
Type: [PackageVersionOrigin](API_PackageVersionOrigin.md) object
Required: No

 ** packageName **   <a name="codeartifact-Type-PackageVersionDescription-packageName"></a>
 The name of the requested package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

 ** publishedTime **   <a name="codeartifact-Type-PackageVersionDescription-publishedTime"></a>
 A timestamp that contains the date and time the package version was published.
Type: Timestamp
Required: No

 ** revision **   <a name="codeartifact-Type-PackageVersionDescription-revision"></a>
 The revision of the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`
Required: No

 ** sourceCodeRepository **   <a name="codeartifact-Type-PackageVersionDescription-sourceCodeRepository"></a>
 The repository for the source code in the package version, or the source code used to build it.
Type: String
Required: No

 ** status **   <a name="codeartifact-Type-PackageVersionDescription-status"></a>
 A string that contains the status of the package version.
Type: String
Valid Values: `Archived | Disposed | Published | Unfinished | Unlisted`
Required: No

 ** summary **   <a name="codeartifact-Type-PackageVersionDescription-summary"></a>
 A summary of the package version. The summary is extracted from the package. The information in and detail level of the summary depends on the package version's format.
Type: String
Required: No

 ** version **   <a name="codeartifact-Type-PackageVersionDescription-version"></a>
 The version of the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

## See Also
<a name="API_PackageVersionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageVersionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageVersionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageVersionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
