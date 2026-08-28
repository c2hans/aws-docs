---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Offering.html
---

# Offering
<a name="API_Offering"></a>

 A savings plan that reserves a certain amount of outbound bandwidth usage at a discounted rate each month over a period of time.

## Contents
<a name="API_Offering_Contents"></a>

 ** currencyCode **   <a name="mediaconnect-Type-Offering-currencyCode"></a>
 The type of currency that is used for billing. The currencyCode used for all reservations is US dollars.
Type: String
Required: Yes

 ** duration **   <a name="mediaconnect-Type-Offering-duration"></a>
 The length of time that your reservation would be active.
Type: Integer
Required: Yes

 ** durationUnits **   <a name="mediaconnect-Type-Offering-durationUnits"></a>
 The unit of measurement for the duration of the offering.
Type: String
Valid Values: `MONTHS`
Required: Yes

 ** offeringArn **   <a name="mediaconnect-Type-Offering-offeringArn"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.
Type: String
Required: Yes

 ** offeringDescription **   <a name="mediaconnect-Type-Offering-offeringDescription"></a>
 A description of the offering.
Type: String
Required: Yes

 ** pricePerUnit **   <a name="mediaconnect-Type-Offering-pricePerUnit"></a>
 The cost of a single unit. This value, in combination with priceUnits, makes up the rate.
Type: String
Required: Yes

 ** priceUnits **   <a name="mediaconnect-Type-Offering-priceUnits"></a>
 The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate.
Type: String
Valid Values: `HOURLY`
Required: Yes

 ** resourceSpecification **   <a name="mediaconnect-Type-Offering-resourceSpecification"></a>
 A definition of the amount of outbound bandwidth that you would be reserving if you purchase the offering.
Type: [ResourceSpecification](API_ResourceSpecification.md) object
Required: Yes

## See Also
<a name="API_Offering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Offering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Offering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Offering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
