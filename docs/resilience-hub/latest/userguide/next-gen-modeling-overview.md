---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-modeling-overview.html
---

# Overview: the systems, user journeys, and services hierarchy
<a name="next-gen-modeling-overview"></a>

The application modeling hierarchy in the next generation of Resilience Hub consists of three levels:
+ **Systems** – The top-level container representing a business application (for example, an e-commerce platform or a trading system).
+ **User journeys** – Critical business paths within a system (for example, "Path to purchase" or "Order fulfillment").
+ **Services** – The building blocks comprising AWS resources, code, and observability that support user journeys. A service belongs to exactly one system but can support multiple user journeys.

The following example shows a hierarchy for an e-commerce platform:

```
System (e.g., "E-commerce Platform")
├── User Journey: "Path to purchase"
│   ├── Service: "Auth Service"
│   ├── Service: "Checkout Service"
│   └── Service: "Payment Service"
├── User Journey: "Order fulfillment"
│   ├── Service: "Order Management Service"
│   └── Service: "Shipping Service"
└── Shared Service: "EKS Platform Service"
    (supports multiple user journeys)
```

You define where to find your AWS resources (AWS CloudFormation stacks, Terraform state files, resource tags, or Amazon EKS clusters), and the next generation of Resilience Hub automatically discovers and maps them into a topology showing how resources connect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
