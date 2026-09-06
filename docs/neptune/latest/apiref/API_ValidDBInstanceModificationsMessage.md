---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ValidDBInstanceModificationsMessage.html
---

# ValidDBInstanceModificationsMessage
<a name="API_ValidDBInstanceModificationsMessage"></a>

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the [DescribeValidDBInstanceModifications](API_DescribeValidDBInstanceModifications.md) action. You can use this information when you call [ModifyDBInstance](API_ModifyDBInstance.md).

## Contents
<a name="API_ValidDBInstanceModificationsMessage_Contents"></a>

 ** Storage.ValidStorageOptions.N **
Valid storage options for your DB instance.
Type: Array of [ValidStorageOptions](API_ValidStorageOptions.md) objects
Required: No

## See Also
<a name="API_ValidDBInstanceModificationsMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ValidDBInstanceModificationsMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ValidDBInstanceModificationsMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ValidDBInstanceModificationsMessage)
