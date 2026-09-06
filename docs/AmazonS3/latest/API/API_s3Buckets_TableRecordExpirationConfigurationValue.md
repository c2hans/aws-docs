---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationConfigurationValue.html
---

# TableRecordExpirationConfigurationValue
<a name="API_s3Buckets_TableRecordExpirationConfigurationValue"></a>

The expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is enabled, records expire and are automatically removed after the number of days specified in the record expiration settings for the table.

## Contents
<a name="API_s3Buckets_TableRecordExpirationConfigurationValue_Contents"></a>

 ** settings **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationConfigurationValue-settings"></a>
The expiration settings for records in the table.
Type: [TableRecordExpirationSettings](API_s3Buckets_TableRecordExpirationSettings.md) object
Required: No

 ** status **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationConfigurationValue-status"></a>
The status of the expiration settings for records in the table.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_s3Buckets_TableRecordExpirationConfigurationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableRecordExpirationConfigurationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableRecordExpirationConfigurationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableRecordExpirationConfigurationValue)
