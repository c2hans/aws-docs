---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/implement-roadmap.html
---

# Implement the roadmap
<a name="implement-roadmap"></a>

When you have established the roadmap, you need to implement it. We have found that this is where customers face the next challenge: they have spent time *thinking*, and now have to move to *doing*. To connect your strategy to implementation, we recommend the following steps:
+ [Decide where and how to start](#decide)
+ [Organize for success](#organize)
+ [Establish Mechanisms to drive change](#establish)
+ [Develop maturity incrementally](#develop)

## Decide where and how to start
<a name="decide"></a>

This sounds easy, but with so much to achieve, finding a starting point is often a difficult and debated question. Organizations that are moving to the cloud have a lot to focus on, and the initiative can become overwhelming if it isn't put into context. Over the years, customer trends have evolved, but a consistent starting point is [transformational leadership](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-people-perspective/transformational-leadership.html). Driving directives and strategy from the top down and creating the mission statement, tenets, and PR-FAQ enable middle management and individuals to make decisions autonomously, drive clarity, and drive business value from the cloud transformation. If you haven't carried out this exercise or something similar, we recommend it as your first task.

During this exercise, you should recognize that unlike other technology transformations, cloud transformation brings technology closer to the business. Technology is a lever that businesses use to achieve broader goals by enabling agility, stability, cost optimization, and similar outcomes. You must plan this transformation with technology and the business, working back from your organization's 3-5 year strategy, identifying goals along the way, and not being afraid to pivot when needed.

## Organize for success
<a name="organize"></a>

How your organization is structured to achieve cloud migration, adoption, and transformation goals will change as your organization matures. Understanding this, preparing, and being intentional is key to ensuring success.

Generally, at the beginning of the journey the largest teams work on the on-premises environment. Then, as cloud adoption grows, these teams migrate to build, mature, operate, and optimize the cloud platform, and your organization has to adjust to the new ways of working at each of these stages. We have observed that a difficult but important change happens when an organization has moved 5 to 10 percent of their workloads to the cloud (transitioning from the Launch phase to the Scale phase). At this point, an organization uses on-premises teams to operate cloud resources because the migration is not large enough to merit full-time changes, so these teams have to strike a balance between existing and new responsibilities. At the same time, the on-premises teams that are now being asked to operate cloud services require new skills, which involves a steep learning curve.

To understand your organization and develop a plan to enable these changes, we recommend that you look at the topology of teams across your IT organization. We use this method with customers to understand the arrangement and interlinking of functions within an IT organization, which is often different from organizational structures, and then use the AWS COM Framework for guidance on how to organize to deliver against transformation stages and milestones. Any changes to the organizational structure that might be required are informed by this exercise.

The topologies we have used with customers include decentralized, centralized, and federated models. These expand on the operating model 2-by-2 representations covered in the [AWS Well-Architected Framework, Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model-2-by-2-representations.html).

### Decentralized
<a name="decentralized.436cd291-b224-5fe1-be07-10199331a18e"></a>

Large, global corporations that operate across different geographies or industry segments often use the decentralized model, which is illustrated in the following diagram. At these corporations, individual business units have their own IT provisions that can overlap with other regions or business units. However, this is often understood and accepted as a way to provide autonomy and specialization within the region.

![Decentralized operating model](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/bed0e312-afe0-4784-a07b-956759603532.png)

Using the decentralized approach means that each region or business unit has its own Cloud Operating Model that is tailored to the needs of that region or business unit.

### Centralized
<a name="centralized.28efdd0c-0a69-5b07-b2c0-418f45b93980"></a>

A centralized IT function is the model we see most frequently. When this model is in place, customers seek to maintain the same topology when establishing their Cloud Operating Model. This is illustrated in the following diagram.

![Centralized operating model](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/4aabcd39-311d-4b2f-9cc9-b96eb4d77eeb.png)

In this model, the central team provides a curated platform that can be used by workload teams that have their own Cloud Operating Models. With this approach, workload teams can focus on the value they provide to their end-customers without having to worry about the services, operations, or security of the platform they are using. This model works well for smaller companies. However, in large, global organizations, the number of workload teams can be in the hundreds or thousands. To manage at this scale without losing the benefits of a central platform, organizations frequently transition to the federated model, which is outlined in the next section.

### Federated
<a name="federated.38bf7466-3ca0-50a4-a0db-4f8076346430"></a>

Many organizations adopt the federated IT model because it provides a central function that's responsible for the cloud platform but allows for a variety of operating models at the workload level. This means that the central team can focus on providing the best possible platform for the organization without the constraint of working to the lowest common denominator. The following diagram illustrates the federated model.

![Federated operating model](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/8c366025-49b6-4931-bcf2-5a514f6aa3a8.png)

In large organizations, the federated model provides the autonomy required by engineering teams while ensuring that the central team provides the platform and undifferentiated heavy lifting that is common across all workloads. In this model, the central team has to work in the same product-centric way as the engineering teams, but their product is the platform.

### Changing the topology to match the journey
<a name="changing-the-topology-to-match-the-journey.eb29b5f5-3b9e-5856-a851-e7d465a16450"></a>

The topology you choose depends on the size of your company, but it also adjusts to the stage of your cloud journey. The organization of departments or teams isn't static, but changes with each stage of cloud adoption. This means that you might design, discuss, and augment different topologies as the environment changes. Examples of influencing factors include:
+ Moving from proof of concept (POC) to pilot workloads
+ Geographic or business unit expansion
+ Moving to product-centric teams
+ Opportunities to benefit from economies of scale from shared components or patterns
+ Realization of [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html), which influences application and service design over architectural requirements
+ Cloud-first mandates or other top-down initiatives
+ KPI or business goal misses caused by incompatible team goals or organizations

## Establish Mechanisms to drive change
<a name="establish"></a>

Within Amazon, a *Mechanism* is defined as follows: *A complete process that converts Inputs to Outputs and is assembled from Organizational Levers. It uses data and feedback to support the process and ensure outcomes are met.* Because each organization is different, every Cloud Operating Model journey is different, but they all need a Mechanism to drive change.

We recommend that you spend time understanding and developing Mechanisms to match the changes required to implement your Cloud Operating Model. A popular approach is to adopt Agile principles. Agile mechanisms break down organizational and process-based barriers between siloed teams, and create feedback loops to ensure that your organization is spending time innovating on the most impactful activities that will drive the most business value.

## Incrementally develop maturity
<a name="develop"></a>

*Maturity* in the context of a Cloud Operating Model refers to how close your capabilities are to cloud-first ways of working. For example, how autonomous are your processes, and how much human involvement is needed to manage the business as usual (run the company) compared with innovation (change the company)? If your activities are more heavily weighted toward the former, your (cloud) maturity is low; if it's the latter, your maturity is higher. Being low on the maturity scale is not a negative―it's a reflection of where you are on your journey. The aim is to understand where you are and where you need to get to. When we work with AWS customers, we use a maturity scale within the AWS COM Framework to provide the steps along the journey.

We recommend using a Mechanism to incrementally increase maturity across the AWS COM Framework capabilities. An example of how we have worked with customers in this way is  converting maturity reviews and prioritization (inputs) to an increase in maturity (output), and then carrying out experience-based events such as a [Game Day](https://aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.gameday.en.html)s (feedback loops) to verify results and adjust as required. By establishing these mechanisms alongside customers, we have found that when this organizational strength is developed, it not only enables the achievement of immediate milestones, but allows for incremental improvement that lasts beyond the initial phases of the journey.

Paying attention to maturing your organization's capabilities and incrementally building the changes required in specific capabilities, at specific times in your roadmap, ties strategy to implementation. It also helps you take advantage of the economies of scale that come with building on your previous achievements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
