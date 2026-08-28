---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp03.html
---

# SCCOST03-BP03 Choose the right communication service and configuration depending on the use case
<a name="sccost03-bp03"></a>

 Tailor your communication service selection and setup to match specific supply chain scenarios and requirements.

 **Desired outcome:** A well-defined formatting/transmission strategy which meets the functional requirements of downstream applications and the entire SCM environment.

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-53"></a>

 Use AWS B2B Data Interchange to automatically convert Electronic Data Interchange (EDI) documents into JSON and XML formats, while utilizing MQTT 5 protocol for lightweight communication between sensors and AWS IoT Core. Implement AWS IoT Core device shadow to store and synchronize device states, reducing the need for constant communication, and employ caching mechanisms to store frequently accessed data locally.

### Implementation steps
<a name="implementation-steps-54"></a>

1.  Assess communication requirements for different supply chain use cases and select appropriate protocols and services.

1.  Implement AWS B2B Data Interchange for efficient EDI document processing and format conversion.

1.  Deploy MQTT 5 protocol for lightweight, efficient communication between IoT devices and cloud services.

1.  Configure AWS IoT Core device shadow for state synchronization and reduced communication overhead.

1.  Implement local caching mechanisms to minimize cloud requests and reduce bandwidth consumption.

1.  Optimize Quality of Service (QoS) levels and routing paths to balance reliability with cost efficiency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
