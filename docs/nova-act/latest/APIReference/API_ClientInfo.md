---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ClientInfo.html
---

# ClientInfo
<a name="API_ClientInfo"></a>

Information about the client making API requests, used for compatibility checking.

## Contents
<a name="API_ClientInfo_Contents"></a>

 ** compatibilityVersion **   <a name="novaact-Type-ClientInfo-compatibilityVersion"></a>
The compatibility version of the client, used to ensure API compatibility.
Type: Integer
Required: Yes

 ** sdkVersion **   <a name="novaact-Type-ClientInfo-sdkVersion"></a>
The version of the SDK being used by the client.
Type: String
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_ClientInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ClientInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ClientInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ClientInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
