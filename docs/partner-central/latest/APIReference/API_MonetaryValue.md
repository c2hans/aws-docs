---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_MonetaryValue.html
---

# MonetaryValue
<a name="API_MonetaryValue"></a>

Specifies payments details.

## Contents
<a name="API_MonetaryValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Amount **   <a name="AWSPartnerCentral-Type-MonetaryValue-Amount"></a>
Specifies the payment amount.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: Yes

 ** CurrencyCode **   <a name="AWSPartnerCentral-Type-MonetaryValue-CurrencyCode"></a>
Specifies the payment currency. Accepted values are `USD` (US Dollars) and `EUR` (Euros). If the AWS Partition is `aws-eusc` (AWS European Sovereign Cloud), the currency code must be `EUR`.
Type: String
Valid Values: `USD | EUR | GBP | AUD | CAD | CNY | NZD | INR | JPY | CHF | SEK | AED | AFN | ALL | AMD | ANG | AOA | ARS | AWG | AZN | BAM | BBD | BDT | BGN | BHD | BIF | BMD | BND | BOB | BOV | BRL | BSD | BTN | BWP | BYN | BZD | CDF | CHE | CHW | CLF | CLP | COP | COU | CRC | CUC | CUP | CVE | CZK | DJF | DKK | DOP | DZD | EGP | ERN | ETB | FJD | FKP | GEL | GHS | GIP | GMD | GNF | GTQ | GYD | HKD | HNL | HRK | HTG | HUF | IDR | ILS | IQD | IRR | ISK | JMD | JOD | KES | KGS | KHR | KMF | KPW | KRW | KWD | KYD | KZT | LAK | LBP | LKR | LRD | LSL | LYD | MAD | MDL | MGA | MKD | MMK | MNT | MOP | MRU | MUR | MVR | MWK | MXN | MXV | MYR | MZN | NAD | NGN | NIO | NOK | NPR | OMR | PAB | PEN | PGK | PHP | PKR | PLN | PYG | QAR | RON | RSD | RUB | RWF | SAR | SBD | SCR | SDG | SGD | SHP | SLL | SOS | SRD | SSP | STN | SVC | SYP | SZL | THB | TJS | TMT | TND | TOP | TRY | TTD | TWD | TZS | UAH | UGX | USN | UYI | UYU | UZS | VEF | VND | VUV | WST | XAF | XCD | XDR | XOF | XPF | XSU | XUA | YER | ZAR | ZMW | ZWL`
Required: Yes

## See Also
<a name="API_MonetaryValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/MonetaryValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/MonetaryValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/MonetaryValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
