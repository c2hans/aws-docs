---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/migration-consideration.html
---

# Migration consideration
<a name="migration-consideration"></a>

Accurate migration estimates require a comprehensive understanding of your current environment and target architecture before committing to timelines and resource allocations. Overlooking critical factors during the assessment phase can lead to significant estimate variances as the project progresses.

To develop reliable effort estimates for your OpenShift to Amazon EKS migration, evaluate the following factors:

## Start with discovery
<a name="start-with-discovery"></a>

The discovery phase establishes the foundation for accurate migration estimates. Insufficient discovery leads to incomplete assessments and estimate variances during execution. Allocate adequate time for this phase based on your environment's complexity.

A comprehensive discovery phase should include:
+ **Workload inventory** – Catalog all applications, services, and workloads running on OpenShift
+ **Dependency mapping** – Identify application interdependencies, external integrations, and service relationships
+ **Security policy review** – Document existing security controls, RBAC configurations, and compliance requirements
+ **Storage configurations **– Assess persistent volume usage, storage classes, and data persistence patterns
+ **Network topology** – Map network policies, ingress/egress rules, service mesh configurations, and connectivity requirements
+ **CI/CD pipeline assessment** – Evaluate build processes, deployment workflows, and automation tooling

Planning consideration: Legacy workloads with limited documentation or infrequent updates typically require extended discovery time. Factor additional effort for environments where application ownership or architectural knowledge is unclear.

## Categorize workloads by migration complexity
<a name="categorize-workloads-by-migration-complexity"></a>

Migration effort varies significantly based on workload characteristics. A stateless API service requires substantially less effort than a stateful application with persistent storage, custom operators, and complex dependencies. Consider the following application categorization factors.

Categorize workloads into complexity tiers to improve estimation accuracy:
+ **Simple** – Stateless applications with standard configurations and no custom dependencies. Examples include stateless web services, API gateways, and standard containerized applications.
+ **Moderate** – Applications with state management requirements, standard persistent storage needs, and minimal custom tooling. Examples include applications using standard storage classes or common third-party integrations.
+ **Complex** – Workloads requiring custom operators, specific security contexts, or extensive external integrations. Examples include applications with custom resource definitions (CRDs), service mesh configurations, or specialized networking requirements.
+ **High risk** – Business-critical applications with strict availability requirements, legacy codebases, or undocumented dependencies. These workloads require comprehensive testing, validated rollback procedures, and extended validation periods.

Applying effort multipliers: Assign different effort factors based on complexity tiers. Complex workloads typically require 4-5x the migration effort of simple workloads. High-risk workloads may require additional effort for extended testing, stakeholder coordination, and risk mitigation activities.

Document the complexity tier for each workload during discovery to ensure your overall estimate reflects the actual migration scope.

## Gather operational knowledge from application maintainers
<a name="talk-to-the-people-who-actually-maintain-the-applications"></a>

Architecture diagrams and technical documentation may not reflect the current state of your environment. Engineers who maintain and troubleshoot applications often possess operational knowledge that isn't captured in documentation. This should be a critical factor when planning for migration.

Conduct structured interviews with application owners, development teams, and operations staff to capture:
+ **Known issues and failure patterns** – Recurring problems, error conditions, and operational challenges
+ **Existing workarounds** – Temporary solutions or configuration adjustments that maintain functionality
+ **Critical dependencies **– Undocumented integrations, shared services, or external system dependencies
+ **Performance characteristics **– Resource utilization patterns, scaling behaviors, and capacity requirements
+ **Operational procedures** – Manual intervention requirements, restart procedures, or maintenance routines

Allocate time in your project plan for these discovery conversations. The insights gathered help identify migration risks early, preventing timeline impacts from unexpected technical challenges during execution.

## Build estimates as per bottom-up approaches
<a name="build-estimates-bottom-up-not-top-down"></a>

Avoid top-down estimation methods that divide total workloads by available time. This approach doesn't account for workload complexity variations, organizational constraints, or operational realities such as holidays, team availability, and competing priorities.

