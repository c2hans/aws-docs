---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CodeArtifact.html
---

# CodeArtifact
<a name="API_CodeArtifact"></a>

Contains the location of the code artifact for a MicroVM image.

## Contents
<a name="API_CodeArtifact_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** uri **   <a name="lambdamicrovm-Type-CodeArtifact-uri"></a>
The URI of the code artifact in Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

## See Also
<a name="API_CodeArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/CodeArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/CodeArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/CodeArtifact)
