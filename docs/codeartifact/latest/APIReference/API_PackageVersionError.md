---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionError.html
---

# PackageVersionError
<a name="API_PackageVersionError"></a>

l An error associated with package.

## Contents
<a name="API_PackageVersionError_Contents"></a>

 ** errorCode **   <a name="codeartifact-Type-PackageVersionError-errorCode"></a>
 The error code associated with the error. Valid error codes are:
+  `ALREADY_EXISTS`
+  `MISMATCHED_REVISION`
+  `MISMATCHED_STATUS`
+  `NOT_ALLOWED`
+  `NOT_FOUND`
+  `SKIPPED`
Type: String
Valid Values: `ALREADY_EXISTS | MISMATCHED_REVISION | MISMATCHED_STATUS | NOT_ALLOWED | NOT_FOUND | SKIPPED`
Required: No

 ** errorMessage **   <a name="codeartifact-Type-PackageVersionError-errorMessage"></a>
 The error message associated with the error.
Type: String
Required: No

## See Also
<a name="API_PackageVersionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageVersionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageVersionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageVersionError)
