---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountSummary.html
---

# CustomerAccountSummary

A customer account in the results of `SearchCustomerAccounts`. It carries a reduced set of fields compared to the full account that is returned by `GetCustomerAccount`.

## Contents
<a name="API_CustomerAccountSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-Arn"></a>
The Amazon Resource Name (ARN) of the customer account.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account/cust-acc-[0-9a-z]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-Catalog"></a>
The catalog that the customer account belongs to.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-CreatedDate"></a>
The date and time when the customer account was created.
Type: Timestamp
Required: Yes

 ** CustomerAccount **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-CustomerAccount"></a>
A summary of the details of the customer that you provided.
Type: [CustomerAccountDetailsSummary](API_CustomerAccountDetailsSummary.md) object
Required: Yes

 ** EnrichmentStatus **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-EnrichmentStatus"></a>
The enrichment status of the customer account.
Type: String
Valid Values: `PENDING | ENRICHED | NO_MATCH_FOUND | ACTION_REQUIRED`
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-Id"></a>
The unique identifier of the customer account.
Type: String
Pattern: `cust-acc-[0-9a-z]{13}`
Required: Yes

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-LastModifiedDate"></a>
The date and time when the customer account was last modified.
Type: Timestamp
Required: Yes

 ** AwsEnrichment **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-AwsEnrichment"></a>
A summary of the enrichment information that AWS provides about the customer. Present only when `EnrichmentStatus` is `ENRICHED`.
Type: [AwsEnrichmentSummary](API_AwsEnrichmentSummary.md) object
Required: No

 ** PartnerAccountIdentifier **   <a name="AWSPartnerCentral-Type-CustomerAccountSummary-PartnerAccountIdentifier"></a>
Your own identifier for the customer account, if you provided one.
Type: String
Pattern: `(?s).{0,64}`
Required: No

## See Also
<a name="API_CustomerAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountSummary)
