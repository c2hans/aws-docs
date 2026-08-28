---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops08-bp01.html
---

# DRHCOPS08-BP01 Build feedback loops to adapt to changing data residency requirements
<a name="drhcops08-bp01"></a>

 Data residency requirements can change over time. As AWS expands its Local Zones and Region footprint, new options may become available that allow you to move your data closer to AWS-managed infrastructure while still meeting your residency needs.

 For example, if a new Local Zone launches in a location that meets your data residency requirements, you can move data that was previously hosted on Outposts into the Local Zone, which is an AWS-managed environment. Similarly, if a new AWS Region launches in a country or region where you previously had to use a Local Zone or Outposts to meet data residency needs, you can move that data into the new AWS Region.

 **Desired outcome:** Establish feedback loops to continuously adapt to evolving data residency requirements for Outposts and Local Zones.

 **Benefits of establishing this best practice:** Enables proactive compliance with data sovereignty and localization mandates by facilitating timely adjustments to deployments.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-15"></a>

 Regularly checking for updates on new Local Zone and AWS Region launches, and assessing how they align with your data residency requirements, can help you optimize your architecture and potentially move workloads closer to AWS-managed infrastructure while still complying with your data residency needs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
