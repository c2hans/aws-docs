---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewErrorInfo.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DataViewErrorInfo
<a name="API_DataViewErrorInfo"></a>

The structure with error messages.

## Contents
<a name="API_DataViewErrorInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** errorCategory **   <a name="finspace-Type-DataViewErrorInfo-errorCategory"></a>
The category of the error.
+  `VALIDATION` – The inputs to this request are invalid.
+  `SERVICE_QUOTA_EXCEEDED` – Service quotas have been exceeded. Please contact AWS support to increase quotas.
+  `ACCESS_DENIED` – Missing required permission to perform this request.
+  `RESOURCE_NOT_FOUND` – One or more inputs to this request were not found.
+  `THROTTLING` – The system temporarily lacks sufficient resources to process the request.
+  `INTERNAL_SERVICE_EXCEPTION` – An internal service error has occurred.
+  `CANCELLED` – Cancelled.
+  `USER_RECOVERABLE` – A user recoverable error has occurred.
Type: String
Valid Values: `VALIDATION | SERVICE_QUOTA_EXCEEDED | ACCESS_DENIED | RESOURCE_NOT_FOUND | THROTTLING | INTERNAL_SERVICE_EXCEPTION | CANCELLED | USER_RECOVERABLE`
Required: No

 ** errorMessage **   <a name="finspace-Type-DataViewErrorInfo-errorMessage"></a>
The text of the error message.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

## See Also
<a name="API_DataViewErrorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DataViewErrorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DataViewErrorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DataViewErrorInfo)
