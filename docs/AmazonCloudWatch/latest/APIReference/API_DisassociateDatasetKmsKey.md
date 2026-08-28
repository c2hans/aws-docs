---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisassociateDatasetKmsKey.html
---

# DisassociateDatasetKmsKey
<a name="API_DisassociateDatasetKmsKey"></a>

Removes the customer managed AWS Key Management Service (AWS KMS) key association from the specified dataset. After this operation completes, data that you publish to the dataset is encrypted at rest using an AWS owned key managed by Amazon CloudWatch.

Only the `default` dataset is supported. To call this operation, the dataset must currently have a customer managed KMS key associated with it. If the dataset has no associated KMS key, the operation fails with `ResourceNotFoundException`.

Amazon CloudWatch performs a dry-run `kms:Decrypt` call on the currently associated key as part of this operation. The caller must have `kms:Decrypt` permission on the currently associated key. If the key is accessible but the caller lacks `kms:Decrypt` permission, the operation fails with `AccessDeniedException`.

**Note**
If the currently associated key has been deleted, is scheduled for deletion, is pending import, is unavailable, or has been disabled, Amazon CloudWatch does not require `kms:Decrypt` permission on that key and the disassociation proceeds. If the key was only disabled, consider re-enabling it instead of disassociating, because re-enabling allows Amazon CloudWatch to resume decrypting your existing metric data.

**Important**
Disassociating a KMS key from a dataset does not immediately remove the `kms:Decrypt` requirement on data plane operations. For up to three hours after disassociation, callers must continue to have `kms:Decrypt` permission on the previously associated key. Some data might still be encrypted with that key during this window. After this enforcement window elapses, the `kms:Decrypt` requirement is lifted.

For more information about using customer managed keys with Amazon CloudWatch, see [Encryption at rest with customer managed keys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cmk-encryption.html) in the *Amazon CloudWatch User Guide*.

## Request Parameters
<a name="API_DisassociateDatasetKmsKey_RequestParameters"></a>

 ** DatasetIdentifier **
Specifies the identifier of the dataset from which to remove the KMS key association. For the `default` dataset, you can specify either `default` or the full dataset Amazon Resource Name (ARN) in the format `arn:aws:cloudwatch:Region:account-id:dataset/default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(default|arn:[a-zA-Z0-9-]+:cloudwatch:[a-zA-Z0-9-]*:\d{12}:dataset/default)`
Required: Yes

## Errors
<a name="API_DisassociateDatasetKmsKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_DisassociateDatasetKmsKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DisassociateDatasetKmsKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DisassociateDatasetKmsKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
