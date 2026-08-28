---
source_url: https://docs.aws.amazon.com/vpc/latest/mirroring/working-with-traffic-mirroring.html
---

# Work with Traffic Mirroring to copy network traffic
<a name="working-with-traffic-mirroring"></a>

Use Traffic Mirroring to create, manage, and share traffic mirror targets. These targets capture and forward a copy of your traffic to the destination of your choice. Whether you're a network administrator, security analyst, or DevOps engineer, with Traffic Mirroring you can proactively identify and address network issues, ensure compliance, and optimize your overall network performance.

With Traffic Mirroring, you can create and delete traffic mirror targets, view and modify their configurations, and even share them with other AWS accounts. You can also construct custom traffic mirror filters to capture only the data you need, and set up, modify, or delete traffic mirror sessions to control the flow of mirrored data. By using these powerful features, you can unlock new insights and make informed decisions about your infrastructure, ultimately enhancing your organization's overall network visibility and security.

By using Traffic Mirroring, you can gain visibility into your network, enabling you to make more informed decisions, improve security posture, and drive greater operational efficiency across your AWS environment.

You can work with traffic mirror targets, sessions, and filters by using the Amazon VPC console or the AWS CLI.

**Topics**
+ [Create or delete a traffic mirror target](create-traffic-mirroring-target.md)
+ [View traffic mirror targets and modify target tags](modify-traffic-mirroring-targets.md)
+ [Share a traffic mirror target](tm-sharing.md)
+ [Accept or delete a shared traffic mirror target](tm-share-accept.md)
+ [Create, modify, or delete a traffic mirror filter](create-traffic-mirroring-filter.md)
+ [Create, modify, or delete a traffic mirror session](create-traffic-mirroring-session.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
