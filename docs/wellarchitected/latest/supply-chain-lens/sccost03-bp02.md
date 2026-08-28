---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp02.html
---

# SCCOST03-BP02 Adjust collection frequency depending on the context
<a name="sccost03-bp02"></a>

 Optimize data collection frequency based on business needs and context using event-based triggers and thresholds to reduce costs while maintaining performance and efficiency.

 **Desired outcome:** A well-defined collection strategy which meets the business and functional requirements.

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-52"></a>

 Optimize data collection frequency based on functional and business needs to minimize unnecessary transmission and improve efficiency in supply chain systems.

 Implement event-based or context-dependent collection schemes using tools like AWS IoT Greengrass components to dynamically adapt data gathering, while defining threshold values and triggers for specific events or parameters to determine when to adjust collection frequency.

### Implementation steps
<a name="implementation-steps-53"></a>

1.  Analyze business requirements to determine optimal data collection frequencies for different types of supply chain data.

1.  Implement event-based data collection that triggers only when significant changes or thresholds are reached.

1.  Configure dynamic collection frequency adjustment based on operational context and business priorities.

1.  Deploy AWS IoT Greengrass components to enable intelligent, context-aware data collection at edge locations.

1.  Establish threshold-based triggers that automatically adjust collection frequency based on operational conditions.

1.  Monitor data collection costs and effectiveness to continuously optimize collection strategies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
