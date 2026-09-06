---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainEntryPoint.html
---

# DomainEntryPoint
<a name="API_DomainEntryPoint"></a>

Information about how a package originally entered the CodeArtifact domain. For packages published directly to CodeArtifact, the entry point is the repository it was published to. For packages ingested from an external repository, the entry point is the external connection that it was ingested from. An external connection is a CodeArtifact repository that is connected to an external repository such as the npm registry or NuGet gallery.

**Note**
If a package version exists in a repository and is updated, for example if a package of the same version is added with additional assets, the package version's `DomainEntryPoint` will not change from the original package version's value.

## Contents
<a name="API_DomainEntryPoint_Contents"></a>

 ** externalConnectionName **   <a name="codeartifact-Type-DomainEntryPoint-externalConnectionName"></a>
The name of the external connection that a package was ingested from.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-:]{1,99}`
Required: No

 ** repositoryName **   <a name="codeartifact-Type-DomainEntryPoint-repositoryName"></a>
The name of the repository that a package was originally published to.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: No

## See Also
<a name="API_DomainEntryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DomainEntryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DomainEntryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DomainEntryPoint)