Use a bottom-up estimation methodology:

1. Estimate by workload category – Calculate effort for each complexity tier based on the assessment framework

1. Include integration work – Account for service connectivity, API integrations, and cross-application dependencies

1. Add testing effort – Include functional testing, performance validation, and user acceptance testing

1. Document migration activities – Allocate time for runbooks, architecture updates, and knowledge transfer

1. Apply contingency buffers – Add reserves for unforeseen technical challenges and scope adjustments

Timeline reconciliation: If the bottom-up estimate exceeds business timeline expectations, address the gap during planning rather than during execution. Options include:
+ Phased migration approach with prioritized workload batches
+ Additional resource allocation or contractor engagement
+ Scope adjustments based on business priority
+ Extended timeline with revised milestone commitments

Early alignment between technical estimates and business expectations reduces mid-project disruptions and enables informed decision-making.

## Account for supporting activities beyond workload migration
<a name="account-for-the-stuff-that-doesn-t-show-up-in-beginning"></a>

Migration projects require substantial effort beyond workload movement. Include these supporting activities in your estimate to ensure adequate resource allocation.
+ Environment setup and configuration – Amazon EKS cluster provisioning, node group configuration, and AWS service integration
+ IAM policies and RBAC mapping – Translation of OpenShift security contexts to AWS IAM roles and Kubernetes RBAC policies
+ Secrets migration and rotation – Migration to AWS Secrets Manager or Amazon EKS secrets encryption, including credential rotation procedures
+ Monitoring and alerting reconfiguration – Implementation of Amazon CloudWatch, AWS X-Ray, or third-party observability tools with appropriate alerting thresholds
+ Runbook updates – Documentation of operational procedures, troubleshooting guides, and incident response workflows for the new platform
+ Team training and knowledge transfer – Upskilling on Amazon EKS, AWS services, and updated operational procedures
+ Stakeholder communication – Regular status reporting, milestone reviews, and executive updates throughout the migration
+ Change management processes – Coordination with change advisory boards, approval workflows, and deployment scheduling
+ Rollback testing and validation – Development and testing of rollback procedures to ensure business continuity

Explicitly document these activities in your project plan with dedicated effort allocations. Omitting these items from estimates leads to under-resourcing and timeline pressure during execution.

## Factor In learning curve
<a name="factor-in-learning-curve-honestly"></a>

Teams transitioning from OpenShift to Amazon EKS require time to develop proficiency with AWS-native services, EKS operational patterns, and cloud-native tooling. Initial migration velocity will be lower as teams build familiarity with the new platform.

Apply a learning curve factor to early migration phases:

1. Initial workloads – Estimate 1.5-2x baseline effort for the first batch of migrations as teams establish processes, tooling, and troubleshooting approaches

1. Mid-phase workloads – Reduce the multiplier as teams gain experience with common migration patterns and AWS service integration

1. Later workloads – Approach baseline estimates as teams achieve proficiency with Amazon EKS operations and migration workflows

Planning consideration: Structure your migration waves to place simpler, lower-risk workloads early in the schedule. This allows teams to build competency before addressing complex or business-critical applications. Factor this velocity ramp into your overall timeline rather than assuming consistent productivity throughout the project.

## Use t-shirt sizing for early conversations, hours for planning
<a name="use-t-shirt-sizing-for-early-conversations-hours-for-planning"></a>

Use estimation techniques appropriate to the project maturity and decision-making requirements.

**Initial assessment phase**: T-shirt sizing (Small, Medium, Large, Extra Large) provides directional guidance for early planning and feasibility discussions without requiring detailed analysis. This approach supports initial budget conversations and timeline expectations.

**Detailed planning phase**: Convert t-shirt sizes to specific effort ranges once the project receives approval and enters active planning. Define clear criteria for each size category to ensure consistent application across workloads.

Example sizing framework:
+ Small – 40-80 hours: Stateless workloads with standard configurations
+ Medium – 80-160 hours: Applications with moderate complexity and standard dependencies
+ Large – 160-320 hours: Complex workloads with custom operators or extensive integrations
+ Extra Large – 320\+ hours: High-risk, business-critical applications requiring extended validation

