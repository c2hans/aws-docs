---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp01.html
---

# SCCOST03-BP01 Compress and aggregate data whenever possible to reduce the amount of data that needs to be transmitted over the network
<a name="sccost03-bp01"></a>

 Maximizing processing and sanitation of data reduces the amount of data to be sent and processed in the cloud, leading to significant cost savings and improved performance.

 **Desired outcome:** A well-defined strategy on where data gets processed and transmitted to reduce unnecessary load on the network and cloud

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-51"></a>

 Maximize processing and sanitation of the data in-situ, to reduce the amount of data to be sent and processed in the cloud. AWS IoT Greengrass v2 can help with processing and summarization of data at the edge, while implementing data filtering and aggregation at the edge using AWS IoT Core rules engine or AWS IoT Greengrass v2 components to send only relevant, summarized data to the cloud.

### Implementation steps
<a name="implementation-steps-52"></a>

1.  Identify data processing opportunities at the edge to reduce the volume of data transmitted to the cloud.

1.  Deploy AWS IoT Greengrass v2 for local data processing, filtering, and aggregation at manufacturing facilities.

1.  Implement data compression techniques and Combine multiple measurements into single messages to reduce transmission costs.

1.  Configure AWS IoT Core rules engine to filter and route only relevant data to cloud storage and processing systems.

1.  Establish data summarization processes that aggregate detailed operational data into meaningful insights before cloud transmission.

1.  Monitor network usage and data transmission costs to continuously optimize edge processing strategies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
