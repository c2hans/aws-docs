---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinksItem.html
---

# ListLinksItem
<a name="API_ListLinksItem"></a>

A structure that contains information about one of this source account's links to a monitoring account.

## Contents
<a name="API_ListLinksItem_Contents"></a>

 ** Arn **   <a name="OAM-Type-ListLinksItem-Arn"></a>
The ARN of the link.
Type: String
Required: No

 ** Id **   <a name="OAM-Type-ListLinksItem-Id"></a>
The random ID string that AWS generated as part of the link ARN.
Type: String
Required: No

 ** Label **   <a name="OAM-Type-ListLinksItem-Label"></a>
The label that was assigned to this link at creation, with the variables resolved to their actual values.
Type: String
Required: No

 ** ResourceTypes **   <a name="OAM-Type-ListLinksItem-ResourceTypes"></a>
The resource types supported by this link.
Type: Array of strings
Required: No

 ** SinkArn **   <a name="OAM-Type-ListLinksItem-SinkArn"></a>
The ARN of the sink that this link is attached to.
Type: String
Required: No

## See Also
<a name="API_ListLinksItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/ListLinksItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/ListLinksItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/ListLinksItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Observability Access Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query OAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
