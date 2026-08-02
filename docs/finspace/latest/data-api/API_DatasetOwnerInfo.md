---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DatasetOwnerInfo.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DatasetOwnerInfo
<a name="API_DatasetOwnerInfo"></a>

A structure for Dataset owner info.

## Contents
<a name="API_DatasetOwnerInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** email **   <a name="finspace-Type-DatasetOwnerInfo-email"></a>
Email address for the Dataset owner.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 320.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}`
Required: No

 ** name **   <a name="finspace-Type-DatasetOwnerInfo-name"></a>
The name of the Dataset owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `.*\S.*`
Required: No

 ** phoneNumber **   <a name="finspace-Type-DatasetOwnerInfo-phoneNumber"></a>
Phone number for the Dataset owner.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `^[\+0-9\#\,\(][\+0-9\-\.\/\(\)\,\#\s]+$`
Required: No

## See Also
<a name="API_DatasetOwnerInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DatasetOwnerInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DatasetOwnerInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DatasetOwnerInfo)
