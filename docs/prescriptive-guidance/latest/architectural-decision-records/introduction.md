---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/introduction.html
---

# Using architectural decision records to streamline decision-making during development
<a name="introduction"></a>

*Darius Kunce and Dominik Goby, Amazon Web Services*

This guide introduces the architectural decision records (ADR) process for software engineering projects. ADRs support team alignment, document strategic directions for a project or product, and reduce recurring and time-consuming decision-making efforts.

During project and product development, software engineering teams need to make architectural decisions to reach their goals. These decisions can be technical, such as deciding to use the command query responsibility segregation (CQRS) pattern, or process-related, such as deciding to use the GitFlow workflow to manage source code. Making these decisions is a time-consuming and difficult process. Teams must justify, document, and communicate these decisions to relevant stakeholders.

Three major anti-patterns often emerge when making architectural decisions:
+ No decision is made at all, out of fear of making the wrong choice.
+ A decision is made without any justification, and people don't understand why it was made. This results in the same topic being discussed multiple times.
+ The decision isn't captured in an architectural decision repository, so team members forget or don't know that the decision was made.

These anti-patterns are particularly important to tackle during the development process of a product or project.

Capturing the decision, the context, and considerations that led to the decision in the form of an ADR enables current and future stakeholders to collect information about the decisions made and the thought process behind each decision. This reduces software development time and provides better documentation for future teams.

## Objectives
<a name="business-outcomes"></a>

ADRs target three business outcomes:
+ They align current and future team members.
+ They set a strategic direction for the project or product.
+ They avoid decision anti-patterns by defining a process to properly document and communicate architectural decisions.

ADRs capture the context of the decision to inform future stakeholders. A collection of ADRs provide a hand-over experience and reference documentation. Team or project members use the ADR collection for follow-up projects and product feature planning. Being able to reference ADRs reduces the time required during development, reviews, and architectural decisions. ADRs also allow other teams to learn from, and gain insights into, considerations made by other project and product development teams.
