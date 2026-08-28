---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3DataAccessAsset.html
---

# S3DataAccessAsset
<a name="API_S3DataAccessAsset"></a>

The Amazon S3 data access that is the asset.

## Contents
<a name="API_S3DataAccessAsset_Contents"></a>

 ** Bucket **   <a name="dataexchange-Type-S3DataAccessAsset-Bucket"></a>
The Amazon S3 bucket hosting data to be shared in the S3 data access.
Type: String
Required: Yes

 ** KeyPrefixes **   <a name="dataexchange-Type-S3DataAccessAsset-KeyPrefixes"></a>
The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.
Type: Array of strings
Required: No

 ** Keys **   <a name="dataexchange-Type-S3DataAccessAsset-Keys"></a>
S3 keys made available using this asset.
Type: Array of strings
Required: No

 ** KmsKeysToGrant **   <a name="dataexchange-Type-S3DataAccessAsset-KmsKeysToGrant"></a>
 List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset. Providers must include all AWS KMS keys used to encrypt these shared S3 objects.
Type: Array of [KmsKeyToGrant](API_KmsKeyToGrant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** S3AccessPointAlias **   <a name="dataexchange-Type-S3DataAccessAsset-S3AccessPointAlias"></a>
The automatically-generated bucket-style alias for your Amazon S3 Access Point. Customers can access their entitled data using the S3 Access Point alias.
Type: String
Required: No

 ** S3AccessPointArn **   <a name="dataexchange-Type-S3DataAccessAsset-S3AccessPointArn"></a>
The ARN for your Amazon S3 Access Point. Customers can also access their entitled data using the S3 Access Point ARN.
Type: String
Required: No

## See Also
<a name="API_S3DataAccessAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/S3DataAccessAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/S3DataAccessAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/S3DataAccessAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
