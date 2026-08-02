---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupDescription.html
---

# BackupDescription
<a name="API_BackupDescription"></a>

Contains the description of the backup created for the table.

## Contents
<a name="API_BackupDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BackupDetails **   <a name="DDB-Type-BackupDescription-BackupDetails"></a>
Contains the details of the backup created for the table.
Type: [BackupDetails](API_BackupDetails.md) object
Required: No

 ** SourceTableDetails **   <a name="DDB-Type-BackupDescription-SourceTableDetails"></a>
Contains the details of the table when the backup was created.
Type: [SourceTableDetails](API_SourceTableDetails.md) object
Required: No

 ** SourceTableFeatureDetails **   <a name="DDB-Type-BackupDescription-SourceTableFeatureDetails"></a>
Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.
Type: [SourceTableFeatureDetails](API_SourceTableFeatureDetails.md) object
Required: No

## See Also
<a name="API_BackupDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BackupDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BackupDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BackupDescription)
