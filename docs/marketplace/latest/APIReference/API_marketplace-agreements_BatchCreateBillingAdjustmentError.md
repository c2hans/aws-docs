---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BatchCreateBillingAdjustmentError.html
---

# BatchCreateBillingAdjustmentError
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentError"></a>

An error for a billing adjustment request entry that failed validation.

## Contents
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clientToken **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentError-clientToken"></a>
The client token of the request entry that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** code **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentError-code"></a>
The error code indicating the reason for failure.
Type: String
Valid Values: `CONFLICT_EXCEPTION | VALIDATION_EXCEPTION | RESOURCE_NOT_FOUND_EXCEPTION | INTERNAL_FAILURE`
Required: Yes

 ** message **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentError-message"></a>
A human-readable message describing the error.
Type: String
Required: Yes

## See Also
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentError)
