---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConflictingAliasesList.html
---

# ConflictingAliasesList
<a name="API_ConflictingAliasesList"></a>

A list of aliases (also called CNAMEs) and the CloudFront standard distributions and AWS accounts that they are associated with. In the list, the standard distribution and account IDs are partially hidden, which allows you to identify the standard distributions and accounts that you own, but helps to protect the information of ones that you don't own.

## Contents
<a name="API_ConflictingAliasesList_Contents"></a>

 ** Items **   <a name="cloudfront-Type-ConflictingAliasesList-Items"></a>
Contains the conflicting aliases in the list.
Type: Array of [ConflictingAlias](API_ConflictingAlias.md) objects
Required: No

 ** MaxItems **   <a name="cloudfront-Type-ConflictingAliasesList-MaxItems"></a>
The maximum number of conflicting aliases requested.
Type: Integer
Required: No

 ** NextMarker **   <a name="cloudfront-Type-ConflictingAliasesList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing conflicting aliases where you left off.
Type: String
Required: No

 ** Quantity **   <a name="cloudfront-Type-ConflictingAliasesList-Quantity"></a>
The number of conflicting aliases returned in the response.
Type: Integer
Required: No

## See Also
<a name="API_ConflictingAliasesList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConflictingAliasesList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConflictingAliasesList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConflictingAliasesList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
