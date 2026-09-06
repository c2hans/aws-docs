---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RuleCondition.html
---

# RuleCondition
<a name="API_RuleCondition"></a>

The conditions for a routing rule. All specified fields must match for the rule to apply (AND logic). At least one condition field must be set.

## Contents
<a name="API_RuleCondition_Contents"></a>

 ** hostHeader **   <a name="rtbfabric-Type-RuleCondition-hostHeader"></a>
The exact host header value to match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._~-]+`
Required: No

 ** hostHeaderWildcard **   <a name="rtbfabric-Type-RuleCondition-hostHeaderWildcard"></a>
A wildcard pattern for host header matching (for example, `*.example.com`).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[A-Za-z0-9._~*-]+`
Required: No

 ** pathExact **   <a name="rtbfabric-Type-RuleCondition-pathExact"></a>
The exact path to match. Must start with `/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `/[A-Za-z0-9._~/-]*`
Required: No

 ** pathPrefix **   <a name="rtbfabric-Type-RuleCondition-pathPrefix"></a>
The path prefix to match. The request path must start with this value. Must start with `/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `/[A-Za-z0-9._~/-]*`
Required: No

 ** queryStringEquals **   <a name="rtbfabric-Type-RuleCondition-queryStringEquals"></a>
A query string key-value pair that must be present and match exactly.
Type: [QueryStringKeyValuePair](API_QueryStringKeyValuePair.md) object
Required: No

 ** queryStringExists **   <a name="rtbfabric-Type-RuleCondition-queryStringExists"></a>
A query string key that must be present in the request (any value is accepted).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9._~-]+`
Required: No

## See Also
<a name="API_RuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/RuleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/RuleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/RuleCondition)
