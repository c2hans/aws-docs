---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/embed-the-honeypot-link-in-your-web-application-optional.html
---

# Embed the Honeypot link in your web application (optional)
<a name="embed-the-honeypot-link-in-your-web-application-optional"></a>

If you chose `yes` for the **Activate Bad Bot Protection** parameter in [Step 1. Launch the stack](step-1.-launch-the-stack.md), the CloudFormation template creates a trap endpoint to a low-interaction production honeypot. This trap is intended to detect and divert inbound requests from content scrapers and bad bots. Valid users won’t attempt to access this endpoint.

This component enhances bad bot detection by monitoring direct connections to an Application Load Balancer (ALB) or Amazon CloudFront, in addition to the honeypot mechanism. If a bot bypasses the honeypot and attempts to interact with ALB or CloudFront, the system analyzes request patterns and logs to identify malicious activity. When a bad bot is detected, its IP address is extracted and added to an AWS WAF block list to prevent further access. Bad bot detection operates through a structured logic chain, ensuring comprehensive threat coverage:
+ HTTP Flood Protection Lambda Log Parser – Collects bad bot IPs from log entries during flood analysis.
+ Scanner & Probe Protection Lambda Log Parser – Identifies bad bot IPs from scanner-related log entries.
+ HTTP Flood Protection Athena Log Parser – Extracts bad bot IPs from Athena logs, using partitions across query run.
+ Scanner & Probe Protection Athena Log Parser – Retrieves bad bot IPs from scanner-related Athena logs, using the same partitioning strategy.
+ Fallback Detection – If both HTTP Flood Protection and Scanner & Probe Protection are disabled, the system relies on the Log Lambda parser, which logs bot activity based on [WAF label filters](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html).

Use one of the following procedures to embed the honeypot link for requests from either a CloudFront distribution.

## Create a CloudFront Origin for the Honeypot Endpoint
<a name="create-a-cloudfront-origin-for-the-honeypot-endpoint"></a>

Use this procedure for web applications that are deployed with a CloudFront distribution. With CloudFront, you can include a `robots.txt` file to help identify content scrapers and bots that ignore the robots exclusion standard. Complete the following steps to embed the hidden link and then explicitly disallow it in your `robots.txt` file.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose the stack that you built in [Step 1. Launch the stack](step-1.-launch-the-stack.md)

1. Choose the **Outputs** tab.

1. From the **BadBotHoneypotEndpoint** key, copy the endpoint URL.
   + The behavior path (`/ProdStage`)

1. Embed this endpoint link in your content pointing to the honeypot. Hide this link from your human users. As an example, review the following code sample: `<a href="/behavior_path" rel="nofollow" style="display: none" aria-hidden="true">honeypot link</a>`.

1. Modify the `robots.txt` file in the root of your website to explicitly disallow the honeypot link, as follows:

```
User-agent: <*>
        Disallow: /<behavior_path>
```

**Important**
No path registration in CloudFront is required as requests are: Blocked by WAF **BadBotRuleFilter**. Solution collected in logs automatically. Processed by the **Log parser** lambda. This simplified approach uses the WAF logs directly instead of requiring additional endpoint configuration, making the bad bot detection process more efficient through log analysis

**Note**
It’s your responsibility to verify what tag values work in your website environment. Don’t use `rel="nofollow"` if your environment doesn’t observe it. For more information about robots meta tags configuration, refer to the [Google developer’s guide](https://developers.google.com/search/reference/robots_meta_tag). Modify the `robots.txt` file in the root of your website to explicitly disallow the honeypot link, as follows:

## Embed the Honeypot endpoint as an external link
<a name="embed-the-honeypot-endpoint-as-an-external-link"></a>

**Note**
These rules use the source IP address from the web request origin. If you have traffic that goes through one or more proxies or load balancers, the web request origin will contain the address of the last proxy, and not the originating address of the client.

Use this procedure for web applications.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose the stack that you built in [Step 1. Launch the stack](step-1.-launch-the-stack.md).

1. Choose the **Outputs** tab.

1. From the **BadBotHoneypotEndpoint** key, copy the endpoint URL.

   ```
   <a href="<BadBotHoneypotEndpoint value>" rel="nofollow" style="display: none" aria-hidden="true"><honeypot link></a>
   ```
**Note**
This procedure uses `rel=nofollow` to instruct robots to not access the honeypot URL. However, because the link is embedded externally, you can’t include a `robots.txt` file to explicitly disallow the link. It’s your responsibility to verify what tags work in your website environment. Don’t use `rel="nofollow"` if your environment doesn’t observe it.
