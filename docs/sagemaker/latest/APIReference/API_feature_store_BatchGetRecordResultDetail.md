---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecordResultDetail.html
---

# BatchGetRecordResultDetail
<a name="API_feature_store_BatchGetRecordResultDetail"></a>

The output of records that have been retrieved in a batch.

## Contents
<a name="API_feature_store_BatchGetRecordResultDetail_Contents"></a>

 ** FeatureGroupName **   <a name="sagemaker-Type-feature_store_BatchGetRecordResultDetail-FeatureGroupName"></a>
The `FeatureGroupName` containing Records you retrieved in a batch.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** Record **   <a name="sagemaker-Type-feature_store_BatchGetRecordResultDetail-Record"></a>
The `Record` retrieved.
Type: Array of [FeatureValue](API_feature_store_FeatureValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** RecordIdentifierValueAsString **   <a name="sagemaker-Type-feature_store_BatchGetRecordResultDetail-RecordIdentifierValueAsString"></a>
The value of the record identifier in string format.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** ExpiresAt **   <a name="sagemaker-Type-feature_store_BatchGetRecordResultDetail-ExpiresAt"></a>
The `ExpiresAt` ISO string of the requested record.
Type: String
Required: No

## See Also
<a name="API_feature_store_BatchGetRecordResultDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordResultDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordResultDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordResultDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
