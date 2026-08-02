---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecordError.html
---

# BatchGetRecordError
<a name="API_feature_store_BatchGetRecordError"></a>

The error that has occurred when attempting to retrieve a batch of Records.

## Contents
<a name="API_feature_store_BatchGetRecordError_Contents"></a>

 ** ErrorCode **   <a name="sagemaker-Type-feature_store_BatchGetRecordError-ErrorCode"></a>
The error code of an error that has occurred when attempting to retrieve a batch of Records. For more information on errors, see [Errors](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html#API_feature_store_GetRecord_Errors).
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** ErrorMessage **   <a name="sagemaker-Type-feature_store_BatchGetRecordError-ErrorMessage"></a>
The error message of an error that has occurred when attempting to retrieve a record in the batch.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

 ** FeatureGroupName **   <a name="sagemaker-Type-feature_store_BatchGetRecordError-FeatureGroupName"></a>
The name of the feature group that the record belongs to.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** RecordIdentifierValueAsString **   <a name="sagemaker-Type-feature_store_BatchGetRecordError-RecordIdentifierValueAsString"></a>
The value for the `RecordIdentifier` in string format of a Record from a `FeatureGroup` that is causing an error when attempting to be retrieved.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_feature_store_BatchGetRecordError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordError)
