---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html
---

# PackageVersionOrigin
<a name="API_PackageVersionOrigin"></a>

Information about how a package version was added to a repository.

## Contents
<a name="API_PackageVersionOrigin_Contents"></a>

 ** domainEntryPoint **   <a name="codeartifact-Type-PackageVersionOrigin-domainEntryPoint"></a>
A [DomainEntryPoint](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainEntryPoint.html) object that contains information about from which repository or external connection the package version was added to the domain.
Type: [DomainEntryPoint](API_DomainEntryPoint.md) object
Required: No

 ** originType **   <a name="codeartifact-Type-PackageVersionOrigin-originType"></a>
Describes how the package version was originally added to the domain. An `INTERNAL` origin type means the package version was published directly to a repository in the domain. An `EXTERNAL` origin type means the package version was ingested from an external connection.
Type: String
Valid Values: `INTERNAL | EXTERNAL | UNKNOWN`
Required: No

## See Also
<a name="API_PackageVersionOrigin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageVersionOrigin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageVersionOrigin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageVersionOrigin)
