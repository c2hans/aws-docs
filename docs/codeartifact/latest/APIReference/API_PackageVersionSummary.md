---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html
---

# PackageVersionSummary
<a name="API_PackageVersionSummary"></a>

 Details about a package version, including its status, version, and revision. The [ListPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html) operation returns a list of `PackageVersionSummary` objects.

## Contents
<a name="API_PackageVersionSummary_Contents"></a>

 ** status **   <a name="codeartifact-Type-PackageVersionSummary-status"></a>
 A string that contains the status of the package version. It can be one of the following:
Type: String
Valid Values: `Archived | Disposed | Published | Unfinished | Unlisted`
Required: Yes

 ** version **   <a name="codeartifact-Type-PackageVersionSummary-version"></a>
 Information about a package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** origin **   <a name="codeartifact-Type-PackageVersionSummary-origin"></a>
A [PackageVersionOrigin](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html) object that contains information about how the package version was added to the repository.
Type: [PackageVersionOrigin](API_PackageVersionOrigin.md) object
Required: No

 ** revision **   <a name="codeartifact-Type-PackageVersionSummary-revision"></a>
 The revision associated with a package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`
Required: No

## See Also
<a name="API_PackageVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageVersionSummary)
