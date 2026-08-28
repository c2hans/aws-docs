---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/faq-scope.html
---

# FAQs about defining scope and requirements
<a name="faq-scope"></a>

The [Defining the scope and requirements for database decomposition](scope.md) section of this guide discusses how to analyze interactions, map dependencies, and establish success criteria. This FAQ section addresses key questions about establishing and managing project boundaries. Whether you're dealing with unclear technical constraints, conflicting departmental needs, or evolving business requirements, these FAQs provide practical guidance on maintaining a balanced approach.

## How detailed should the initial scope definition be?
<a name="how-detailed-should-the-initial-scope-definition-be"></a>

Working backwards from your customers' needs, define project scope with enough detail to identify system boundaries and critical dependencies while maintaining flexibility for discovery. Map essential elements, including system interfaces, key stakeholders, and major technical constraints. Start small by selecting a bounded, low-risk portion of the system that provides measurable value. This approach helps teams to learn and adjust strategies before tackling more complex components.

Document critical business requirements that drive the decomposition effort, but avoid over-specifying details that might change during implementation. This balanced approach makes sure that teams can move forward with clarity while remaining adaptable to new insights and challenges that emerge during the modernization journey.

## What if I discover additional dependencies after starting the project?
<a name="what-if-i-discover-additional-dependencies-after-starting-the-project"></a>

Expect to uncover additional dependencies as the project progresses. Maintain a live dependency log and conduct regular scope reviews to assess impact on timelines and resources. Implement a clear change management process, and include buffer time in project plans to handle unexpected discoveries. The goal isn't to prevent changes but to manage them effectively. This helps teams to adapt quickly while maintaining project momentum.

## How do I handle stakeholders from different departments who have conflicting requirements?
<a name="how-do-i-handle-stakeholders-from-different-departments-who-have-conflicting-requirements"></a>

Handle conflicting departmental requirements through clear prioritization that is based on business value and system impact. Secure executive sponsorship to drive key decisions and resolve conflicts quickly. Schedule regular stakeholder alignment meetings to discuss trade-offs and maintain transparency. Document all decisions and their rationale to promote clear communication and maintain project momentum. Focus discussions on quantifiable business benefits rather than departmental preferences.

## What's the best way to assess technical constraints when documentation is poor or outdated?
<a name="whats-the-best-way-to-assess-technical-constraints-when-documentation-is-poor-or-outdated"></a>

When facing poor documentation, combine traditional analysis with modern AI tools. Use large language models (LLMs) to analyze code repositories, logs, and existing documentation in order to identify patterns and potential constraints. Interview experienced developers and database architects to validate AI findings and uncover undocumented constraints. Deploy monitoring tools that have enhanced AI capabilities in order to observe system behavior and predict potential issues.

Create small technical experiments that validate your assumptions. You can use AI-powered testing tools to accelerate the process. Document findings in a knowledge base that can be continuously enhanced through AI-assisted updates. Consider engaging subject matter experts for complex areas, and use AI pair-programming tools to accelerate their analysis and documentation efforts.

## How do I balance immediate business needs with long-term technical goals?
<a name="how-do-i-balance-immediate-business-needs-with-long-term-technical-goals"></a>

Create a phased project roadmap that aligns immediate business needs with long-term technical objectives. Identify quick wins that deliver tangible value early so that you can build stakeholder confidence. Break down the decomposition into clear milestones. Each should deliver measurable business benefits while progressing toward architectural goals. Maintain flexibility to address urgent business needs through regular roadmap reviews and adjustments.

## How do I make sure that I'm not missing critical requirements from silent stakeholders?
<a name="how-do-i-make-sure-that-im-not-missing-critical-requirements-from-silent-stakeholders"></a>

Map all potential stakeholders across the organization, including downstream system owners and indirect users. Create multiple feedback channels through structured interviews, workshops, and regular review sessions. Build proof-of-concepts and prototypes to make requirements tangible and spark meaningful discussions. For example, a simple dashboard that shows system dependencies often reveals hidden stakeholders and requirements that weren't initially apparent.

Conduct regular validation sessions with both vocal and quiet stakeholders, and make sure that all perspectives are captured. Critical insights often come from those closest to daily operations rather than the loudest voices in the planning meetings.

## Do these recommendations apply for monolithic mainframe databases?
<a name="do-these-recommendations-apply-for-monolithic-mainframe-databases"></a>

The methodology described in this guide also applies to decomposing monolithic mainframe databases. The primary challenges with these databases are managing requirements from the various stakeholders. The technology recommendations in this guide might apply to monolithic mainframe databases. If the mainframe has a relational database, such as an online transaction processing (OLTP) database, then many of the recommendations apply. For online analytical processing (OLAP) databases, such as those used to generate business reports, then only some of the recommendations apply.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
