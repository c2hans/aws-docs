---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryS3BucketDestination.html
---

# InventoryS3BucketDestination
<a name="API_InventoryS3BucketDestination"></a>

Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where S3 Inventory results are published.

## Contents
<a name="API_InventoryS3BucketDestination_Contents"></a>

 ** Bucket **   <a name="AmazonS3-Type-InventoryS3BucketDestination-Bucket"></a>
The Amazon Resource Name (ARN) of the bucket where inventory results will be published.
Type: String
Required: Yes

 ** Format **   <a name="AmazonS3-Type-InventoryS3BucketDestination-Format"></a>
Specifies the output format of the inventory results.
Type: String
Valid Values: `CSV | ORC | Parquet`
Required: Yes

 ** AccountId **   <a name="AmazonS3-Type-InventoryS3BucketDestination-AccountId"></a>
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.
 Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.
Type: String
Required: No

 ** Encryption **   <a name="AmazonS3-Type-InventoryS3BucketDestination-Encryption"></a>
Contains the type of server-side encryption used to encrypt the inventory results.
Type: [InventoryEncryption](API_InventoryEncryption.md) data type
Required: No

 ** Prefix **   <a name="AmazonS3-Type-InventoryS3BucketDestination-Prefix"></a>
The prefix that is prepended to all inventory results.
Type: String
Required: No

## See Also
<a name="API_InventoryS3BucketDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryS3BucketDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryS3BucketDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryS3BucketDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
