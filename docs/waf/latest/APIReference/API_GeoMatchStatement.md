---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchStatement.html
---

# GeoMatchStatement
<a name="API_GeoMatchStatement"></a>

A rule statement that labels web requests by country and region and that matches against web requests based on country code. A geo match rule labels every request that it inspects regardless of whether it finds a match.
+ To manage requests only by country, you can use this statement by itself and specify the countries that you want to match against in the `CountryCodes` array.
+ Otherwise, configure your geo match rule with Count action so that it only labels requests. Then, add one or more label match rules to run after the geo match rule and configure them to match against the geographic labels and handle the requests as needed.

 AWS WAF labels requests using the alpha-2 country and region codes from the International Organization for Standardization (ISO) 3166 standard. AWS WAF determines the codes using either the IP address in the web request origin or, if you specify it, the address in the geo match `ForwardedIPConfig`.

If you use the web request origin, the label formats are `awswaf:clientip:geo:region:<ISO country code>-<ISO region code>` and `awswaf:clientip:geo:country:<ISO country code>`.

If you use a forwarded IP address, the label formats are `awswaf:forwardedip:geo:region:<ISO country code>-<ISO region code>` and `awswaf:forwardedip:geo:country:<ISO country code>`.

For additional details, see [Geographic match rule statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-geo-match.html) in the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

## Contents
<a name="API_GeoMatchStatement_Contents"></a>

 ** CountryCodes **   <a name="WAF-Type-GeoMatchStatement-CountryCodes"></a>
An array of two-character country codes that you want to match against, for example, `[ "US", "CN" ]`, from the alpha-2 country ISO codes of the ISO 3166 international standard.
When you use a geo match statement just for the region and country labels that it adds to requests, you still have to supply a country code for the rule to evaluate. In this case, you configure the rule to only count matching requests, but it will still generate logging and count metrics for any matches. You can reduce the logging and metrics that the rule produces by specifying a country that's unlikely to be a source of traffic to your site.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `AF | AX | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BQ | BA | BW | BV | BR | IO | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CG | CD | CK | CR | CI | HR | CU | CW | CY | CZ | DK | DJ | DM | DO | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | GF | PF | TF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GP | GU | GT | GG | GN | GW | GY | HT | HM | VA | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | JM | JP | JE | JO | KZ | KE | KI | KP | KR | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MQ | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | NC | NZ | NI | NE | NG | NU | NF | MP | NO | OM | PK | PW | PS | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | GS | SS | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TL | TG | TK | TO | TT | TN | TR | TM | TC | TV | UG | UA | AE | GB | US | UM | UY | UZ | VU | VE | VN | VG | VI | WF | EH | YE | ZM | ZW | XK`
Required: No

 ** ForwardedIPConfig **   <a name="WAF-Type-GeoMatchStatement-ForwardedIPConfig"></a>
The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
Type: [ForwardedIPConfig](API_ForwardedIPConfig.md) object
Required: No

## See Also
<a name="API_GeoMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GeoMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GeoMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GeoMatchStatement)
