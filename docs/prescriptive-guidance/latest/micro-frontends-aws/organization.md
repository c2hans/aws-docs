---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/organization.html
---

# Organization and ways of working
<a name="organization"></a>

As with all architectural strategies, micro-frontends have implications far beyond the technology that an organization chooses to implement. The decision to build micro-frontend applications must align with business, product, organization, operations, and even culture (for example, empowering teams and decentralizing decision making). In return, this type of micro-frontend architecture supports truly agile, product-driven development, because it significantly reduces communication overhead between otherwise independent teams.

## Agile development
<a name="agile"></a>

The idea of agile software development has become so universal in recent years that virtually every organization claims to work agile. While a conclusive definition of *agile* is beyond the scope of this strategy, it's worth reviewing key elements that are relevant to micro-frontend development.

The foundation of the agile paradigm is the [Agile Manifesto](https://agilemanifesto.org/) (2001), which postulated four main tenets (for example, "Individuals and interactions over processes and tools") and twelve principles. Process frameworks such as Scrum and the Scaled Agile Framework (SAFe) have emerged around the Agile Manifesto and have found their way into everyday practices. However, the philosophy behind them is largely misunderstood or ignored.

In the context of micro-frontends architecture, the following agile principles are important to embrace:
+ "Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale."

  This principle emphasizes how important it is to work in increments and deliver software to production as regularly and as often as possible. From a technological perspective, this refers to continuous integration and continuous delivery (CI/CD). In CI/CD, the tools and processes for building, testing, and deployment are integral parts of each software project. The principle also implies that the runtime infrastructure and the operational responsibilities must be owned by the team. That ownership is especially important in distributed systems where independent subsystems might have significantly differing requirements for infrastructure and operations.
+ "Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done."

  "The best architectures, requirements, and designs emerge from self-organizing teams."

  Both of these principles emphasize the benefits of ownership, independence, and end-to-end responsibility. A micro-frontend architecture will be successful when (and only when) teams truly own their micro-frontends. End-to-end responsibility from the conception through design and implementation on to delivery and operation ensures that the team can actually exercise ownership. This independence is required, both technically and organizationally, for the team to have autonomy over the strategic direction. We don't recommend using a micro-frontend platform in a centralized organization that uses a waterfall development model.

## Team composition and size
<a name="teams"></a>

For a software team to exercise ownership, it must govern itself, including how and what the team delivers, within the boundaries imposed by the organization.

To be effective, teams must be able to deliver software independently and have the authority to decide the best way to deliver it. A team that receives feature requirements from an external product manager or UI designs from an external designer, without being involved in the planning of these items, cannot be considered autonomous. The features might violate existing contracts or functionality. Such violations will require further discussions and negotiations, with the risk of delaying the delivery and introducing unnecessary conflicts between teams.

At the same time, teams should not become too large. While a larger team has more resources and can accommodate individual absences, communication complexity grows exponentially with each new member. It isn't possible to state a universally valid maximum team size. The number of people needed for a project depends on factors such as team maturity, technical complexity, pace of innovation, and infrastructure. For example, Amazon follows the two-pizza rule: A team that is too large to be fed on two pizzas should be split into smaller teams. That can be a challenge. The split should happen along natural boundaries and should give each team autonomy and ownership over their work.

## DevOps culture
<a name="devops"></a>

DevOps refers to a software engineering practice where the steps of the development lifecycle are tightly integrated from organizational and technical perspectives. Contrary to popular belief, DevOps is very much about culture and mindset, and very little about roles and tooling.

Traditionally, a software organization would have teams of specialists, such as for design, implementation, testing, deployment, and operations. Whenever a team completed their job, they would hand the project over to the next team. However, the delivery of software through silos of specialized teams causes friction during handovers. At the same time, when specialists are forced to work with a narrow focus, they lack knowledge in neighboring domains, and they don't have a systemic view of the product. Those deficits can lead to low coherence of the software product.

For example, when a software architect designs a solution that is to be implemented by someone on a different team, they might overlook inherent aspects of the implementation (such as a dependency mismatch). Developers then take shortcuts (such as a monkey patch), or a formalized back-and-forth is initiated between the architect and the development team. Because of the overhead of managing these processes, development is no longer agile (in the sense of flexible, adaptive, incremental, and informal).

Although the term DevOps mainly pertains to culture, it implies the technologies and processes that make DevOps possible in practice. DevOps is closely related to CI/CD. When a developer has finished implementing an increment of software, they commit it to a version-control system such as Git. Traditionally, a build system would then build and integrate the software, and have it tested and released in a more or less unified and centralized process. With CI/CD, the building, integration, testing, and release of the software is inherent and automated. Ideally, the process is part of the software project itself through configuration files that are tailored to the given project specifically.

As many steps as possible are automated. For example, manual testing practices should be reduced, because nearly all types of tests can be automated. When the project is set up in that way, updates to a software product can be delivered several times each day with high confidence. Another technology that supports DevOps is infrastructure as code (IaC).

Traditionally, setting up and maintaining IT infrastructure would require the manual work of installing and maintaining hardware (setting up cables and servers in a data center) and operational software. This was necessary, but it had numerous drawbacks. Setup was time-consuming and error-prone. Hardware was often over-provisioned or under-provisioned, leading to either excess spending or degraded performance. By using IaC, you can  describe the infrastructure requirements for an IT system through a configuration file from which cloud services can be deployed and updated automatically.

What does all of this have to do with micro-frontends? DevOps, CI/CD, and IaC are ideal complements to a micro-frontend architecture. The benefits of micro-frontends rely on fast and frictionless delivery processes. A DevOps culture can thrive only in environments where teams own software projects with end-to-end responsibility.

## Orchestrating micro-frontend development across multiple teams
<a name="orchestration"></a>

When scaling micro-frontend development across multiple cross-functional teams, two problems emerge: First, teams start to develop their own interpretation of the paradigm, make framework and library choices, and create their own tooling and helper libraries. Second, fully autonomous teams must take responsibility for generic capabilities such as low-level infrastructure management. Therefore, it makes sense to introduce two additional teams in a multi-team micro-frontend organization: an enablement team and a platform team. These concepts are widely adopted in modern IT organizations with distributed systems and are well-documented in [Team Topologies](https://teamtopologies.com/key-concepts).

The following diagram shows the enablement team providing tools, libraries, standards and testing to three micro-frontend teams. The platform team provides infrastructure, shared runtime capabilities, and domain services to those same three micro-frontend teams.

![Enablement and platform teams contributing to three micro-frontend teams.](http://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/images/guide-img/4cd7ea48-b17c-411c-a5b2-fa8a58f6a617/images/932edbc8-66de-45ba-b80e-37a0dc75153d.png)

The platform team supports the micro-frontend teams by freeing them from undifferentiated heavy lifting. This support can include infrastructure services such as container runtimes, CI/CD pipelines, collaboration tooling, and monitoring. However, setting up a platform team should not lead to an organization in which development is detached from operations. The opposite is true: The platform team offers an engineering product, and micro-frontend teams have ownership and runtime responsibility of their services on the platform.

The enablement team provides support by focusing on governance and ensuring consistency across the micro-frontend teams. (The platform team should not be involved with this.) The enablement team maintains shared resources such as a UI library, and it creates standards such as choice of framework, performance budgets, and interoperability conventions. At the same time, it provides new teams or team members with training in applying standards and tooling as defined by governance.

## Deploying
<a name="deploy"></a>

The north star for autonomy in micro-frontend teams is to have an automated pipeline with a path to production that is independent from other micro-frontend teams. Teams that follow the share-nothing principle can implement independent pipelines. Teams that share libraries or depend on a platform team must decide how to manage dependencies in deployment pipelines.

Typically, each pipeline does the following:
+ Builds frontend assets
+ Deploys the assets to hosting for consumption
+ Ensures that registries and caches are updated so that the new versions can be delivered to customers

The actual pipeline steps vary depending on the technology stack and the page composition approach.

For client-side composition, this means uploading application bundles to hosting buckets, and releasing to consumption through caching at a CDN. Applications that use browser caching with service workers should also implement ways to update the service-worker caches.

For server-side composition, this usually means deploying the new version of the server component and updating the micro-frontend registry to make the new version discoverable. You can use blue/green or canary deployment patterns to gradually roll out new versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
