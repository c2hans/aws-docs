---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ReceivedMetadata.html
---

# ReceivedMetadata
<a name="API_ReceivedMetadata"></a>

Metadata associated with received licenses and grants.

## Contents
<a name="API_ReceivedMetadata_Contents"></a>

 ** AllowedOperations **   <a name="licensemanager-Type-ReceivedMetadata-AllowedOperations"></a>
Allowed operations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `CreateGrant | CheckoutLicense | CheckoutBorrowLicense | CheckInLicense | ExtendConsumptionLicense | ListPurchasedLicenses | CreateToken`
Required: No

 ** ReceivedStatus **   <a name="licensemanager-Type-ReceivedMetadata-ReceivedStatus"></a>
Received status.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | DISABLED | WORKFLOW_COMPLETED`
Required: No

 ** ReceivedStatusReason **   <a name="licensemanager-Type-ReceivedMetadata-ReceivedStatusReason"></a>
Received status reason.
Type: String
Length Constraints: Maximum length of 400.
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_ReceivedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ReceivedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ReceivedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ReceivedMetadata)
