---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide described various network access approaches in different scenarios, and it describes the benefits and drawbacks of each architecture. You should understand why choosing a network access approach should not be a purely technology discussion. Alignment between business and technology is essential. The following next steps and recommendations can help you assess and standardize your network architecture strategy by evaluating current capabilities, analyzing market needs, and implementing governance controls.

This section contains the following topics:
+ [Assessing current architecture and capabilities](#next-steps-assess)
+ [Market and customer analysis](#next-steps-marketing-analysis)
+ [Strategic alignment](#next-steps-strategy)
+ [Standardization](#next-steps-standardization)

## Assessing current architecture and capabilities
<a name="next-steps-assess"></a>

Review the current network architecture against relevant data sources, such as the self-assessment framework in this guide, current regulatory requirements, and the current state of the market (both in terms of your customer and a competitive analysis). For example, consider using the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which is based on decades of experience running production systems at scale in the AWS Cloud.

Review any potential exceptions, one-offs, and historical product decisions. Be curious, challenge them, and do not automatically assume their validity. Customer requirements from years ago might no longer be valid. Challenging assumptions creates opportunity to simplify and reduce the complexity of your architecture.

In simple terms, document the observations so that they can be accessed and understood by diverse roles in your organization. Capture where the current state differs from target state, what the target state is, the impact, and when observations were made. Recording this information helps your organizations make decisions based on fresh data.

## Market and customer analysis
<a name="next-steps-marketing-analysis"></a>

Gather insights into market trends. What's the currently preferred way of consumers to access SaaS offerings like yours? Are you still meeting your customers where they are? Did the customer cohorts or behavior change? Did your executives steer the ship toward a new market, a geography with specific regulatory requirements, or a new customer tier? Did your business, or operating model change? For example, are you considering white-labeling your services? Does your growth plan include working with partners so that your service is available to customers when they connect with those partners?

## Strategic alignment
<a name="next-steps-strategy"></a>

When you understand your current capabilities, current architecture, market, and customers, call a strategic alignment meeting. With the relevant product, business, and technology stakeholders, challenge which requirements are still valid and which new requirements need to be considered. Find opportunities to reduce complexity by dropping requirements that are no longer needed. This is not a design by committee; the engineering team needs to prepare and own the actual architecture and implementation details. However, this meeting should clarify why this is the set of requirements that maximizes the benefits for your customers and organization.

## Standardization
<a name="next-steps-standardization"></a>

To attract customers, it might be tempting to let each one freely choose how to connect to your service. After all, any solution might technically work, and you might also have the know-how and resources to manage and operate all of them. This can work well up to a certain point, but as your business scales, it becomes difficult to manage. Your observability stack needs to support metrics from multiple solutions, and your site reliability engineers also need to be able to understand them. You need up-to-date documentation for each connectivity approach. Major changes in your application need to be evaluated against each access approach you are offering. You need to write and maintain automations and infrastructure as code (IaC) for each access approach. The additional overhead of not standardizing access to your service must be weighed against the flexibility that you want to offer to your customers.

If you need a north star to guide your decision making, we suggest standardization. Standardization of how your customers interact with the services you provide is typically the single most impactful action you can take to improve many success metrics across your organization. Standardization makes it easier for product teams to understand the cost structure of your services and make data-driven product decisions. It is easier for operations teams to troubleshoot problems and automate parts of the troubleshooting process in an environment that is developed, rolled out, and operated according to predefined standards. It can help you detect anomalies, unexpected behaviors, or actions by a malicious actor. Standardization also reduces technical debt. It takes fewer cycles for engineering teams to test and roll out changes to production. It can also increase your speed to market, improve self-service onboarding success, and reduce regulatory risk.

Therefore, we suggest that you also review any one-offs that may be in place today. Quantify the number of operational cycles that you spend supporting existing customers. Compare your results with historical data, and assess whether your current approach scales for the years to come. Whenever there is a need to divert from standards, challenge the requirements behind those requests. Evaluate the impact, and balance the immediate benefits with long-term commitments.

In cases where customization is inevitable but in conflict with your standards, consider a shared responsibility model. In this model, your products are largely shielded from the requested changes, and the customization happens in a minimalist, dedicated environment. For an example, see the [Connecting with a transit VPC architecture](options-onprem.md#options-onprem-transit-vpc) section.

## Governance
<a name="next-steps-governance"></a>

For compliance with regulatory requirements and your own, internal standards, governance is essential. With proper governance in place, you can control where and how to enforce standards. You also establish to controls to detect divergence from standards and inform resource owners about necessary corrective actions. [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), and [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) are a few of many AWS services that can help you manage and govern your workloads in the AWS Cloud.

## Repetition
<a name="next-steps-repetition"></a>

Using learnings from your initial efforts, set up a lightweight, repeatable process to stay aligned in the future. Define which roles you need inputs from, how often, how accurate the data needs to be, how the data will be shared, and who will act on it.
