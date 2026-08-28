---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItemRequest.html
---

# LineItemRequest
<a name="API_LineItemRequest"></a>

Information about a line item request.

## Contents
<a name="API_LineItemRequest_Contents"></a>

 ** CatalogItemId **   <a name="outposts-Type-LineItemRequest-CatalogItemId"></a>
The ID of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `OR-[A-Z0-9]{7}`
Required: No

 ** Quantity **   <a name="outposts-Type-LineItemRequest-Quantity"></a>
The quantity of a line item request.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_LineItemRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/LineItemRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/LineItemRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/LineItemRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
