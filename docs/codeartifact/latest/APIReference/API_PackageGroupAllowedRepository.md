---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupAllowedRepository.html
---

# PackageGroupAllowedRepository
<a name="API_PackageGroupAllowedRepository"></a>

 Details about an allowed repository for a package group, including its name and origin configuration.

## Contents
<a name="API_PackageGroupAllowedRepository_Contents"></a>

 ** originRestrictionType **   <a name="codeartifact-Type-PackageGroupAllowedRepository-originRestrictionType"></a>
The origin configuration restriction type of the allowed repository.
Type: String
Valid Values: `EXTERNAL_UPSTREAM | INTERNAL_UPSTREAM | PUBLISH`
Required: No

 ** repositoryName **   <a name="codeartifact-Type-PackageGroupAllowedRepository-repositoryName"></a>
 The name of the allowed repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: No

## See Also
<a name="API_PackageGroupAllowedRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageGroupAllowedRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageGroupAllowedRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageGroupAllowedRepository)
