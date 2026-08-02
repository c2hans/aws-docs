---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/scaling.html
---

# Scaling chaos engineering across your organization
<a name="scaling"></a>

As your organization adopts chaos engineering, standardizing and implementing it will present challenges. In the early stages of maturity, different teams are likely to use different tooling and variations of the chaos engineering process described in the previous sections. At the same time, some teams might not prioritize or adopt chaos engineering at all, despite its potential benefits. The following sections provide guidance on how to overcome these challenges.

Overall, your approach to chaos engineering should be designed to strike a balance between centralized leadership and decentralized participation. This balance helps ensure that chaos engineering is integrated into the development process and that learnings are shared across your organization.

## Establishing a chaos engineering practice
<a name="establish-practice"></a>

Standardizing the practice of chaos engineering can accelerate its adoption. Sharing the learnings from experiments across teams can magnify the return on chaos engineering investments.

Build a centralized center of excellence, or assemble a group of subject matter experts, as part of your chaos engineering practice. As a small, centralized function, this team can function across software development, infrastructure, security, and business teams and maintain standards that are used by those teams. For simplicity,  the center of excellence is called the *centralized practice team*, and groups that apply chaos engineering are called *practicing teams* in the remainder of this guide.

### Role of the centralized practice team
<a name="role-of-the-centralized-practice-team.07d37dc0-74fd-5c7f-95c2-f2b6e56ed369"></a>

The centralized practice team is responsible for developing and implementing chaos engineering practices across the organization. They work closely with practicing teams to guide them in designing and conducting experiments, and ensuring that the experiments are valuable to the business. The centralized practice team also provides guidance and support to the development, infrastructure, and security teams to help them integrate chaos engineering into their development processes.

The key responsibilities of a centralized chaos engineering practice team include the following:
+ **Enablement** ‒ A centralized chaos engineering function acts as a facilitator to introduce the practice of chaos engineering through game days and workshops. They guide teams in the process of chaos engineering, including selecting failure scenarios, defining hypotheses, and producing reports to be shared with the wider organization. The centralized practice team should own training materials and work to upskill the practicing teams in their use of chaos engineering.
+ **Advisory** ‒ The centralized practice team can also act in an advisory role to oversee experiments that are conducted by the practicing teams. Their experience and knowledge can ensure that experiments deliver value to the business and are conducted in a safe manner. Similarly, the team can oversee the execution and debrief of an experiment to guide people who are new to chaos engineering.
+ **Marketing and value tracking** ‒ Communicating the business value of chaos engineering is key to the success of such a program. Each team that participates in chaos engineering experiments should collect data from the experiments across the business and demonstrate the value of the organization's investment into chaos engineering. This includes quantifying and celebrating the number of incidents that were avoided during each experiment, the downtime that would have been incurred if the experiment had failed, and the overall impact to the business if the failure scenarios had occurred in production. By gathering and centralizing such data from across the teams, and making the data available across the organization, the centralized practice team can track and influence the value derived from the adoption of chaos engineering throughout the organization.
+ **Standards** ‒ The centralized practice team should own and maintain the process for conducting chaos experiments, the templates for planning and reporting on experiments, and the tooling used to conduct experiments.

  The central team should own and manage experiment planning templates, experiment report templates, process documentation, and enablement materials. Best practice documentation and enablement materials provide guidance to practicing teams on topics such as the guardrails they can use to limit the impact of an experiment, when to conduct an experiment in production, and how to evolve their use of chaos engineering over time. For examples of templates and outputs, see the [appendix](appendix.md).

  The centralized practice team should also own the process for conducting an experiment, including communications and escalation, and when and how to communicate with other teams in the organization before or during an experiment. The process should also outline when guardrails are required.

  The centralized practice team should also select and own the core tools for conducting chaos experiments (for example, tools such as AWS FIS). The selection and implementation of supplementary tools, such as load generation tools, should be left to the practicing teams to decide. Practicing teams should be able to adapt the overall process and tooling to best suit their needs.

### Role of the practicing teams
<a name="role-of-the-practicing-teams.2b83c77a-f52b-569c-a2b1-46accaf95435"></a>

The centralized team is responsible for driving the overall chaos engineering strategy, whereas the practicing teams participate in the process and own the development and execution of experiments. This helps to ensure that the experiments are relevant to each specific product or service, and that the learnings are actionable and can be applied to improve the product's reliability and resilience. The centralized practice team acts as a mentor and owner of the organization's chaos engineering standards and process. However, in order to prevent the centralized team from becoming a bottleneck, individual practicing teams will need to learn from the central practice to perform chaos experiments for themselves.

## Establishing a community of practice
<a name="establish-community"></a>

In addition to creating a centralized team, we recommend that you establish an informal community of practitioners who are interested in chaos engineering. This community provides a platform for sharing knowledge, best practices, and experiences across practicing teams and the wider organization.

The community of practice can be operated by the centralized chaos engineering practice team, but anyone within the organization can become a member of the community. The centralized team can leverage the community of practice to broadcast updates and source learnings, and to collect feedback from practicing teams who are using the standards and process managed by the centralized team. The community will act as a feedback loop to inform the centralized team of the effectiveness of chaos engineering practices across the practicing teams. The centralized practice team can then adjust their documentation and supporting artifacts to best support the product teams.

## Incorporating chaos engineering into your operational resilience
<a name="incorporate-resilience"></a>

A chaos experiment is an investment by your business to prevent incidents in production. It will be necessary to determine where the business can realize the greatest return on this investment. The organization can work with the centralized chaos engineering practice team to update its standards and determine which products are critical enough to require chaos experimentation.

**Systems development process**

Chaos engineering and chaos experiments should be performed repeatedly as part of an application's lifecycle. Similar to how teams regularly perform disaster recovery tests, they should conduct chaos experiments and game days continuously and periodically throughout the year. This approach improves how an organization anticipates, observes, and responds to incidents.
