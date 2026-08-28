---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus03.html
---

# FSISUS03: How do you select a Region to optimize financial services workloads for sustainability?
<a name="fsisus03"></a>

 Financial institutions must focus on sustainability within their cloud operating model to reduce their impact on the environment and to encourage sustainable practices. Focusing on these areas helps financial institutions adapt their workloads to financial services industry sustainability best practices, to adopt new environmentally friendly technology trends, and to plan for the business impacts of potential future regulatory requirements. The selection of the best Region might be driven by taking into account a variety of reasons.

## FSISUS03-BP01 Choose Regions with services and hardware required for financial service organizations that maximize carbon footprint reductions
<a name="fsisus03-bp01"></a>

### Prescriptive guidance
<a name="prescriptive-guidance-11"></a>

 Recommended guidance for customer architecture includes:
+  Develop a list of all services required by financial services workloads.
+  Select a Region using guidance from FSISUS01-BP01.
+  Develop a cross-reference of sustainable Regions chosen according to the [services that are offered within each Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) as well as the variety and types of sustainable hardware offered in the Region.
+  Prioritize Regions offering energy-efficient generative AI services and sustainable hardware for financial services AI workloads.
+  Select Regions with renewable energy sources for computationally intensive generative AI model training.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
