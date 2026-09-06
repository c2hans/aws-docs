---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Webhook.html
---

# Webhook
<a name="API_Webhook"></a>

Represents a complete Webhook with all its properties, and unique identifier.

## Contents
<a name="API_Webhook_Contents"></a>

 ** webhookId **   <a name="devopsagent-Type-Webhook-webhookId"></a>
The unique identifier of the Webhook
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** webhookUrl **   <a name="devopsagent-Type-Webhook-webhookUrl"></a>
Webhook endpoint URL.
Type: String
Pattern: `https://[a-zA-Z0-9.-]+(?:/.*)?`
Required: Yes

 ** webhookType **   <a name="devopsagent-Type-Webhook-webhookType"></a>
Webhook authentication type.
Type: String
Valid Values: `hmac | apikey | gitlab | pagerduty`
Required: No

## See Also
<a name="API_Webhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Webhook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Webhook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Webhook)
