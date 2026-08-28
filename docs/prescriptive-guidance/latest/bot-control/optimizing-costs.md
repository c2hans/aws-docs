---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/optimizing-costs.html
---

# Optimizing costs for your bot control strategy
<a name="optimizing-costs"></a>

The nature of web traffic is dynamic. This means that the technology and services used to mitigate threats can vary and be tuned over time. This is key when considering a bot control strategy and the controls included in it. Optimization over time is the main principle to keep in mind, and it comes from the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) of the AWS Well-Architected Framework.

AWS WAF web ACLs can be dynamic, especially when new features are released or you are trying to mitigate a new threat. Keeping an eye on your costs involves understanding the [cost dimensions](https://aws.amazon.com/waf/pricing/) of the AWS WAF service and how each affects your final spend. The main driving cost is the number of requests evaluated by the service. There are additional charges if you use the [Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) and [account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html) managed rule groups or if you use advanced actions, such as [CAPTCHA or challenge](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge.html).

Because specialized bot controls come at a premium cost, the primary cost optimization goal is to reduce the number of requests inspected by these advanced controls. Applicable techniques include separating high-value content, applying lower-cost measures first, scoping down the area of evaluation, and combining bot protection with other types of controls. Cost monitoring techniques provide additional visibility across your organization.

## Separating dynamic and static content
<a name="separating-content"></a>

One cost reduction technique is isolating the static content from the dynamic application. The majority of requests to typical web applications are requests to static objects. A common method to reduce the load on application servers is to move static content to its own URL, such as `static.example.com`. This is often achieved by creating a unique content delivery distribution with the caching configuration optimized for static content. This technique can also help lower bot control costs if static content is not commonly targeted in the site or application. Separating the static content from the dynamic application can allow for a more precise application of advanced bot controls.

## Applying lower-cost rules first
<a name="lower-cost-rules"></a>

Another technique is to apply lower-cost, baseline rules that filter out unwanted traffic before using advanced controls, which are more expensive. In practice, this commonly means placing bot control mitigations as a last layer of defense and using preceding controls to filter out unwanted traffic. This pyramid approach was previously discussed in [Techniques for bot control](techniques.md) in this guide. The main goal is to use these lower-cost options to stop unwanted traffic, which reduces the number of requests processed by  advanced, higher-cost mitigation techniques.

## Scoping down the area of evaluation
<a name="scoping-down"></a>

AWS WAF [scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) provide a powerful technique for reducing the number of requests inspected by advanced rules. If separating static content into its own URL cannot be implemented, then scope-down statements are another method to filter out requests that do not require advanced mitigation techniques. This can be done by defining a specific application path, an HTTP method (such as POST), or a similar combination.

## Combining bot protection with other controls
<a name="combining-controls"></a>

Additional cost-control considerations should be reviewed when protecting applications against multiple threats in addition to unwanted bot traffic. For example, protecting against distributed denial of service (DDoS) attacks and against account takeover require additional configuration that can affect costs. [Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) is recommended to help protect applications against DDoS attacks. In particular, its application-layer mitigations can automatically address request floods, thus reducing the number of requests that may be processed by the AWS WAF Bot Control rule group, when placing the rule ahead in the evaluation order. Shield Advanced has an additional benefit; standard managed and custom AWS WAF rules come at no additional cost for resources protected by Shield Advanced. Note that intelligent threat mitigation rule groups, including Bot Control, do incur additional costs, even for resources protected by Shield Advanced.

Applications that require account takeover prevention can use the AWS WAF [Fraud Control account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-acfp.html) rule group. ATP rule group's per-request inspection cost is higher than that of the Bot Control rule group. That higher cost makes it critical to apply the ATP rule group as precisely as possible. Using the Bot Control rule group in conjunction with ATP can help achieve this objective. The Bot Control rule group should be placed ahead of ATP in the web ACL to filter out bot requests and reduce the number of requests inspected by ATP.

For continuous optimization, the most significant activity is monitoring [CloudWatch metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html) associated with the Bot Control rule group. The goal over time is to drive down the number of requests evaluated by the Bot Control rule group to only those that target the resources you need to protect against unwanted bot activity. Building CloudWatch dashboards provides visibility of most critical metrics for applications, including AWS WAF costs and usage.

## Monitoring costs
<a name="monitoring-costs"></a>

[AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) is a tool that enables you to view and analyze your costs and usage. Cost Explorer facilitates analysis of AWS costs, including AWS WAF costs incurred. The tool provides cost information for the most recent 12 months and forecasts future spend for the next 12 months.

[AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) is another cost management control tool that can be useful for monitoring AWS WAF costs. It uses advanced ML technologies to identify anomalous spend and root causes. This helps you quickly take action or receive alerts if there's an unexpected increase in cost. To receive an alert when a specific cost threshold is reached,[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) can provide that tracking and monitoring functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
