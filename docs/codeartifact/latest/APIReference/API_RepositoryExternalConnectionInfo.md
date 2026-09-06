---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositoryExternalConnectionInfo.html
---

# RepositoryExternalConnectionInfo
<a name="API_RepositoryExternalConnectionInfo"></a>

 Contains information about the external connection of a repository.

## Contents
<a name="API_RepositoryExternalConnectionInfo_Contents"></a>

 ** externalConnectionName **   <a name="codeartifact-Type-RepositoryExternalConnectionInfo-externalConnectionName"></a>
 The name of the external connection associated with a repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-:]{1,99}`
Required: No

 ** packageFormat **   <a name="codeartifact-Type-RepositoryExternalConnectionInfo-packageFormat"></a>
 The package format associated with a repository's external connection. The valid package formats are:
+  `npm`: A Node Package Manager (npm) package.
+  `pypi`: A Python Package Index (PyPI) package.
+  `maven`: A Maven package that contains compiled code in a distributable format, such as a JAR file.
+  `nuget`: A NuGet package.
+  `generic`: A generic package.
+  `ruby`: A Ruby package.
+  `swift`: A Swift package.
+  `cargo`: A Cargo package.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: No

 ** status **   <a name="codeartifact-Type-RepositoryExternalConnectionInfo-status"></a>
 The status of the external connection of a repository. There is one valid value, `Available`.
Type: String
Valid Values: `Available`
Required: No

## See Also
<a name="API_RepositoryExternalConnectionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/RepositoryExternalConnectionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/RepositoryExternalConnectionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/RepositoryExternalConnectionInfo)
