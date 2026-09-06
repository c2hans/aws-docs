---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ValidityTerm.html
---

# ValidityTerm
<a name="API_marketplace-agreements_ValidityTerm"></a>

Defines the conditions that will keep an agreement created from this offer valid.

## Contents
<a name="API_marketplace-agreements_ValidityTerm_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementDuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ValidityTerm-agreementDuration"></a>
Defines the duration that the agreement remains active. If `AgreementStartDate` isn’t provided, the agreement duration is relative to the agreement signature time. The duration is represented in the ISO\_8601 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** agreementEndDate **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ValidityTerm-agreementEndDate"></a>
Defines the date when the agreement ends. The agreement ends at 23:59:59.999 UTC on the date provided. If `AgreementEndDate` isn’t provided, the agreement end date is determined by the validity of individual terms.
Type: Timestamp
Required: No

 ** agreementStartDate **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ValidityTerm-agreementStartDate"></a>
Defines the date when agreement starts. The agreement starts at 00:00:00.000 UTC on the date provided. If `AgreementStartDate` isn’t provided, the agreement start date is determined based on agreement signature time.
Type: Timestamp
Required: No

 ** id **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ValidityTerm-id"></a>
The unique identifier for the term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: No

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ValidityTerm-type"></a>
Category of the term being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z]+`
Required: No

## See Also
<a name="API_marketplace-agreements_ValidityTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ValidityTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ValidityTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ValidityTerm)
