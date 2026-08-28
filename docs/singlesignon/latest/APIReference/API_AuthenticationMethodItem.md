---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AuthenticationMethodItem.html
---

# AuthenticationMethodItem
<a name="API_AuthenticationMethodItem"></a>

A structure that describes an authentication method and its type.

## Contents
<a name="API_AuthenticationMethodItem_Contents"></a>

 ** AuthenticationMethod **   <a name="singlesignon-Type-AuthenticationMethodItem-AuthenticationMethod"></a>
A structure that describes an authentication method. The contents of this structure is determined by the `AuthenticationMethodType`.
Type: [AuthenticationMethod](API_AuthenticationMethod.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** AuthenticationMethodType **   <a name="singlesignon-Type-AuthenticationMethodItem-AuthenticationMethodType"></a>
The type of authentication that is used by this method.
Type: String
Valid Values: `IAM`
Required: No

## See Also
<a name="API_AuthenticationMethodItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AuthenticationMethodItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AuthenticationMethodItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AuthenticationMethodItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
