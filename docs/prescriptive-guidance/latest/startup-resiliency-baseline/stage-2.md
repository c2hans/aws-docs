---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/startup-resiliency-baseline/stage-2.html
---

# Stage 2: Design and implement
<a name="stage-2"></a>

This section discusses turning your resilience objectives into reality. You've mapped out what matters most to your business, and now it's time to build it. How do you build in resilience without slowing down innovation?

Think of AWS managed services as a resilience shortcut. Instead of burning precious engineering hours maintaining infrastructure, use services that handle redundancy for you. For example, consider [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). It automatically stores multiple copies of your data within an AWS Region for durability. It doesn't require extra code or late-night pager duties.

What about your core application components? Smart choices can multiply your team's impact. Consider a database that is the backbone of your service. Instead of building your own replication system, consider using [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html), which automatically handles failover. These features might cost more, but they shift your team's focus from maintaining infrastructure to solving business problems. This cost can be offset through faster feature delivery and avoided revenue loss during outages.

Sometimes startups need to build custom solutions. That's the nature of innovative startups. When you do, keep it simple but smart. Spread your application across multiple Availability Zones by using [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) and [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html). Set the Auto Scaling group minimum capacity to handle your baseline traffic even if one Availability Zone fails. This provides resilience against localized failures without complex architectural patterns. As your startup grows and customers demand higher resilience, you can evolve to more sophisticated approaches.

We recommend that you keep your production and development environments in separate AWS accounts. It's tempting to mix them when you're moving fast, but this boundary is your safety net. It prevents a well-meaning experiment from taking down your production service. Think of it as insurance for your "move fast and break things" development culture - break things in development, keep production stable.

If your application depends on third-party services, plan for their failures. When your payment processor has issues, can your system gracefully handle it? Build simple circuit breakers and fallback options. Maybe queue those transactions instead of showing error messages. Your customers will appreciate that you kept things working, even if not perfectly.

Document as you build, but keep it practical. Focus on recording the *why *behind key decisions, and create simple recovery playbooks. It's important to have these ready when incidents occur.

You're not building for perfect resilience; you're building for appropriate resilience. Every hour spent over-engineering resilience is an hour not spent on features that customers are asking for. Use AWS managed services as your foundation, add targeted resilience where it matters most, and create clear paths to scale up resilience as your business grows.

The next chapter discusses how to validate these design choices without burning through engineering resources. For startups, testing should be a reasonable lift and a smart investment in your application's resilience.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