Document your sizing definitions and share them with stakeholders to establish common understanding. This ensures alignment between technical teams and business stakeholders throughout the estimation and planning process.

## Include contingency reserves
<a name="build-in-contingency-and-defend-it"></a>

Migration projects encounter unforeseen challenges including late-discovered dependencies, tooling issues, team availability constraints, and technical complexities that emerge during execution.

Include a contingency reserve of 15-25% in your total effort estimate. The appropriate percentage depends on:
+ Environment complexity – Higher contingency for environments with limited documentation or legacy workloads
+ Team experience – Additional reserve for teams new to Amazon EKS or AWS services
+ Risk assessment – Increased contingency for migrations with strict availability requirements or complex dependencies
+ Communicating contingency: Frame contingency as risk management rather than estimate padding. This reserve addresses inherent project uncertainties and enables the team to respond to challenges without requiring scope or timeline renegotiation.

Historical data shows that projects without explicit contingency allocation typically experience schedule delays rather than early completion. Building contingency into the initial estimate provides flexibility to manage risks while maintaining stakeholder commitments.

## Separate estimation from commitment
<a name="separate-estimation-from-commitment"></a>

Distinguish between estimates and commitments when communicating with stakeholders. An estimate represents your best assessment based on available information at a specific point in time. A commitment is a formal delivery promise with associated accountability.

Document estimate assumptions: include the conditions and constraints that underpin your estimate:
+ Team availability and resource allocation
+ Completion of discovery and assessment phases
+ Stability of production environments during migration
+ Access to subject matter experts and application owners
+ Availability of required AWS services and tooling
+ No major scope changes or additional workload discoveries

Confidence levels: communicate estimate confidence based on information completeness. Early-phase estimates with limited discovery have lower confidence than detailed estimates built from comprehensive assessments.

Assumption tracking: establish a process to revisit estimates when underlying assumptions change. Significant deviations such as resource constraints, scope additions, or environmental discoveries warrant estimate updates and stakeholder communication.

A clear distinction between estimates and commitments enables realistic planning and maintains stakeholder trust throughout the migration lifecycle.

## Document your assumptions clearly
<a name="document-your-assumptions-visibly"></a>

All migration estimates rely on underlying assumptions about resources, access, scope, and constraints. Document these assumptions explicitly and include them in project planning materials and stakeholder communications.

Key assumptions to document:
+ Team size and availability – Dedicated resource allocation, expected availability percentages, and skill levels
+ Environment access timelines – AWS account provisioning, network connectivity, and access to source OpenShift environments
+ Third-party support responsiveness – Vendor response times for tooling issues, licensing questions, or technical escalations
+ Scope boundaries – Included and excluded workloads, migration approach decisions, and out-of-scope activities
+ Testing requirements – Validation depth, performance testing scope, and acceptance criteria
+ Maintenance windows – Availability and duration of approved downtime windows for migration activities

Assumption management: include assumptions in executive summaries and project charters rather than relegating them to appendices. When assumptions prove incorrect or conditions change, documented assumptions provide clear rationale for estimate adjustments and timeline revisions.

Transparent assumption documentation supports informed decision-making and facilitates productive conversations when project conditions evolve.

## Get input from multiple perspectives
<a name="get-input-from-multiple-perspectives"></a>

Engage multiple teams in the estimation process to capture diverse perspectives on migration complexity, risks, and effort requirements. Single-source estimates often miss domain-specific considerations that impact project scope and timeline.

Include representatives from:
+ Platform engineering – Infrastructure provisioning, cluster configuration, and AWS service integration
+ Application development – Code modifications, dependency updates, and application-specific migration requirements
+ Security and compliance – IAM policy design, security control implementation, and regulatory requirement validation
+ Operations and SRE – Monitoring setup, incident response procedures, and operational readiness activities
+ Project management – Timeline coordination, resource allocation, and stakeholder communication planning

