---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GrantItem.html
---

# GrantItem
<a name="API_GrantItem"></a>

A structure that defines a single grant and its configuration.

## Contents
<a name="API_GrantItem_Contents"></a>

 ** Grant **   <a name="singlesignon-Type-GrantItem-Grant"></a>
The configuration structure for the selected grant.
Type: [Grant](API_Grant.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** GrantType **   <a name="singlesignon-Type-GrantItem-GrantType"></a>
The type of the selected grant.
Type: String
Valid Values: `authorization_code | refresh_token | urn:ietf:params:oauth:grant-type:jwt-bearer | urn:ietf:params:oauth:grant-type:token-exchange`
Required: Yes

## See Also
<a name="API_GrantItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/GrantItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/GrantItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/GrantItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
