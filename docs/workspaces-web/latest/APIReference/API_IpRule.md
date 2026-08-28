---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_IpRule.html
---

# IpRule
<a name="API_IpRule"></a>

The IP rules of the IP access settings.

## Contents
<a name="API_IpRule_Contents"></a>

 ** ipRange **   <a name="workspacesweb-Type-IpRule-ipRange"></a>
The IP range of the IP rule.
Type: String
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/([0-9]|[12][0-9]|3[0-2])|)`
Required: Yes

 ** description **   <a name="workspacesweb-Type-IpRule-description"></a>
The description of the IP rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

## See Also
<a name="API_IpRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/IpRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/IpRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/IpRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