Each discipline identifies risks and effort areas specific to their domain. Platform engineers assess infrastructure complexity, while security teams evaluate compliance requirements and policy migration effort. Operations teams identify monitoring and alerting reconfiguration needs that may not be apparent to development teams.

Collaborative estimation produces more comprehensive and defensible project plans than isolated assessment efforts.

## Review past migrations
<a name="review-past-migrations-yours-and-others"></a>

Use historical project data and external resources to inform your estimation approach and identify common complexity areas.

Internal retrospectives: If your organization has completed previous platform migrations or major infrastructure projects, review post-project analyses to identify:
+ Activities that required more effort than initially estimated
+ Timeline variances and their root causes
+ Areas where estimates proved accurate or conservative
+ Lessons learned that apply to container platform migrations
+ External resources: For organizations undertaking their first major migration, gather insights from multiple sources:
+ AWS Professional Services and AWS Partners – Leverage migration experience and reference architectures specific to OpenShift to Amazon EKS transitions
+ Industry communities – Engage with Cloud Native Computing Foundation (CNCF) communities, AWS user groups, and Kubernetes forums
+ Peer organizations – Connect with teams who have completed similar migrations through professional networks or industry events
+ AWS case studies and reference implementations – Review documented migration patterns and architectural guidance

External perspectives provide realistic insights into common challenges, effort distribution, and risk areas that may not be apparent during initial planning.

## Track actuals vs estimates during execution
<a name="track-actuals-against-estimates-during-execution"></a>

Treat estimation as an ongoing process throughout the migration rather than a one-time planning activity. Track actual effort against estimates to identify variances early and adjust remaining project plans accordingly.

**Variance tracking: **monitor actual migration effort for completed workloads and compare against initial estimates. Significant deviations such as consistent 30% overruns in early migration waves indicate the need to reassess estimates for remaining workloads.

**Checkpoint reviews:** establish regular review intervals to evaluate:
+ Actual versus estimated effort for completed migrations
+ Emerging patterns in complexity or technical challenges
+ Changes in team velocity or productivity
+ New risks or dependencies discovered during execution
+ Validity of original assumptions and constraints

Corrective actions: when variance patterns emerge, update estimates for remaining workloads and communicate timeline or resource implications to stakeholders. Early detection and adjustment prevent larger schedule impacts later in the project.

Schedule checkpoint reviews at logical project milestones such as after each migration wave or monthly intervals rather than waiting for project completion to assess estimate accuracy.

## Clear communication
<a name="communicate-uncertainty-ranges"></a>

Provide effort ranges rather than single-point estimates when uncertainty exists. Ranges reflect the inherent variability in complex migration projects and communicate estimate confidence levels to stakeholders.

Example range format:

"We estimate 800-1,100 hours for this migration phase, with final effort dependent on the complexity discovered during dependency mapping and workload assessment."

Range construction: base your range on:
+ Lower bound – Effort required if assumptions hold and no significant complications arise
+ Upper bound – Effort required if moderate complexity or dependency issues emerge
+ Confidence level – Narrower ranges indicate higher confidence based on information completeness

Range-based estimates set realistic expectations and provide flexibility to accommodate discovery findings without requiring formal estimate revisions. As you gather more information through discovery and early migration phases, you can narrow ranges and increase estimate precision.

Document the factors that influence the range boundaries so stakeholders understand what drives potential variance.

## Conclusion
<a name="final-thought"></a>

Effective migration estimation focuses on reducing uncertainty, establishing realistic expectations, and maintaining stakeholder alignment throughout the project lifecycle. Comprehensive upfront assessment and planning enable smoother execution and more predictable outcomes.

The estimation practices outlined in this guide thorough discovery, workload complexity assessment, cross-functional collaboration, and continuous validation provide a foundation for successful OpenShift to Amazon EKS migrations. Organizations that invest in structured estimation approaches experience fewer mid-project disruptions, more accurate budget management, and stronger stakeholder confidence in technical delivery.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
