---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/startup-resiliency-baseline/stage-5.html
---

# Stage 5: Respond and learn
<a name="stage-5"></a>

When you're running a startup, complex post-mortem processes can slow down your team. This chapter explores how to learn from incidents without turning them into bureaucratic exercises.

Integrate incident learning into your existing rhythms. If your team already has regular meetings, use ten minutes to discuss recent incidents. Focus on practical questions, such as:
+ Did the runbooks help?
+ Did the alerts happen at the right time?
+ Could AWS managed services have prevented this?

Stay focused on actions, not blame. In a startup, you're not building a perfect system; you're building one that gets better every time something goes wrong.

You can use your ticketing system to track incidents; there's no need for specialized tools. Create a simple template that includes the incident timeline, customer impact, recovery steps taken, and lessons learned. This cam become institutional memory if you actively use it. Review past incidents during onboarding to bring new engineers up to speed. Reference them in architecture reviews when designing similar systems. Pull them into game days to create realistic failure scenarios based on actual events. The template captures what happened, and regular use transforms it into organizational learning.

As startups grow, patterns emerge. Maybe certain components fail more often, or perhaps particular types of changes cause problems. Use these patterns to guide resilience investments. If database failovers cause issues, consider improving your multiple Availability Zone setup. If third-party service disruptions are a common theme, consider improving circuit breakers.

The goal isn't to prevent every possible failure. That's impossible and would slow you down too much. The goal is to learn fast, adapt quickly, and keep the application reliable enough while you're growing rapidly. Use each incident as a chance to make your system a little more resilient, your team a little more knowledgeable, and your customers a little more confident in your service. For startups, speed and learning beat perfection. Create lightweight processes that help you learn from incidents without slowing innovation. The best resilience practices are the ones your team actually uses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
