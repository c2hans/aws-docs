---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ShipmentInformation.html
---

# ShipmentInformation
<a name="API_ShipmentInformation"></a>

 Information about a line item shipment.

## Contents
<a name="API_ShipmentInformation_Contents"></a>

 ** ShipmentCarrier **   <a name="outposts-Type-ShipmentInformation-ShipmentCarrier"></a>
 The carrier of the shipment.
Type: String
Valid Values: `DHL | DBS | FEDEX | UPS | EXPEDITORS`
Required: No

 ** ShipmentTrackingNumber **   <a name="outposts-Type-ShipmentInformation-ShipmentTrackingNumber"></a>
 The tracking number of the shipment.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 42.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

## See Also
<a name="API_ShipmentInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ShipmentInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ShipmentInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ShipmentInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
