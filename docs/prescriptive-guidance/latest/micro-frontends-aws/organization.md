---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/organization.html
---

# Organization and ways of working
<a name="organization"></a>

As with all architectural strategies, micro-frontends have implications far beyond the technology that an organization chooses to implement. The decision to build micro-frontend applications must align with business, product, organization, operations, and even culture (for example, empowering teams and decentralizing decision making). In return, this type of micro-frontend architecture supports agile, product-driven development, because it can help reduce communication overhead between otherwise independent teams.

## Agile development
<a name="agile"></a>

The idea of agile software development has become so universal in recent years that virtually every organization claims to work agile. While a conclusive definition of *agile* is beyond the scope of this strategy, it's worth reviewing key elements that are relevant to micro-frontend development.

The foundation of the agile paradigm is the [Agile Manifesto](https://agilemanifesto.org/) (2001), which postulated four main tenets (for example, "Individuals and interactions over processes and tools") and twelve principles. Process frameworks such as Scrum and the Scaled Agile Framework (SAFe) have emerged around the Agile Manifesto and have found their way into everyday practices. However, many teams misunderstand or ignore the philosophy behind them.

In the context of micro-frontends architecture, the following agile principles are important to embrace:
+ "Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale."

  This principle emphasizes how important it is to work in increments and deliver software to production as often as possible. From a technological perspective, this refers to continuous integration and continuous delivery (CI/CD). In CI/CD, the tools and processes for building, testing, and deployment are integral parts of each software project. The principle also implies that the team must own the runtime infrastructure and the operational responsibilities. That ownership is especially important in distributed systems where independent subsystems might have significantly differing requirements for infrastructure and operations.
+ "Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done."

  "The best architectures, requirements, and designs emerge from self-organizing teams."

  Both of these principles emphasize the benefits of ownership, independence, and end-to-end responsibility. A micro-frontend architecture is more likely to succeed when teams truly own their micro-frontends. End-to-end responsibility from conception through design and implementation to delivery and operation helps the team exercise ownership. This independence is required, both technically and organizationally, for the team to have autonomy over the strategic direction. We don't recommend using a micro-frontend architecture in a centralized organization that uses a waterfall development model.

## Team composition and size
<a name="teams"></a>

For a software team to exercise ownership, it must govern itself, including how and what the team delivers, within the boundaries imposed by the organization.

To be effective, teams must be able to deliver software independently and have the authority to decide the most effective way to deliver it. A team that receives feature requirements from an external product manager or UI designs from an external designer, without being involved in the planning of these items, isn't autonomous. The features might violate existing contracts or functionality. Such violations require further discussions and negotiations, which risk delaying the delivery and introducing unnecessary conflicts between teams.

At the same time, teams shouldn't become too large. While a larger team has more resources and can accommodate individual absences, communication complexity increases significantly with each new member. No single maximum team size applies to every situation. The number of people needed for a project depends on factors such as team maturity, technical complexity, pace of innovation, and infrastructure. For example, Amazon follows the two-pizza rule: If two pizzas can't feed a team, split it into smaller teams. Splitting a team can be challenging. Split along natural boundaries so that each team has autonomy and ownership over its work.

## DevOps culture
<a name="devops"></a>

DevOps refers to a software engineering practice where the steps of the development lifecycle are tightly integrated from organizational and technical perspectives. Contrary to popular belief, DevOps is very much about culture and mindset, and very little about roles and tooling.

Traditionally, a software organization would have teams of specialists, such as for design, implementation, testing, deployment, and operations. Whenever a team completed their job, they would hand the project over to the next team. However, the delivery of software through silos of specialized teams causes friction during handovers. At the same time, when specialists are forced to work with a narrow focus, they lack knowledge in neighboring domains, and they don't have a systemic view of the product. Those deficits can lead to low coherence of the software product.

For example, when a software architect designs a solution that someone on a different team implements, the architect might overlook inherent aspects of the implementation (such as a dependency mismatch). Developers then take shortcuts (such as patching a dependency at runtime), or the architect and the development team start a formalized back-and-forth. Because of the overhead of managing these processes, development is no longer agile (in the sense of flexible, adaptive, incremental, and informal).

Although the term DevOps mainly pertains to culture, it implies the technologies and processes that make DevOps possible in practice. DevOps is closely related to continuous integration and continuous delivery (CI/CD). When a developer finishes implementing an increment of software, they commit it to a version-control system such as Git. Traditionally, a build system would then build and integrate the software, and then test and release it in a unified and centralized process. With CI/CD, the building, integration, testing, and release of the software are inherent and automated. Ideally, the process is part of the software project itself through configuration files that are tailored to the specific project.

You automate as many steps as possible. For example, reduce manual testing practices, because you can automate many types of tests. When you set up the project in that way, you can deliver updates to a software product several times each day with high confidence. Another technology that supports DevOps is infrastructure as code (IaC).

Traditionally, setting up and maintaining IT infrastructure required the manual work of installing and maintaining hardware (setting up cables and servers in a data center) and operational software. This approach had numerous drawbacks. Setup was time-consuming and error-prone. Hardware was often over-provisioned or under-provisioned, leading to either excess spending or degraded performance. By using IaC, you can describe the infrastructure requirements for an IT system in a configuration file, and then deploy and update cloud services from that file automatically.

What does all of this have to do with micro-frontends? DevOps, CI/CD, and IaC complement a micro-frontend architecture. The benefits of micro-frontends rely on fast and efficient delivery processes. A DevOps culture thrives in environments where teams own software projects with end-to-end responsibility.

## Orchestrating micro-frontend development across multiple teams
<a name="orchestration"></a>

When scaling micro-frontend development across multiple cross-functional teams, two problems emerge. First, teams start to develop their own interpretation of the paradigm, make framework and library choices, and create their own tooling and helper libraries. Second, fully autonomous teams must take responsibility for generic capabilities such as low-level infrastructure management. Therefore, it makes sense to introduce two additional teams in a multi-team micro-frontend organization: an enablement team and a platform team. These concepts are widely adopted in modern IT organizations with distributed systems and are well-documented in [Team Topologies](https://teamtopologies.com/key-concepts).

The following diagram shows the enablement team providing tools, libraries, standards, and testing to three micro-frontend teams. The platform team provides infrastructure, shared runtime capabilities, and domain services to those same three micro-frontend teams.

![Enablement and platform teams contributing to three micro-frontend teams.](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/932edbc8-66de-45ba-b80e-37a0dc75153d.png)

The platform team supports the micro-frontend teams by freeing them from undifferentiated heavy lifting. This support can include infrastructure services such as container runtimes, continuous integration and continuous delivery (CI/CD) pipelines, collaboration tooling, and monitoring. However, setting up a platform team shouldn't lead to an organization in which development is detached from operations. The opposite is true: the platform team offers an engineering product, and micro-frontend teams own their services and are responsible for running them on the platform.

The enablement team provides support by focusing on governance and ensuring consistency across the micro-frontend teams. The platform team doesn't take part in this work. The enablement team maintains shared resources such as a UI library, and it creates standards such as choice of framework, performance budgets, and interoperability conventions. At the same time, it trains new teams and team members in applying the standards and tooling that governance defines.

## Deploying
<a name="deploy"></a>

The goal for autonomy in micro-frontend teams is to have an automated pipeline with a path to production that is independent from other micro-frontend teams. Teams that follow the share-nothing principle can implement independent pipelines. Teams that share libraries or depend on a platform team must decide how to manage dependencies in deployment pipelines.

Typically, each pipeline does the following:
+ Builds frontend assets
+ Deploys the assets to hosting for consumption
+ Ensures that registries and caches are updated so that the new versions can be delivered to customers

The actual pipeline steps vary depending on the technology stack and the page composition approach.

For client-side composition, this means uploading application bundles to hosting buckets and releasing to consumption through caching at a content delivery network (CDN). Applications that use browser caching with service workers should also implement ways to update the service-worker caches.

For server-side composition, this usually means deploying the new version of the server component and updating the micro-frontend registry to make the new version discoverable. You can use blue/green or canary deployment patterns to gradually roll out new versions.
