---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxSavedownStorageConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxSavedownStorageConfiguration
<a name="API_KxSavedownStorageConfiguration"></a>

The size and type of temporary storage that is used to hold data during the savedown process. All the data written to this storage space is lost when the cluster node is restarted.

## Contents
<a name="API_KxSavedownStorageConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** size **   <a name="finspace-Type-KxSavedownStorageConfiguration-size"></a>
The size of temporary storage in gibibytes.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 16000.
Required: No

 ** type **   <a name="finspace-Type-KxSavedownStorageConfiguration-type"></a>
The type of writeable storage space for temporarily storing your savedown data. The valid values are:
+ SDS01 – This type represents 3000 IOPS and io2 ebs volume type.
Type: String
Valid Values: `SDS01`
Required: No

 ** volumeName **   <a name="finspace-Type-KxSavedownStorageConfiguration-volumeName"></a>
 The name of the kdb volume that you want to use as writeable save-down storage for clusters.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_KxSavedownStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxSavedownStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxSavedownStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxSavedownStorageConfiguration)
