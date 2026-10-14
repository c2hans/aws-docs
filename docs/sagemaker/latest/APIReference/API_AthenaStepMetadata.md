---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AthenaStepMetadata.html
---

# AthenaStepMetadata
<a name="API_AthenaStepMetadata"></a>

The query execution identifier and the result output location for the Amazon Athena query that an Athena step runs.

## Contents
<a name="API_AthenaStepMetadata_Contents"></a>

 ** QueryExecutionId **   <a name="sagemaker-Type-AthenaStepMetadata-QueryExecutionId"></a>
The unique identifier of the Amazon Athena query execution that was run by this step execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** S3OutputLocation **   <a name="sagemaker-Type-AthenaStepMetadata-S3OutputLocation"></a>
The Amazon S3 location of the Amazon Athena query results. This is the effective output location reported by `GetQueryExecution` for the query. This value can be absent when the query uses Athena managed query results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_AthenaStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AthenaStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AthenaStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AthenaStepMetadata)
