---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryEncryption.html
---

# InventoryEncryption
<a name="API_InventoryEncryption"></a>

Contains the type of server-side encryption used to encrypt the S3 Inventory results.

## Contents
<a name="API_InventoryEncryption_Contents"></a>

 ** SSEKMS **   <a name="AmazonS3-Type-InventoryEncryption-SSEKMS"></a>
Specifies the use of SSE-KMS to encrypt delivered inventory reports.
Type: [SSEKMS](API_SSEKMS.md) data type
Required: No

 ** SSES3 **   <a name="AmazonS3-Type-InventoryEncryption-SSES3"></a>
Specifies the use of SSE-S3 to encrypt delivered inventory reports.
Type: [SSES3](API_SSES3.md) data type
Required: No

## See Also
<a name="API_InventoryEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
