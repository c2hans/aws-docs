---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/guidelines-steps.html
---

# Guidelines and steps
<a name="guidelines-steps"></a>

The three primary phases during OI are discovery, design, and implementation. This section covers the inputs required from other workstreams and the outputs expected from each phase.

## Discovery phase
<a name="discovery"></a>

Discovery is the ﬁrst phase. It forms the basis of operations readiness. During discovery, you should:
+ Hold workshop or kickoﬀ meetings to come up with a prioritized list of operational domains that need to be modernized.
+ Gather as much information as possible to get the big picture of your processes and procedures.
+ Review documentation such as playbooks, runbooks, and organizational charts.
+ Speak to application owners, support staﬀ, and business owners to create a full picture of pain points.
+ Review service-level agreements (SLAs), operational-level agreements (OLAs), and disaster recovery and backup strategies.
+ Assess your current tooling and technology stack.
+ Evaluate skill gaps and training needs.

## Design phase
<a name="design"></a>

The design phase usually begins soon after discovery and before implementation. However, depending on your delivery methodology (for example, if you're using an agile approach), design and implementation can occur in the same sprint. During the design phase, you use insights from the discovery phase to address gaps and to refine, improve, or even eliminate existing processes and procedures. Key activities include:
+ Creating specific deliverables (for example, architecture diagrams and process flows)
+ Planning change management activities
+ Determining risk assessment and mitigation strategies
+ Planning the timeline and resource allocation

## Implementation phase
<a name="implementation"></a>

Implementation can begin in parallel with the design phase depending on your delivery methodology (for example, agile). During the implementation phase, focus shifts to executing the designed solutions and preparing the organization for adoption. Key activities include:
+ Developing a phased rollout strategy
+ Defining training and documentation requirements
+ Establishing success metrics and key performance Indicators (KPIs)
+ Defining a post-implementation review process
+ Testing for operational readiness

The design and implementation phases are critical to operational automation and integration. For this reason, everything must be fully prepared and production-ready before the go-live date. For detailed guidance on what to consider during these phases, see the [Best practices and recommendations](best-practices.md) section.

Perform these phases in a logical manner in one or more sprints. Deliver functions for core operations or other prioritized domains. You can capture the work for each phase in a cloud playbook. A playbook can take the form of scripts, automated runbooks, or even a summary of processes or steps required to operate your modernized environment.

The following diagram shows the 21 OI domains organized in 4 functions: core operations, security and control, business management, and supporting functions. These are described in detail in the [next section](best-practices.md).

![Operations integration (OI) domains organized in 4 functions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/images/guide-img/6545b5e3-3780-4eb8-a195-e92454bb488e/images/dde01325-c310-4aa4-a8be-c38b1d7ae65e.png)
