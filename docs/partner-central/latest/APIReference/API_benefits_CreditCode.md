---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CreditCode.html
---

# CreditCode
<a name="API_benefits_CreditCode"></a>

Represents an AWS credit code that can be applied to an AWS account for billing purposes.

## Contents
<a name="API_benefits_CreditCode_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsAccountId **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-AwsAccountId"></a>
The AWS account ID that the credit code is associated with or can be applied to.
Type: String
Required: Yes

 ** AwsCreditCode **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-AwsCreditCode"></a>
The actual credit code string that can be redeemed in the AWS billing console.
Type: String
Required: Yes

 ** ExpiresAt **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-ExpiresAt"></a>
The timestamp when the credit code expires and can no longer be redeemed.
Type: Timestamp
Required: Yes

 ** IssuedAt **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-IssuedAt"></a>
The timestamp when the credit code was issued.
Type: Timestamp
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-Status"></a>
The current status of the credit code (e.g., active, redeemed, expired).
Type: String
Valid Values: `ACTIVE | INACTIVE | FULFILLED`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-benefits_CreditCode-Value"></a>
The monetary value of the credit code.
Type: [MonetaryValue](API_benefits_MonetaryValue.md) object
Required: Yes

## See Also
<a name="API_benefits_CreditCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/CreditCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/CreditCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/CreditCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
