---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxNAS1Configuration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxNAS1Configuration
<a name="API_KxNAS1Configuration"></a>

 The structure containing the size and type of the network attached storage (NAS\_1) file system volume.

## Contents
<a name="API_KxNAS1Configuration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** size **   <a name="finspace-Type-KxNAS1Configuration-size"></a>
 The size of the network attached storage. For storage type `SSD_1000` and `SSD_250` you can select the minimum size as 1200 GB or increments of 2400 GB. For storage type `HDD_12` you can select the minimum size as 6000 GB or increments of 6000 GB.
Type: Integer
Valid Range: Minimum value of 1200.
Required: No

 ** type **   <a name="finspace-Type-KxNAS1Configuration-type"></a>
 The type of the network attached storage.
Type: String
Valid Values: `SSD_1000 | SSD_250 | HDD_12`
Required: No

## See Also
<a name="API_KxNAS1Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxNAS1Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxNAS1Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxNAS1Configuration)
