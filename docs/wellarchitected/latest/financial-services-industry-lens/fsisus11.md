---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus11.html
---

# FSISUS11: Do you store processed data or raw data?
<a name="fsisus11"></a>

## FSISUS11-BP01 Use processed data to reduce your storage footprint
<a name="fsisus11-bp01-use-processed-data-to-reduce-your-storage-footprint"></a>

 Often raw data from your data sources may include a large number of observations from streaming data sources that continually produce data or include large amounts of redundant data from a variety of sources. You can reduce your storage requirements by first processing the raw data, then storing only the results. Unless you have a raw data retention compliance policy or requirement, you can purge the raw data automatically shortly after processing to reduce your data storage requirements.

 Store processed generative AI training data rather than raw data when compliance allows. Implement efficient vector storage strategies for generative AI applications. Optimize vector lengths for embedded tokens in generative AI systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
