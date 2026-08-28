---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_SampleDocuments.html
---

# SampleDocuments
<a name="API_SampleDocuments"></a>

Describes a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

## Contents
<a name="API_SampleDocuments_Contents"></a>

 ** bucketName **   <a name="b2bi-Type-SampleDocuments-bucketName"></a>
Contains the Amazon S3 bucket that is used to hold your sample documents.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** keys **   <a name="b2bi-Type-SampleDocuments-keys"></a>
Contains an array of the Amazon S3 keys used to identify the location for your sample documents.
Type: Array of [SampleDocumentKeys](API_SampleDocumentKeys.md) objects
Required: Yes

## See Also
<a name="API_SampleDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/SampleDocuments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/SampleDocuments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/SampleDocuments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
