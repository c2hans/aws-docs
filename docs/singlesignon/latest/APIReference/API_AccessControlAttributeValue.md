---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AccessControlAttributeValue.html
---

# AccessControlAttributeValue
<a name="API_AccessControlAttributeValue"></a>

The value used for mapping a specified attribute to an identity source. For more information, see [Attribute mappings](https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html) in the *IAM Identity Center User Guide*.

## Contents
<a name="API_AccessControlAttributeValue_Contents"></a>

 ** Source **   <a name="singlesignon-Type-AccessControlAttributeValue-Source"></a>
The identity source to use when mapping a specified attribute to IAM Identity Center.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\p{L}\p{Z}\p{N}_.:\/=+\-@\[\]\{\}\$\\"]*`
Required: Yes

## See Also
<a name="API_AccessControlAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AccessControlAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AccessControlAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AccessControlAttributeValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
