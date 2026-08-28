---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_QuoteSpecification.html
---

# QuoteSpecification
<a name="API_QuoteSpecification"></a>

A physical specification for a quote option. Describes the rack or server configuration that would be deployed.

## Contents
<a name="API_QuoteSpecification_Contents"></a>

 ** ExistingRackSpecificationDetails **   <a name="outposts-Type-QuoteSpecification-ExistingRackSpecificationDetails"></a>
The existing rack specification details, if the specification type is `UPDATED_RACK` or `EXISTING_RACK`.
Type: [RackSpecificationDetails](API_RackSpecificationDetails.md) object
Required: No

 ** FinalRackSpecificationDetails **   <a name="outposts-Type-QuoteSpecification-FinalRackSpecificationDetails"></a>
The final rack specification details after the quote is fulfilled.
Type: [RackSpecificationDetails](API_RackSpecificationDetails.md) object
Required: No

 ** QuoteSpecificationType **   <a name="outposts-Type-QuoteSpecification-QuoteSpecificationType"></a>
The type of specification. Valid values are `NEW_RACK`, `UPDATED_RACK`, `EXISTING_RACK`, and `SERVER`.
Type: String
Valid Values: `UPDATED_RACK | NEW_RACK | EXISTING_RACK | SERVER`
Required: No

 ** ServerSpecificationDetails **   <a name="outposts-Type-QuoteSpecification-ServerSpecificationDetails"></a>
The server specification details, if the specification type is `SERVER`.
Type: [ServerSpecificationDetails](API_ServerSpecificationDetails.md) object
Required: No

## See Also
<a name="API_QuoteSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/QuoteSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/QuoteSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/QuoteSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
