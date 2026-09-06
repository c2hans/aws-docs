---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ExpectedCustomerSpend.html
---

# ExpectedCustomerSpend
<a name="API_ExpectedCustomerSpend"></a>

Provides an estimate of the revenue that the partner is expected to generate from the opportunity. This information helps partners assess the financial value of the project.

## Contents
<a name="API_ExpectedCustomerSpend_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **   <a name="AWSPartnerCentral-Type-ExpectedCustomerSpend-CurrencyCode"></a>
Indicates the currency in which the revenue estimate is provided. This helps in understanding the financial impact across different markets. Accepted values are `USD` (US Dollars) and `EUR` (Euros). If the AWS Partition is `aws-eusc` (AWS European Sovereign Cloud), the currency code must be `EUR`.
Type: String
Valid Values: `USD | EUR | GBP | AUD | CAD | CNY | NZD | INR | JPY | CHF | SEK | AED | AFN | ALL | AMD | ANG | AOA | ARS | AWG | AZN | BAM | BBD | BDT | BGN | BHD | BIF | BMD | BND | BOB | BOV | BRL | BSD | BTN | BWP | BYN | BZD | CDF | CHE | CHW | CLF | CLP | COP | COU | CRC | CUC | CUP | CVE | CZK | DJF | DKK | DOP | DZD | EGP | ERN | ETB | FJD | FKP | GEL | GHS | GIP | GMD | GNF | GTQ | GYD | HKD | HNL | HRK | HTG | HUF | IDR | ILS | IQD | IRR | ISK | JMD | JOD | KES | KGS | KHR | KMF | KPW | KRW | KWD | KYD | KZT | LAK | LBP | LKR | LRD | LSL | LYD | MAD | MDL | MGA | MKD | MMK | MNT | MOP | MRU | MUR | MVR | MWK | MXN | MXV | MYR | MZN | NAD | NGN | NIO | NOK | NPR | OMR | PAB | PEN | PGK | PHP | PKR | PLN | PYG | QAR | RON | RSD | RUB | RWF | SAR | SBD | SCR | SDG | SGD | SHP | SLL | SOS | SRD | SSP | STN | SVC | SYP | SZL | THB | TJS | TMT | TND | TOP | TRY | TTD | TWD | TZS | UAH | UGX | USN | UYI | UYU | UZS | VEF | VND | VUV | WST | XAF | XCD | XDR | XOF | XPF | XSU | XUA | YER | ZAR | ZMW | ZWL`
Required: Yes

 ** Frequency **   <a name="AWSPartnerCentral-Type-ExpectedCustomerSpend-Frequency"></a>
Indicates how frequently the customer is expected to spend the projected amount. Use `Monthly` for recurring monthly spend (required for `TargetCompany: "AWS"` entries). Use `None` for one-time deal value entries (required for `TargetCompany: "Self"` entries when providing Total Contract Value).
Type: String
Valid Values: `Monthly`
Required: Yes

 ** TargetCompany **   <a name="AWSPartnerCentral-Type-ExpectedCustomerSpend-TargetCompany"></a>
Specifies the entity associated with this spend entry. Use `AWS` for the system’s AWS Monthly Recurring Revenue (MRR) estimate. Use `Self` for the partner’s own deal value entry when providing Total Contract Value (TCV) for automatic MRR conversion. When `ExpectedContractDuration` is present on the Project, only `AWS` and `Self` are accepted. When `ExpectedContractDuration` is not present, only `AWS` is accepted and any other value will be automatically set to `AWS`.
Type: String
Pattern: `(?s).{1,80}`
Required: Yes

 ** Amount **   <a name="AWSPartnerCentral-Type-ExpectedCustomerSpend-Amount"></a>
Represents the estimated monthly revenue that the partner expects to earn from the opportunity. This helps in forecasting financial returns.
Type: String
Pattern: `((0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?)?`
Required: No

 ** EstimationUrl **   <a name="AWSPartnerCentral-Type-ExpectedCustomerSpend-EstimationUrl"></a>
A URL providing additional information or context about the spend estimation.
Type: String
Pattern: `https://(calculator\.aws|pricing\.calculator\.aws\.eu)/#/estimate\?id=[a-f0-9]{32,64}`
Required: No

## See Also
<a name="API_ExpectedCustomerSpend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ExpectedCustomerSpend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ExpectedCustomerSpend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ExpectedCustomerSpend)
