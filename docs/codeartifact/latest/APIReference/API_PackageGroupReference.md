---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupReference.html
---

# PackageGroupReference
<a name="API_PackageGroupReference"></a>

Information about the identifiers of a package group.

## Contents
<a name="API_PackageGroupReference_Contents"></a>

 ** arn **   <a name="codeartifact-Type-PackageGroupReference-arn"></a>
 The ARN of the package group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** pattern **   <a name="codeartifact-Type-PackageGroupReference-pattern"></a>
 The pattern of the package group. The pattern determines which packages are associated with the package group, and is also the identifier of the package group.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 520.
Pattern: `[^\p{C}\p{IsWhitespace}]+`
Required: No

## See Also
<a name="API_PackageGroupReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageGroupReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageGroupReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageGroupReference)
