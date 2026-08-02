---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/measuring-tagging-effectiveness-and-driving-improvements.html
---

# Measuring tagging effectiveness and driving improvements
<a name="measuring-tagging-effectiveness-and-driving-improvements"></a>

 After you have implemented a tagging strategy, it's important to measure its effectiveness against the target use cases. The measure of effectiveness will vary by use case. For example:
+  **Cost attribution** - You could measure the tagging coverage of resources based on spend using tools such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/). For example, you could track the *percent of tagged or untagged* resources that generate charges, particularly monitoring specific tag keys.
+  **Automation** - You might want to audit if the desired result has been achieved. For example, whether non-production Amazon EC2 instances are suspended outside of business hours, auditing instance start and stop times.

 [Resource Groups & Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) within the management account provides additional capabilities to analyze tag policy compliance for all the linked accounts in your organization.

 Based on the results of the measurement of your tagging effectiveness, identify if any improvements or alterations are needed in any of the steps such as use case definition, tagging schema implementation or enforcement. Make necessary changes and repeat the cycle until desired effectiveness is achieved. In the example with cost attribution, you can look at percentage improvement.

 Since it’s the developers and operators that need to perform the actual tagging of resources, it's critical to have them take ownership. This isn’t the only additional responsibility that teams typically assume in their journey of AWS adoption. Increased responsibility for the security and cost of developing and operating their application are also important. Organizations often use goals and targets as means of motivating the adoption of new practices, so this can also apply here.
