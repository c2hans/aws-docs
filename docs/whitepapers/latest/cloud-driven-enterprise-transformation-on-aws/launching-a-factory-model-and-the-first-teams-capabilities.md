---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/launching-a-factory-model-and-the-first-teams-capabilities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Launching a factory model and the first teams’ capabilities
<a name="launching-a-factory-model-and-the-first-teams-capabilities"></a>

**Develop a plan with clear milestone objectives**

For large projects, leaders at Amazon are unwavering on the vision, but flexible on the details and the path to get there. Customers adopting cloud have an opportunity to set clear business targets of 100% migration of Windows and Linux-based platforms first, and to begin to sequence “first mover” teams to drive 50-100 applications at a time to AWS. They can then begin to fill in details as the factory velocity increases and more full skill-set migration teams are brought online. Ideally, business and technology teams should be organized around application portfolios of 50-100 applications, and can complete migration in less than one year. The application groups should be organized so that they can be managed by a small interdisciplinary team, and work with a dedicated set of application owners, testers and business partners / product owners.

Customers with portfolios of thousands of applications do not need a detailed plan for all the remaining business applications hosted on-premises to get started. The “[boil the ocean](https://www.investopedia.com/terms/b/boil-the-ocean.asp#:~:text=%22Boil%20the%20ocean%22%20is%20an,job%20or%20project%20unnecessarily%20difficult.)” approach used by some companies and consultancies to do detailed planning for every last workload before getting underway in earnest for such a large portfolio slows progress. This is not an efficient use of resources, and by delaying the initial production migrations, removes opportunities for teams to “learn by doing”.

Teams move more rapidly and can produce more sprint velocity on AWS only with experience, so the sooner teams begin moving, the sooner they can start to move up the learning curve. They need a framework, as described in this whitepaper, and a business unit to volunteer to join the transformation program journey. The rest of the details for what typically constitutes a multi-year program and thousands of applications can be determined in parallel to program launch. Not having all the answers is no reason to not get started. The best way to get through the transformation is to get started.

Set high-level objectives for each responsible team at the outset to provide a deadline to complete application migrations. Setting top-down aggressive goals, expressed in the number of applications in production on AWS on a quarterly basis, sets the line of sight while maintaining flexibility on the implementation. The detailed wave-by-wave planning can be filled in after teams are in flight and have a better grasp of the design decisions, and what transformation work will be required prior to cutover based on these decisions. While final wave planning can be deferred for 4-5 sprints (8-10 weeks) for a business unit work team, discovery and AWS design should be commenced as soon as it is practical after a migration team is organized around a set of business units or functional application suites.

**Activate a “team-based” approach**

Group the applications developed and managed by a single team, take 5-6 two-week sprints to activate the team and achieve migration velocity, and carry through until all the candidate workloads are migrated to AWS. The focus on moving small sets of applications rapidly from discovery to production on AWS limits the amount of “work in process”.

For those workloads with a longer migration timeline or many components that need to be modernized with the move to cloud, and for suites that are tightly coupled, plan cutovers well in advance and with business alignment. There are several modes to coordinate design, build, deploy, and operate modes, and these can be managed by different owners if the consistent factory playbook is followed.

AWS does not recommend “cherry picking” easy applications across numerous teams. The context switching is not efficient. The effort to activate teams should be done once. “Cherry picking” takes longer for teams to get “all in” on AWS, where new capability development and operational efficiencies are magnified in a single cloud environment. Applications selected for pilot should represent a set of similar applications in the portfolio, in terms of common requirements, complexity, and effort, and set the minimum standards for how subsequent migrations will be implemented.

*Table 5 – Traditional vs. modern views of IT transformation planning and implementation *

|  Traditional view  |  Modern view  |
| --- | --- |
|  Try to develop a detailed plan for the entire migration (all applications all waves) before starting. +   Waterfall process (complete all designs before starting migrations)  <br />+   Sequential delivery (hand-offs) of infrastructure build, middleware configuration, code deployment, network configuration, and testing  <br />+   Architecture teams operate separately from engineering, test, networking, and security   |  Activate a “team-based” approach. +   Use migration to activate team capabilities  <br />+   Reduce complexity by accelerating teams / portfolios through migration  <br />+   Empowered teams with guardrails  <br />+   Integrated two-pizza team design through cutover (Full stack product team or industrialized deployment for non-critical applications)  <br />+   Sprint-based collaboration via rapid iteration through consistent dev, pre-production / QA, and production build and cutover   |

 **Deploy a “factory model” to accelerate your cloud-based business transformation**

You can accelerate your journey to AWS by leveraging a “factory” model to distribute decision rights and increase velocity, while also maintaining the appropriate degree of configuration and architectural controls needed to drive re-usability, consistency, and enforcement of required global and local controls. The primary components of acceleration include:
+  Agile delivery framework
+  Structured “big rock” design sessions for complex applications
+  Application infrastructure pattern development for re-usable architectures
+  Templatized application documentation for design, build, and deployment phases
+  Documented quality standards to increase build, automation, and deployment functions that can be distributed, reducing SME bottlenecks
+  “Build faster” approach applied in specific cases, where it may be effective to split first-time application build documentation and testing in lower environments from incremental deployment automation in higher environments
+  Clear operations integration plans and acceptance criteria for seamless transition to operations teams where applicable
+  Observability strategy to measure performance, inform optimization priorities, and rapidly diagnose issues

The AWS migration factory approach is built on best practices from hundreds of AWS enterprise migrations, and can be specifically tuned to corporate standards. It is applicable to various patterns and paths, whenever a high degree of standardization can be propagated.

A key part to any transformational approach is “structure with flexibility”. Structure includes minimum standards for completeness of design, exit, and acceptance criteria for each build stage, complete documentation including quality infrastructure as code instructions, and operational readiness verification. Regardless of team configuration, factory model, or deployment paths, the process of moving any application to AWS will incorporate the same standardized steps of discovery, design, build, deployment, integration, cutover, and operation.

How the build, deployment, and operations tasks will be shared or owned end-to-end will vary by team, but must meet all the criteria regardless of path. Another strategy to speed builds is to build and deploy consistently across development (Dev), QA / test, and production environments on the V1 path to migration. This may overbuild your lower environments on V1, but after cutover these lower environments can be re-sized or re-configured for cost efficiency.

For V1, speed is gained by consistency of builds. In the dev environment, you test and begin automation of build. In QA / test, teams will establish third-party or external connections if required, and run test suites in this deployment (mirroring production configuration). Production build, validate, and deploy teams may find any last-mile networking or other issues to solve. The cutover itself will usually be a non-event.

For each stage of deployment, there will be tested failback plans in place as well as backup, recovery, and disaster recovery (DR) procedures based on protection needs. Teams with clear acceptance criteria and runbook cutover timelines are empowered to make adjustments or rollback as needed. In every case, clear communication with business partners on cutover timeline and testing windows is the key to successful planning. AWS migration teams help customers develop and implement these plans, and continuously adapt and improve customers’ migration factory practices tailored to specific business needs.
