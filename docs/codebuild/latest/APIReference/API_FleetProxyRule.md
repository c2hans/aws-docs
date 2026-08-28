---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_FleetProxyRule.html
---

# FleetProxyRule
<a name="API_FleetProxyRule"></a>

Information about the proxy rule for your reserved capacity instances.

## Contents
<a name="API_FleetProxyRule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** effect **   <a name="CodeBuild-Type-FleetProxyRule-effect"></a>
The behavior of the proxy rule.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** entities **   <a name="CodeBuild-Type-FleetProxyRule-entities"></a>
The destination of the proxy rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** type **   <a name="CodeBuild-Type-FleetProxyRule-type"></a>
The type of proxy rule.
Type: String
Valid Values: `DOMAIN | IP`
Required: Yes

## See Also
<a name="API_FleetProxyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/FleetProxyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/FleetProxyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/FleetProxyRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
