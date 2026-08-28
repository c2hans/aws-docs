---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnabledServicePrincipal.html
---

# EnabledServicePrincipal
<a name="API_EnabledServicePrincipal"></a>

A structure that contains details of a service principal that represents an AWS service that is enabled to integrate with AWS Organizations.

## Contents
<a name="API_EnabledServicePrincipal_Contents"></a>

 ** DateEnabled **   <a name="organizations-Type-EnabledServicePrincipal-DateEnabled"></a>
The date that the service principal was enabled for integration with AWS Organizations.
Type: Timestamp
Required: No

 ** ServicePrincipal **   <a name="organizations-Type-EnabledServicePrincipal-ServicePrincipal"></a>
The name of the service principal. This is typically in the form of a URL, such as: ` servicename.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]*`
Required: No

## See Also
<a name="API_EnabledServicePrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/EnabledServicePrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/EnabledServicePrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/EnabledServicePrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
