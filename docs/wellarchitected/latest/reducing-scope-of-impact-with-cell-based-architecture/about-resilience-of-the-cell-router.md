---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/about-resilience-of-the-cell-router.html
---

# About resilience of the cell router
<a name="about-resilience-of-the-cell-router"></a>

 In a cell-based architecture, the only component that has the shared state of all cells is the cell router. It presents itself as a single point of failure. Therefore, it is essential that it be built of with maximum reliability and also as a cellular component, regardless of whether your cell strategy is AZ independent or non-AZ independent, all the recommendations described so far and later must also be followed for the cell router. Mainly issues of service limits, size and observability.

 In other words, the routing layer still has to scale *infinitely*, but the set of problems that you have to solve for scaling the thinnest possible layer should be a subset of the scaling challenges that non-cellularized application would have to face.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
