---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ValidAdditionalStorageOptions.html
---

# ValidAdditionalStorageOptions
<a name="API_ValidAdditionalStorageOptions"></a>

Contains the valid options for additional storage volumes for a DB instance.

## Contents
<a name="API_ValidAdditionalStorageOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SupportsAdditionalStorageVolumes **
Indicates whether the DB instance supports additional storage volumes.
Type: Boolean
Required: No

 ** Volumes.member.N **
The valid additional storage volume options for the DB instance.
Type: Array of [ValidVolumeOptions](API_ValidVolumeOptions.md) objects
Required: No

## See Also
<a name="API_ValidAdditionalStorageOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ValidAdditionalStorageOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ValidAdditionalStorageOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ValidAdditionalStorageOptions)
