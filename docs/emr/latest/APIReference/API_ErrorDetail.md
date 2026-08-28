---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ErrorDetail.html
---

# ErrorDetail
<a name="API_ErrorDetail"></a>

A tuple that provides information about an error that caused a cluster to terminate.

## Contents
<a name="API_ErrorDetail_Contents"></a>

 ** ErrorCode **   <a name="EMR-Type-ErrorDetail-ErrorCode"></a>
The name or code associated with the error.
Type: String
Required: No

 ** ErrorData **   <a name="EMR-Type-ErrorDetail-ErrorData"></a>
A list of key value pairs that provides contextual information about why an error occured.
Type: Array of string to string maps
Required: No

 ** ErrorMessage **   <a name="EMR-Type-ErrorDetail-ErrorMessage"></a>
A message that describes the error.
Type: String
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
