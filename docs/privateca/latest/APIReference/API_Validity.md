---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html
---

# Validity
<a name="API_Validity"></a>

Validity specifies the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the validity of a certificate starts or expires, or as a span of time after issuance, stated in days, months, or years. For more information, see [Validity](https://tools.ietf.org/html/rfc5280#section-4.1.2.5) in RFC 5280.

 AWS Private CA API consumes the `Validity` data type differently in two distinct parameters of the `IssueCertificate` action. The required parameter `IssueCertificate`:`Validity` specifies the end of a certificate's validity period. The optional parameter `IssueCertificate`:`ValidityNotBefore` specifies a customized starting time for the validity period.

## Contents
<a name="API_Validity_Contents"></a>

 ** Type **   <a name="privateca-Type-Validity-Type"></a>
Determines how * AWS Private CA* interprets the `Value` parameter, an integer. Supported validity types include those listed below. Type definitions with values include a sample input value and the resulting output.
 `END_DATE`: The specific date and time when the certificate will expire, expressed using UTCTime (YYMMDDHHMMSS) or GeneralizedTime (YYYYMMDDHHMMSS) format. When UTCTime is used, if the year field (YY) is greater than or equal to 50, the year is interpreted as 19YY. If the year field is less than 50, the year is interpreted as 20YY.
+ Sample input value: 491231235959 (UTCTime format)
+ Output expiration date/time: 12/31/2049 23:59:59
 `ABSOLUTE`: The specific date and time when the validity of a certificate will start or expire, expressed in seconds since the Unix Epoch.
+ Sample input value: 2524608000
+ Output expiration date/time: 01/01/2050 00:00:00
 `DAYS`, `MONTHS`, `YEARS`: The relative time from the moment of issuance until the certificate will expire, expressed in days, months, or years.
Example if `DAYS`, issued on 10/12/2020 at 12:34:54 UTC:
+ Sample input value: 90
+ Output expiration date: 01/10/2020 12:34:54 UTC
The minimum validity duration for a certificate using relative time (`DAYS`) is one day. The minimum validity for a certificate using absolute time (`ABSOLUTE` or `END_DATE`) is one second.
Type: String
Valid Values: `END_DATE | ABSOLUTE | DAYS | MONTHS | YEARS`
Required: Yes

 ** Value **   <a name="privateca-Type-Validity-Value"></a>
A long integer interpreted according to the value of `Type`, below.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_Validity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/Validity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/Validity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/Validity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
