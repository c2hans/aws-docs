---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/get-started-cloud-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Get started with your cloud services provider
<a name="get-started-cloud-services"></a>

When you start using cloud services you will need to decide on the region in which you will be mainly operating your cloud services. An AWS Region is a physical location around the world where data centers. AWS calls each group of logical data centers an Availability Zone (AZ). Each region consists of multiple, isolated, and physically separate AZs within a geographic area. Customers choose a region based on where it makes sense for their workloads and the customer’s security, risk and compliance posture. In order to choose appropriately, you can consider:
+ Proximity to your location (headquarters)
+ Proximity to your customers
+ Services available in your [region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
+ Regulatory and data residency considerations
+ Compliance frameworks that are relevant, such as GDPR and HIPAA
+ Legal and/or tax requirements

Generally, customers select a single main region where they set up administrative services to govern and control all of their cloud resources across all regions where they have workloads. In some specific cases, you may use more than one region in order to best serve your customers or to provide for additional scalability, reliability or low latency for certain workloads, or to satisfy workload-specific requirements, but generally one region is sufficient.

Once you decide which one will be your main region, the next policy you need to establish is what regions you will be operating in, considering your customer base, your disaster recovery strategy, and (other) policies you may have already established in your current IT environment. The policy should include not only what regions you will use, but what you need/want to do with the regions in which you will not be operating any of your workloads, and allowing or restricting access to these regions. This will be part of your **Data residency and retention requirements**; basically, where does your data need to live to comply with your legal requirements, and how long do you need to keep this data stored for your customers. As you define this, you can build data lifecycle polices, to help you archive data at a specified frequency, and delete data that is older than the maximum required archive date.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
