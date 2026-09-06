---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ValidDBInstanceModificationsMessage.html
---

# ValidDBInstanceModificationsMessage
<a name="API_ValidDBInstanceModificationsMessage"></a>

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the `DescribeValidDBInstanceModifications` action. You can use this information when you call `ModifyDBInstance`.

## Contents
<a name="API_ValidDBInstanceModificationsMessage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalStorage **
The valid additional storage options for the DB instance.
Type: [ValidAdditionalStorageOptions](API_ValidAdditionalStorageOptions.md) object
Required: No

 ** Storage.ValidStorageOptions.N **
Valid storage options for your DB instance.
Type: Array of [ValidStorageOptions](API_ValidStorageOptions.md) objects
Required: No

 ** SupportsDedicatedLogVolume **
Indicates whether a DB instance supports using a dedicated log volume (DLV).
Type: Boolean
Required: No

 ** ValidProcessorFeatures.AvailableProcessorFeature.N **
Valid processor features for your DB instance.
Type: Array of [AvailableProcessorFeature](API_AvailableProcessorFeature.md) objects
Required: No

## See Also
<a name="API_ValidDBInstanceModificationsMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ValidDBInstanceModificationsMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ValidDBInstanceModificationsMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ValidDBInstanceModificationsMessage)
