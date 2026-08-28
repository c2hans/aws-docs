---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecordIdentifier.html
---

# BatchGetRecordIdentifier
<a name="API_feature_store_BatchGetRecordIdentifier"></a>

The identifier that identifies the batch of Records you are retrieving in a batch.

## Contents
<a name="API_feature_store_BatchGetRecordIdentifier_Contents"></a>

 ** FeatureGroupName **   <a name="sagemaker-Type-feature_store_BatchGetRecordIdentifier-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the `FeatureGroup` containing the records you are retrieving in a batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/)?([a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** RecordIdentifiersValueAsString **   <a name="sagemaker-Type-feature_store_BatchGetRecordIdentifier-RecordIdentifiersValueAsString"></a>
The value for a list of record identifiers in string format.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: Yes

 ** FeatureNames **   <a name="sagemaker-Type-feature_store_BatchGetRecordIdentifier-FeatureNames"></a>
List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: No

## See Also
<a name="API_feature_store_BatchGetRecordIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecordIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
