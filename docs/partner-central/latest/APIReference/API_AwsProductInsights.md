---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsProductInsights.html
---

# AwsProductInsights
<a name="API_AwsProductInsights"></a>

Comprehensive spend analysis for a single source (AWS or Partner) including total amounts, optimization savings, program category breakdowns, and detailed product-level insights.

## Contents
<a name="API_AwsProductInsights_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsProducts **   <a name="AWSPartnerCentral-Type-AwsProductInsights-AwsProducts"></a>
Product-level details including costs and optimization recommendations.
Type: Array of [AwsProductDetails](API_AwsProductDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** CurrencyCode **   <a name="AWSPartnerCentral-Type-AwsProductInsights-CurrencyCode"></a>
ISO 4217 currency code. Supported values are `USD` and `EUR`. Returns `EUR` when the opportunity is in the `aws-eusc` (AWS European Sovereign Cloud) partition.
Type: String
Valid Values: `USD | EUR | GBP | AUD | CAD | CNY | NZD | INR | JPY | CHF | SEK | AED | AFN | ALL | AMD | ANG | AOA | ARS | AWG | AZN | BAM | BBD | BDT | BGN | BHD | BIF | BMD | BND | BOB | BOV | BRL | BSD | BTN | BWP | BYN | BZD | CDF | CHE | CHW | CLF | CLP | COP | COU | CRC | CUC | CUP | CVE | CZK | DJF | DKK | DOP | DZD | EGP | ERN | ETB | FJD | FKP | GEL | GHS | GIP | GMD | GNF | GTQ | GYD | HKD | HNL | HRK | HTG | HUF | IDR | ILS | IQD | IRR | ISK | JMD | JOD | KES | KGS | KHR | KMF | KPW | KRW | KWD | KYD | KZT | LAK | LBP | LKR | LRD | LSL | LYD | MAD | MDL | MGA | MKD | MMK | MNT | MOP | MRU | MUR | MVR | MWK | MXN | MXV | MYR | MZN | NAD | NGN | NIO | NOK | NPR | OMR | PAB | PEN | PGK | PHP | PKR | PLN | PYG | QAR | RON | RSD | RUB | RWF | SAR | SBD | SCR | SDG | SGD | SHP | SLL | SOS | SRD | SSP | STN | SVC | SYP | SZL | THB | TJS | TMT | TND | TOP | TRY | TTD | TWD | TZS | UAH | UGX | USN | UYI | UYU | UZS | VEF | VND | VUV | WST | XAF | XCD | XDR | XOF | XPF | XSU | XUA | YER | ZAR | ZMW | ZWL`
Required: Yes

 ** Frequency **   <a name="AWSPartnerCentral-Type-AwsProductInsights-Frequency"></a>
Time period for spend amounts.
Type: String
Valid Values: `Monthly`
Required: Yes

 ** TotalAmountByCategory **   <a name="AWSPartnerCentral-Type-AwsProductInsights-TotalAmountByCategory"></a>
Spend amounts mapped to AWS programs and modernization pathways.
Type: String to string map
Value Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: Yes

 ** TotalAmount **   <a name="AWSPartnerCentral-Type-AwsProductInsights-TotalAmount"></a>
Total estimated spend for this source before optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

 ** TotalOptimizedAmount **   <a name="AWSPartnerCentral-Type-AwsProductInsights-TotalOptimizedAmount"></a>
Total estimated spend after applying recommended optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

 ** TotalPotentialSavingsAmount **   <a name="AWSPartnerCentral-Type-AwsProductInsights-TotalPotentialSavingsAmount"></a>
Quantified savings achievable through implementing optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

## See Also
<a name="API_AwsProductInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsProductInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsProductInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsProductInsights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
