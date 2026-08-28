---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_LambdaFunctionAssociations.html
---

# LambdaFunctionAssociations
<a name="API_LambdaFunctionAssociations"></a>

A complex type that specifies a list of Lambda@Edge functions associations for a cache behavior.

If you want to invoke one or more Lambda@Edge functions triggered by requests that match the `PathPattern` of the cache behavior, specify the applicable values for `Quantity` and `Items`. Note that there can be up to 4 `LambdaFunctionAssociation` items in this list (one for each possible value of `EventType`) and each `EventType` can be associated with only one function.

If you don't want to invoke any Lambda@Edge functions for the requests that match `PathPattern`, specify `0` for `Quantity` and omit `Items`.

## Contents
<a name="API_LambdaFunctionAssociations_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-LambdaFunctionAssociations-Quantity"></a>
The number of Lambda@Edge function associations for this cache behavior.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-LambdaFunctionAssociations-Items"></a>
 **Optional**: A complex type that contains `LambdaFunctionAssociation` items for this cache behavior. If `Quantity` is `0`, you can omit `Items`.
Type: Array of [LambdaFunctionAssociation](API_LambdaFunctionAssociation.md) objects
Required: No

## See Also
<a name="API_LambdaFunctionAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/LambdaFunctionAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/LambdaFunctionAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/LambdaFunctionAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
