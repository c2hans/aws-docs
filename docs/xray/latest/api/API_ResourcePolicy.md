---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ResourcePolicy.html
---

# ResourcePolicy
<a name="API_ResourcePolicy"></a>

A resource policy grants one or more AWS services and accounts permissions to access X-Ray. Each resource policy is associated with a specific AWS account.

## Contents
<a name="API_ResourcePolicy_Contents"></a>

 ** LastUpdatedTime **   <a name="xray-Type-ResourcePolicy-LastUpdatedTime"></a>
When the policy was last updated, in Unix time seconds.
Type: Timestamp
Required: No

 ** PolicyDocument **   <a name="xray-Type-ResourcePolicy-PolicyDocument"></a>
The resource policy document, which can be up to 5kb in size.
Type: String
Required: No

 ** PolicyName **   <a name="xray-Type-ResourcePolicy-PolicyName"></a>
The name of the resource policy. Must be unique within a specific AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** PolicyRevisionId **   <a name="xray-Type-ResourcePolicy-PolicyRevisionId"></a>
Returns the current policy revision id for this policy name.
Type: String
Required: No

## See Also
<a name="API_ResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ResourcePolicy)
