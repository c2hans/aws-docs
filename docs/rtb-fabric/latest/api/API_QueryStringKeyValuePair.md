---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_QueryStringKeyValuePair.html
---

# QueryStringKeyValuePair
<a name="API_QueryStringKeyValuePair"></a>

A key-value pair for query string matching in a routing rule condition.

## Contents
<a name="API_QueryStringKeyValuePair_Contents"></a>

 ** key **   <a name="rtbfabric-Type-QueryStringKeyValuePair-key"></a>
The key of the query string parameter to match. Must contain only RFC 3986 unreserved characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9._~-]+`
Required: Yes

 ** value **   <a name="rtbfabric-Type-QueryStringKeyValuePair-value"></a>
The value of the query string parameter to match. Must contain only RFC 3986 unreserved characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9._~-]+`
Required: Yes

## See Also
<a name="API_QueryStringKeyValuePair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/QueryStringKeyValuePair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/QueryStringKeyValuePair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/QueryStringKeyValuePair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
