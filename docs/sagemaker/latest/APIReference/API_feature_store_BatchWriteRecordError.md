---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecordError.html
---

# BatchWriteRecordError
<a name="API_feature_store_BatchWriteRecordError"></a>

The error that has occurred when attempting to write a record in a batch.

## Contents
<a name="API_feature_store_BatchWriteRecordError_Contents"></a>

 ** Entry **   <a name="sagemaker-Type-feature_store_BatchWriteRecordError-Entry"></a>
The entry that failed to be written.
Type: [BatchWriteRecordEntry](API_feature_store_BatchWriteRecordEntry.md) object
Required: Yes

 ** ErrorCode **   <a name="sagemaker-Type-feature_store_BatchWriteRecordError-ErrorCode"></a>
The error code for the failed record write.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** ErrorMessage **   <a name="sagemaker-Type-feature_store_BatchWriteRecordError-ErrorMessage"></a>
The error message for the failed record write.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

## See Also
<a name="API_feature_store_BatchWriteRecordError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchWriteRecordError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
