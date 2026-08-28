---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp02.html
---

# RAISP01 BP02 Consider design trade-offs across competing objectives
<a name="raisp01-bp02"></a>

 Analyze how meeting one release requirement could impact others and establish clear protocols for managing these situations. Your release criteria will sometimes pull your system design in different directions.

 For example, making your system more transparent might affect its accuracy, or adding stronger privacy protections could make it harder to explain how decisions are made. Focus on meeting the minimum requirements for each criteria rather than excelling at some while falling short on others.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation considerations
<a name="implementation-considerations-62"></a>

1.  Identify where your release criteria might work against each other. Understand how meeting one requirement could make it harder to meet another. For example, adding privacy features might lower accuracy, or making decisions more explainable might slow things down.

1.  Set clear priority rules that favor meeting minimum requirements for the criteria over excelling at individual ones. Work with your team, legal experts, and business stakeholders to decide approaches like we'll accept 85% accuracy if it assists us achieve 90% privacy protection rather than maximize accuracy.

1.  Design your system using a holistic approach that meets release criteria requirements. Consider how your architecture, models, and components work together as a whole to achieve acceptable performance across each area instead of optimizing individual parts separately.

1.  Build your system according to these balanced design choices, focusing on hitting your minimum goals across everything such as 85% accuracy, 90% privacy protection, and acceptable response times rather than pushing for peak performance in a single area.

## Resources
<a name="resources-59"></a>

 **Related documents:**
+  [ISO/IEC 42001:2023 A.6.2.3 Documentation of AI system design and development](https://www.iso.org/standard/42001)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
