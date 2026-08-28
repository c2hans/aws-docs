---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LayersListItem.html
---

# LayersListItem
<a name="API_LayersListItem"></a>

Details about an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Contents
<a name="API_LayersListItem_Contents"></a>

 ** LatestMatchingVersion **   <a name="lambda-Type-LayersListItem-LatestMatchingVersion"></a>
The newest version of the layer.
Type: [LayerVersionsListItem](API_LayerVersionsListItem.md) object
Required: No

 ** LayerArn **   <a name="lambda-Type-LayersListItem-LayerArn"></a>
The Amazon Resource Name (ARN) of the function layer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+`
Required: No

 ** LayerName **   <a name="lambda-Type-LayersListItem-LayerName"></a>
The name of the layer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: No

## See Also
<a name="API_LayersListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LayersListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LayersListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LayersListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
