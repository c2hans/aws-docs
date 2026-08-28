---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/startup-resiliency-baseline/introduction.html
---

# AWS Startup Resiliency Baseline
<a name="introduction"></a>

*Igor Fil, Dylan McCarroll, and Parth Shah, Amazon Web Services*

Every startup founder knows the tension: the team is racing to ship new features while customers expect every release to just work. You wake up to a notification about last night's outage, customer complaints are flowing in, and your roadmap is already packed with promised features. This is the daily reality for startups—balancing the pressure to innovate with the need to maintain stable services.

The instinct to prioritize new features is natural. Investors want growth, customers ask for more capabilities, and competitors aren't standing still. Yet experience shows that resilience problems can derail even the most innovative startups. A service disruption doesn't just mean lost revenue; it erodes the trust you've worked so hard to build with your customers. In fact, rock-solid reliability can become your silent differentiator in a crowded market.

Building resilience into your startup doesn't mean slowing down or massive infrastructure investments. It's about making smart choices early that prevent problems later. Think of it like building a house. It's much easier to put in a solid foundation at the start than to fix structural issues once everything is built. By weaving resilient practices into your initial architecture and operations, you create a competitive advantage. You're not just delivering a product; you're delivering a reliable experience that builds customer loyalty.

The AWS Startup Resiliency Baseline (AWS SRB) was created specifically for teams facing this challenge. It provides a practical path to build reliability into your systems while maintaining the speed that makes startups special. No heavy processes or enterprise-scale complexity, just practical patterns that grow with your business.

This guide describes how to implement the AWS SRB in a startup environment. It helps you identify what really matters for resilience, where to focus your limited resources, and how to build practices that scale as your company grows.

## Scope of guidance
<a name="scope"></a>

When exploring the practical steps of building startup resilience, it's important to understand where this guidance fits within your organization's broader growth trajectory. The AWS Startup Resiliency Baseline is aligned with the [resilience lifecycle framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/introduction.html). It serves as an initial roadmap, designed to help you implement fundamental resilience measures with minimal development overhead as you deploy your first applications on AWS. Think of it as your starter kit for building reliable systems that can recover effectively from disruptions.

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) and this resilience guidance complement each other to help you build secure and reliable infrastructure. This guide dives deeper into resilience practices while the AWS Well-Architected Framework provides a broader set of architectural best practices. You can assess your architecture against these practices using the [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) in your AWS account.

## Shared responsibility model
<a name="shared-responsibility-model"></a>

It's critical to clarify an important aspect of building resilient systems in the cloud: the partnership between AWS and your startup. Resilience in the cloud operates on a [shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html), with AWS and your team each playing distinct roles in ensuring system resilience.

AWS takes responsibility for the resilience of the underlying cloud infrastructure that powers their services. Think of this as the foundation upon which you build your applications. This includes maintaining the resilience of data centers, networking components, and the core AWS services you use in your architecture.

Your startup's responsibility focuses on the resilience of the systems you build and deploy on this foundation. The recommendations in this guide fall within your domain of responsibility. By implementing these practices thoughtfully, you can create applications that use reliable AWS infrastructure and incorporate robust recovery capabilities.

This model means you're never building resilience in isolation. You're building upon a proven, reliable foundation while focusing your efforts on the aspects that directly impact your customers and business operations. This guide explores how to make the most of this shared responsibility model, using reliable AWS infrastructure while implementing practical measures to make sure that your applications recover gracefully from disruptions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
