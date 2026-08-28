---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FunctionAssociations.html
---

# FunctionAssociations
<a name="API_FunctionAssociations"></a>

A list of CloudFront functions that are associated with a cache behavior in a CloudFront distribution. Your functions must be published to the `LIVE` stage to associate them with a cache behavior.

## Contents
<a name="API_FunctionAssociations_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-FunctionAssociations-Quantity"></a>
The number of CloudFront functions in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-FunctionAssociations-Items"></a>
The CloudFront functions that are associated with a cache behavior in a CloudFront distribution. Your functions must be published to the `LIVE` stage to associate them with a cache behavior.
Type: Array of [FunctionAssociation](API_FunctionAssociation.md) objects
Required: No

## See Also
<a name="API_FunctionAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
