---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/waf-traffic-overview-dashboard.html
---

# AWS WAF traffic overview dashboard
<a name="waf-traffic-overview-dashboard"></a>

The traffic overview dashboard in AWS WAF displays an overview of security-focused metrics so that you can identify and act on security risks in a few clicks, such as adding [rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html) during DDoS events. The dashboards include near real-time summaries of the CloudWatch metrics that AWS WAF collects when it evaluates your applications' web traffic. These dashboards are available by default and require no additional setup. They show metrics for each web ACL that you monitor with AWS WAF, including total requests, blocked requests, allowed requests, bot compared to non-bot requests, bot categories, CAPTCHA solve rate, top 10 matched rules, and more.

You can access default metrics such as the total number of requests, blocked requests, and common attacks blocked, or you can customize your dashboard with the metrics and visualizations that are most important to you.

These dashboards provide enhanced visibility and help you answer questions such as:
+ What percent of the traffic that AWS WAF inspected is getting blocked?
+ What are the top originating countries for the traffic that's being blocked?
+ What are common attacks that AWS WAF detects and protects me from?
+ How do my traffic patterns from this week compare with last week?

The dashboard has built-in integration with CloudWatch. Using this integration, you can navigate back and forth between the dashboard and CloudWatch; for example, you can get a more granular metric overview by viewing the dashboard in CloudWatch. You can also add existing CloudWatch widgets and metrics to the traffic overview dashboard, bringing your tried-and-tested visibility structure into the dashboard.
