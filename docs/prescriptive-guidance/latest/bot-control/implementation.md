---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/implementation.html
---

# Implementation strategy
<a name="implementation"></a>

After you have selected a deployment strategy, implementation can begin. The deployment strategy defines how rules are rolled out to different applications. In the implementation strategy, the focus is on the iterative process of adding controls, testing, continuously monitoring, and then evaluating their effects.

## Understanding traffic patterns
<a name="traffic-patterns"></a>

To really understand traffic patterns, it is important to familiarize yourself with the application's business function and expected attributes, such as usage patterns, key resources, and user personas. Incorporate production traffic and traffic generated during testing against the application to establish a baseline for the evaluation. Make sure that the timeframe includes traffic data that sufficiently represents multiple usage peaks.

Using your preferred tool, review the traffic logs and metrics over the representative usage period. Analyze the AWS WAF log data for anomalous requests by filtering on [log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) such as `headers` (for example, `User-Agent` and `Referer`), `country`, and `clientIp`. Make note of uniform resource identifiers (URIs) and their access frequency. Categorize traffic, such as identifying good bots. For example, permit access for beneficial bots, such as search engine crawlers and monitors.

In the AWS WAF console, on the **Bot control dashboard**, a sample of bot activity is available for any active web ACL. Although this provides an initial perspective of common bot request volumes, perform further configuration and analysis to better understand bot activity.

For an effective implementation, you must have a good understanding of bot traffic, its effects, and which bot requests are beneficial vs. malicious. This helps with the next phase, selecting controls, and helps you evaluate bot traffic in parallel.

## Selecting and adding controls
<a name="selecting-controls"></a>

The initial traffic analysis helps determine which bot controls to use and what actions to select for each. You might also choose to log and monitor activity for potential future action. The initial traffic analysis help you select the best control to manage the traffic. For more information about the available controls, see [Techniques for bot control](techniques.md) in this guide.

Consider including additional SDK implementations during this step. This helps you test and complete SDK implementations in all required applications. AWS WAF bot control and fraud control rules provide a full token evaluation benefit when you implement JavaScript SDK or mobile SDK. For more information, see [Why you should use the application integration SDKs with Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-with-tokens.html) in the AWS WAF documentation.

We recommend implementing token acquisition for different application types as follows:
+ **Single-page application (SPA)** – JavaScript SDK (no redirect)
+ **Mobile browser** – JavaScript SDK or rule actions (CAPTCHA or Challenge)
+ **Web views** – JavaScript SDK or rule actions (CAPTCHA or Challenge)
+ **Native applications** – Mobile SDK
+ **iFrames** – JavaScript SDK

For more information about how to implement the SDKs, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the AWS WAF documentation.

## Testing and deploying to production
<a name="testing"></a>

The controls should be initially deployed in a non-production environment where you can perform testing to verify that the expected web application functionality is preserved. Always perform a thorough validation in a test environment prior to production deployment.

After testing and validation in a non-production environment, the production release can proceed. Select a date and time with the lowest expected user traffic. Before deployment, the application and security teams should review operational readiness, discuss how to roll back changes, and review dashboards to ensure all required metrics and alarms are configured.

With [Amazon CloudFront continuous deployment](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/continuous-deployment.html), you can send a small amount of traffic to a staging distribution that has an AWS WAF web ACL configured specifically for bot control evaluation. AWS WAF provides [version management](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-versioning.html) of any new or updated managed rules so that you can test and approve changes before they start evaluating production traffic.

## Evaluating and tuning controls
<a name="tuning-controls"></a>

Implemented controls can provide further insight and visibility into traffic activity and patterns. Frequently monitor and analyze application traffic in order to add or adjust security controls. There is normally a phase of tuning to mitigate potential false negatives and false positives. *False negatives* are attacks that were not caught by your controls and require you to harden your rules. *False positives* represent legitimate requests that were incorrectly identified as attacks and blocked as a consequence.

The analysis and tuning can be done manually or with the help of tools. A Security Information and Event Management (SIEM) system is a common tool that helps provide metrics and intelligent monitoring. There are many available with varying degrees of sophistication, but they all provide a good starting point to obtain traffic insights.

Defining important key performance indicators (KPIs) for websites and applications can help you more quickly identify when things are not working as expected. For example, you can use credit card charge backs, sales per account, or conversion rates as indicators of business anomalies that can be generated by bots. Defining and understanding which metrics and KPIs are valuable to monitor is even more important than just the act of monitoring.

Understanding how to get the right metrics and logs from a bot control solution is just as important as identifying the metrics to monitor. The next section, [Guidelines for monitoring your bot control strategy](monitoring.md), details monitoring and visibility options to consider.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
