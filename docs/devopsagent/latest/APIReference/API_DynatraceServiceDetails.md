---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DynatraceServiceDetails.html
---

# DynatraceServiceDetails
<a name="API_DynatraceServiceDetails"></a>

Complete service details for Dynatrace integration.

## Contents
<a name="API_DynatraceServiceDetails_Contents"></a>

 ** accountUrn **   <a name="devopsagent-Type-DynatraceServiceDetails-accountUrn"></a>
Dynatrace resource account urn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `urn:dtaccount:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** authorizationConfig **   <a name="devopsagent-Type-DynatraceServiceDetails-authorizationConfig"></a>
Dynatrace OAuth client credentials configuration. Use this when registering with OAuth client credentials flow.
Type: [DynatraceServiceAuthorizationConfig](API_DynatraceServiceAuthorizationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_DynatraceServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/DynatraceServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/DynatraceServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/DynatraceServiceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
