---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchItemError.html
---

# BatchItemError
<a name="API_BatchItemError"></a>

Describes an error that occurred while processing a document in a batch. The operation returns on `BatchItemError` object for each document that contained an error.

## Contents
<a name="API_BatchItemError_Contents"></a>

 ** ErrorCode **   <a name="comprehend-Type-BatchItemError-ErrorCode"></a>
The numeric error code of the error.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ErrorMessage **   <a name="comprehend-Type-BatchItemError-ErrorMessage"></a>
A text description of the error.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Index **   <a name="comprehend-Type-BatchItemError-Index"></a>
The zero-based index of the document in the input list.
Type: Integer
Required: No

## See Also
<a name="API_BatchItemError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchItemError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchItemError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchItemError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
