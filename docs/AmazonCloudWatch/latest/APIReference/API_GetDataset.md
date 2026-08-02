---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDataset.html
---

# GetDataset
<a name="API_GetDataset"></a>

Returns information about the specified dataset. This includes its identifier, Amazon Resource Name (ARN), and any customer managed AWS Key Management Service (AWS KMS) key that is currently associated with it.

Only the `default` dataset is supported. The `default` dataset is implicit for every account in every Region — you can call `GetDataset` for it without first creating it. If no customer managed KMS key has been associated with the dataset, the response omits the `KmsKeyArn` field, indicating that data is encrypted at rest using an AWS owned key managed by Amazon CloudWatch.

To associate a customer managed KMS key with a dataset, use [AssociateDatasetKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AssociateDatasetKmsKey.html). To remove the association, use [DisassociateDatasetKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisassociateDatasetKmsKey.html).

## Request Parameters
<a name="API_GetDataset_RequestParameters"></a>

 ** DatasetIdentifier **
Specifies the identifier of the dataset to retrieve. For the `default` dataset, you can specify either `default` or the full dataset Amazon Resource Name (ARN) in the format `arn:aws:cloudwatch:Region:account-id:dataset/default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(default|arn:[a-zA-Z0-9-]+:cloudwatch:[a-zA-Z0-9-]*:\d{12}:dataset/default)`
Required: Yes

## Response Elements
<a name="API_GetDataset_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
Returns the Amazon Resource Name (ARN) of the dataset, in the format `arn:aws:cloudwatch:Region:account-id:dataset/dataset-id `.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:cloudwatch:[a-zA-Z0-9-]*:\d{12}:dataset/default`

 ** DatasetId **
Returns the identifier of the dataset.
Type: String
Length Constraints: Fixed length of 7.
Pattern: `default`

 ** KmsKeyArn **
Returns the Amazon Resource Name (ARN) of the customer managed AWS KMS key that is currently associated with the dataset, if any. If the dataset is not associated with a customer managed KMS key, this field is not included in the response and the dataset is encrypted at rest using an AWS owned key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:kms:[a-zA-Z0-9-]+:\d{12}:key/[a-f0-9-]+`

## Errors
<a name="API_GetDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_GetDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDataset)
