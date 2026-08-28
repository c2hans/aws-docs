---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AccessControlAttribute.html
---

# AccessControlAttribute
<a name="API_AccessControlAttribute"></a>

These are IAM Identity Center identity store attributes that you can configure for use in attributes-based access control (ABAC). You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify `AccessControlAttributes`, IAM Identity Center passes the attribute values of the authenticated user into IAM for use in policy evaluation.

## Contents
<a name="API_AccessControlAttribute_Contents"></a>

 ** Key **   <a name="singlesignon-Type-AccessControlAttribute-Key"></a>
The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]+`
Required: Yes

 ** Value **   <a name="singlesignon-Type-AccessControlAttribute-Value"></a>
The value used for mapping a specified attribute to an identity source.
Type: [AccessControlAttributeValue](API_AccessControlAttributeValue.md) object
Required: Yes

## See Also
<a name="API_AccessControlAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AccessControlAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AccessControlAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AccessControlAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
