---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchExpectedCustomerSpend.html
---

# OpportunitySearchExpectedCustomerSpend

A curated expected-spend entry: amount and currency only. Frequency and target company are omitted from search results.

## Contents
<a name="API_OpportunitySearchExpectedCustomerSpend_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **   <a name="AWSPartnerCentral-Type-OpportunitySearchExpectedCustomerSpend-CurrencyCode"></a>
The currency of the estimated amount, in ISO 4217 format.
Type: String
Valid Values: `USD | EUR | GBP | AUD | CAD | CNY | NZD | INR | JPY | CHF | SEK | AED | AFN | ALL | AMD | ANG | AOA | ARS | AWG | AZN | BAM | BBD | BDT | BGN | BHD | BIF | BMD | BND | BOB | BOV | BRL | BSD | BTN | BWP | BYN | BZD | CDF | CHE | CHW | CLF | CLP | COP | COU | CRC | CUC | CUP | CVE | CZK | DJF | DKK | DOP | DZD | EGP | ERN | ETB | FJD | FKP | GEL | GHS | GIP | GMD | GNF | GTQ | GYD | HKD | HNL | HRK | HTG | HUF | IDR | ILS | IQD | IRR | ISK | JMD | JOD | KES | KGS | KHR | KMF | KPW | KRW | KWD | KYD | KZT | LAK | LBP | LKR | LRD | LSL | LYD | MAD | MDL | MGA | MKD | MMK | MNT | MOP | MRU | MUR | MVR | MWK | MXN | MXV | MYR | MZN | NAD | NGN | NIO | NOK | NPR | OMR | PAB | PEN | PGK | PHP | PKR | PLN | PYG | QAR | RON | RSD | RUB | RWF | SAR | SBD | SCR | SDG | SGD | SHP | SLL | SOS | SRD | SSP | STN | SVC | SYP | SZL | THB | TJS | TMT | TND | TOP | TRY | TTD | TWD | TZS | UAH | UGX | USN | UYI | UYU | UZS | VEF | VND | VUV | WST | XAF | XCD | XDR | XOF | XPF | XSU | XUA | YER | ZAR | ZMW | ZWL`
Required: Yes

 ** Amount **   <a name="AWSPartnerCentral-Type-OpportunitySearchExpectedCustomerSpend-Amount"></a>
The estimated monthly recurring revenue amount.
Type: String
Pattern: `((0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?)?`
Required: No

## See Also
<a name="API_OpportunitySearchExpectedCustomerSpend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchExpectedCustomerSpend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchExpectedCustomerSpend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchExpectedCustomerSpend)
