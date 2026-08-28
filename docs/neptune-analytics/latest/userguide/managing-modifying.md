---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-modifying.html
---

# Modifying a Neptune Analytics graph
<a name="managing-modifying"></a>

 You can change the settings of a Neptune Analytics graph to accomplish tasks such as changing public connectivity or its provisioned-memory.

 It is recommended that you test any changes using a test graph before modifying any production graphs, so that you are able to fully understand the impact of each change.

**Memory scaling**

 Neptune Analytics is a memory-optimized graph database engine for analytics, which stores data in-memory to enable optimal performance for algorithmic and analytical workflows. A Neptune Analytics graph can have the instance size upscaled or downscale the database to a smaller or larger memory size by updating the graph to higher m-NCU. The minimum size of the mNCU chosen must be capable of storing all the data in the graph, smaller mNCU values than that required by the graph will result in `ValidationException` errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
