---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_S3DataAccessAssetSourceEntry.html
---

# S3DataAccessAssetSourceEntry
<a name="API_S3DataAccessAssetSourceEntry"></a>

Source details for an Amazon S3 data access asset.

## Contents
<a name="API_S3DataAccessAssetSourceEntry_Contents"></a>

 ** Bucket **   <a name="dataexchange-Type-S3DataAccessAssetSourceEntry-Bucket"></a>
The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.
Type: String
Required: Yes

 ** KeyPrefixes **   <a name="dataexchange-Type-S3DataAccessAssetSourceEntry-KeyPrefixes"></a>
Organizes Amazon S3 asset key prefixes stored in an Amazon S3 bucket.
Type: Array of strings
Required: No

 ** Keys **   <a name="dataexchange-Type-S3DataAccessAssetSourceEntry-Keys"></a>
The keys used to create the Amazon S3 data access.
Type: Array of strings
Required: No

 ** KmsKeysToGrant **   <a name="dataexchange-Type-S3DataAccessAssetSourceEntry-KmsKeysToGrant"></a>
List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset.
Type: Array of [KmsKeyToGrant](API_KmsKeyToGrant.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_S3DataAccessAssetSourceEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/S3DataAccessAssetSourceEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/S3DataAccessAssetSourceEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/S3DataAccessAssetSourceEntry)
