---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.6-gather-user-experience-insights-using-digital-experience-monitoring.html
---

# [O.CM.6] Gather user experience insights using digital experience monitoring
<a name="o.cm.6-gather-user-experience-insights-using-digital-experience-monitoring"></a>

 **Category:** RECOMMENDED

 Digital Experience Monitoring (DEM) involves simulating user interactions with applications to measure the performance and availability of services from the perspective of end users. DEM allows teams to proactively detect and resolve issues that may impact user experience. It also helps in validating that application updates or changes do not negatively impact user experience.

 Implement APM tools, such as synthetic transaction monitoring using canaries to simulate user interactions with your application and measure the response times and accuracy of the results.

 DEM is recommended as it provides important insights into the user experience and helps detect issues that may impact user experience

**Related information:**
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [AWS Marketplace - Digital Experience Monitoring](https://aws.amazon.com/marketplace/search/results?searchTerms=Digital+Experience+Monitoring)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
