---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/aws-services.html
---

# Using AWS services to identify cost optimization opportunities for SAP workloads
<a name="aws-services"></a>

## Cost optimization process
<a name="cost-optimization-process"></a>

Cost optimization is a continuous process that, when implemented, should reveal significant insight and potentially large up-front savings. This continuous process provides ongoing insights and helps you react quickly if anomalies are detected in AWS service consumption that could increase costs.

The overall process consists of six steps, which are highlighted in the following image.

1. **Review spend** – Familiarize yourself with the AWS Billing console dashboard. This dashboard provides detailed insights into the charges you have incurred for consumed AWS services. Identify five or fewer services that will be the focus of this cost optimization review cycle.

1. **Action findings** – Use the services mentioned in [Cost optimization services](cost-optimization-services.md) to evaluate the services you've targeted. After you have completed the deep dive analysis, establish and implement an action plan to reduce the overall spend. The [Cost optimization services](cost-optimization-services.md) section includes recommendations.

1. **Monitor actions** – Validate and monitor the changes to confirm that there are no adverse impacts to the environment.

1. **Automate checks** – Identify automations that can simplify the process of identifying, monitoring, and validating cost optimization opportunities. For example, you can set up billing alerts by using the instructions in [Creating a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) (Amazon CloudWatch documentation). For additional insights into standard automation capabilities, see [Cost optimization services](cost-optimization-services.md).

1. **Document** – Document the process, services, and charges in order to complete a comparison and validate that the expected charges have been reduced or stabilized.

1. **Establish cadence** – Establish a cadence to repeat the cost optimization review.

Continuously repeat this cost optimization process and compare the previous documented results. Using this process, you can reduce costs iteratively.
