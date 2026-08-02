---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSnippetError.html
---

# CodeSnippetError
<a name="API_CodeSnippetError"></a>

Contains information about any errors encountered while trying to retrieve a code snippet.

## Contents
<a name="API_CodeSnippetError_Contents"></a>

 ** errorCode **   <a name="inspector2-Type-CodeSnippetError-errorCode"></a>
The error code for the error that prevented a code snippet from being retrieved.
Type: String
Valid Values: `INTERNAL_ERROR | ACCESS_DENIED | CODE_SNIPPET_NOT_FOUND | INVALID_INPUT`
Required: Yes

 ** errorMessage **   <a name="inspector2-Type-CodeSnippetError-errorMessage"></a>
The error message received when Amazon Inspector failed to retrieve a code snippet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** findingArn **   <a name="inspector2-Type-CodeSnippetError-findingArn"></a>
The ARN of the finding that a code snippet couldn't be retrieved for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: Yes

## See Also
<a name="API_CodeSnippetError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSnippetError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSnippetError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSnippetError)
