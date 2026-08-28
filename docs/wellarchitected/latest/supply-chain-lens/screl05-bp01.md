---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/screl05-bp01.html
---

# SCREL05-BP01 Deploy IoT-based monitoring systems to track temperature, humidity, and other environmental factors during transit
<a name="screl05-bp01"></a>

 Deploy comprehensive IoT-based monitoring systems throughout your supply chain to continuously track critical environmental conditions like temperature, humidity, shock, light exposure, and location for sensitive products during storage and transit. Configure these systems with product-specific thresholds that trigger immediate alerts when measurements deviate from acceptable ranges, enabling rapid intervention before product quality is compromised.

 Implement a centralized monitoring dashboard that visualizes real-time condition data across all shipments, with drill-down capabilities to investigate anomalies and historical trend analysis to identify recurring issues. These monitoring capabilities should integrate with quality management systems to automatically document compliance with regulatory requirements and customer specifications while providing complete chain-of-custody verification for sensitive or high-value products.

 **Desired** **outcome**: A supply chain where environmental conditions are actively monitored and controlled to improve product quality.

 **Benefits of establishing this best practice:** Reduces losses due to spoilage or damage, increases customer satisfaction, and compliance with regulatory requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-33"></a>

 To mitigate risks of spoilage or damage, deploy IoT sensors to monitor environmental conditions such as temperature and humidity. Use AWS IoT SiteWise to analyze this data in real-time and implement automated alerts to detect deviations. Regular testing of IoT sensors improves reliability, enabling proactive management of risks during transit.

### Implementation steps
<a name="implementation-steps-33"></a>

1.  **Install IoT sensors**: Deploy sensors to monitor critical environmental conditions during transit.

1.  **Analyze data in real-time**: Use AWS IoT SiteWise to collect and analyze sensor data.

1.  **Set up alerts**: Implement automated alerts for deviations in environmental conditions.

1.  **Test and maintain sensors**: Regularly test sensors to enable accuracy and reliability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
