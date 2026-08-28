---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf04.html
---

# Vector store optimization
<a name="genperf04"></a>

| GENPERF04: How do you improve the performance of data retrieval systems? |
| --- |
|   |

 Data retrieval systems like vector databases support some of the most popular design patterns for generative AI systems. A performance bottleneck in a data retrieval system can have cascading downstream effects, which are difficult to identify. A thorough understanding of data embedding and retrieval systems can help mitigate downstream performance issues. Ultimately, a thorough understanding of the kind of data being tokenized and queried, as well as data access patterns, can help reduce performance issues in the long-run.

**Topics**
+ [GENPERF04-BP01 Test vector embeddings for latency and relevant performance](genperf04-bp01.md)
+ [GENPERF04-BP02 Optimize vector sizes for your use case](genperf04-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
