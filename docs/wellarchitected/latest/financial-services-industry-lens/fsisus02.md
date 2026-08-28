---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus02.html
---

# FSISUS02: How do you address data sovereignty regulations for location of sustainable Region?
<a name="fsisus02"></a>

 While selection of low-carbon Regions is generally recommended for processing of financial data, sometimes data residency requirements stipulate the use of higher carbon storage.

## FSISUS02-BP01 Run workloads and store restricted data in required country and unrestricted in sustainable Region selected by following SUS01 guidance
<a name="fsisus02-bp01-run-workloads-and-store-restricted-data-in-required-country-and-unrestricted-in-sustainable-region-selected-by-following-sus01-guidance"></a>

### Prescriptive guidance
<a name="prescriptive-guidance-10"></a>

 The following guidance provides insights into data sovereignty regulations.
+  Review data sovereignty regulations and identify workloads and data that can be run in sustainable Regions. You may need to separate your data and processing to take advantage of data and processes using lower carbon resources where data residency is not required, while accessing higher carbon resources when data residency is a requirement.
+  Choose a sustainable Region following the guidance provided in FSISUS01.
+  Run your workloads and store data whenever you are not restricted to specific locations using more sustainable Regions.
+  Balance data residency requirements with sustainable generative AI infrastructure placement.
+  Verify that generative AI training data and model artifacts adhere to regional data sovereignty while optimizing for carbon footprint.
+  Consider federated learning approaches for generative AI models when data cannot cross jurisdictional boundaries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
