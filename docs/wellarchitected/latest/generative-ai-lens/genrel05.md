---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05.html
---

# Distributed availability
<a name="genrel05"></a>

| GENREL05: How do you distribute inference workloads over multiple regions of availability? |
| --- |
|   |

 Generative AI applications can be as simple as prompt-response workflows against a single foundation model or as advanced as multi-agent orchestration. The various components associated with a generative AI workload are required to service a region of availability. Availability could be over a well-defined zone or it could be expansive covering large geographic areas. Architecting for this variability is a complex problem.

**Topics**
+ [GENREL05-BP01 Load-balance inference requests across all regions of availability](genrel05-bp01.md)
+ [GENREL05-BP02 Replicate embedding data across all regions of availability](genrel05-bp02.md)
+ [GENREL05-BP03 Verify that agent capabilities are available across all regions of availability](genrel05-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
