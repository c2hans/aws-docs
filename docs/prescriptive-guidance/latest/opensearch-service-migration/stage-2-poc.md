---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/stage-2-poc.html
---

# Stage 2 - Proof of concept
<a name="stage-2-poc"></a>

When performing a migration, it's critical to prove whether the target state solution will work as required. We strongly recommend running a proof-of-concept (PoC) exercise. This section focuses on the various aspects to factor in while running a PoC:
+ Defining entry and exit criteria
+ Securing funding
+ Automating
+ Thorough testing
+ PoC stages
+ Failure simulation

## Defining entry and exit criteria
<a name="entry-exit"></a>

Having clear entry and exit criteria is key to a successful PoC exercise. When you define your entry criteria, consider the following:
+ Use case definition
+ Access to environments
+ Familiarity with various services
+ Associated training requirements

Similarly, define exit criteria that you can use to evaluate the PoC outcome, including the following:
+ Functionality
+ Performance requirements
+ Security implementations PoC

## Securing funding
<a name="funding"></a>

Based on the PoC criteria definition, secure funding for the PoC. Ensure that you have performed the right sizing and considered all costs associated. If you are migrating from on premises to AWS, include the cost associated with migrating your frameworks over to the AWS Cloud from on premises. If you're an existing AWS customer, work with your AWS account manager to understand whether you qualify for credits that can be used for the migration to Amazon OpenSearch Service.

## Automating
<a name="automate"></a>

Identify where automation can be done, and plan for a dedicated track to automate and time-box the testing. Automated deployment and testing helps you to rinse, repeat, test, and validate at a rapid pace and without human-introduced errors.

By time-boxing a test, you can ensure you deliver on time and can pivot to other activities if challenges arise. For example, if your performance tests are taking longer than the estimated time, you can pause that activity. You can then move to other tests and validation activities while your developers fix the issues. You can come back to the performance tests after the issues are resolved. Benchmark your existing solution performance, and create automated performance tests that can validate the effect of your configuration changes during the PoC.

## Thorough testing
<a name="testing"></a>

Test all portions of the stack by making sure that you perform the required validations for the different layers, such as ingestion pipelines and query mechanisms, that integrate with your Amazon OpenSearch Service domain. This will help you validate the end-to-end solution implementation.

### Presentation layer
<a name="presentation-layer.d322e339-dd89-5db0-bd6c-1b5abaa53da0"></a>

In the presentation layer, be sure to run a PoC exercise that includes the following activities:
+ **Authenticate** – Validate the planned mechanisms for authenticating your users.
+ **Authorize** – Identify the authorization mechanisms that you want to follow, and validate that they are working as expected.
+ **Query** – What are the most common use cases that you will encounter in production? What are some edge-case scenarios that are critical to your business? Identify these patterns, and validate them during the PoC.
+ **Render** – Is the data being rendered accurately and appropriately for various users across use cases? For log analytics use cases, you might want to build and test the dashboard on OpenSearch Dashboards or Kibana, depending on the target version, to confirm that it meets your requirements.

### Ingestion layer
<a name="ingestion-layer.b5a29ebb-301c-557b-9474-f362236ccab8"></a>

In the ingestion layer, be sure to evaluate various components such as collection, buffering, aggregation, and storage:
+ **Collection** – For log analytics use cases, validate whether all the data that you are logging is being collected. For search use cases, identify the sources that feed the data and perform validations on completeness and correctness of data to make sure that collection phase has been executed successfully.
+ **Buffer** – If you have a spike in traffic, you might want to make sure that you are buffering the data that is getting ingested. There are various ways to create a buffering design. For example, you can collect data in Amazon Kinesis Data Firehose, or you can use Amazon S3 storage as a buffer.
+ **Aggregation** – Validate any aggregation of data, such as bulk API usage, that you perform during ingestion.
+ **Storage** – Validate whether the storage is able to optimally handle the ingestion that you are performing.

## PoC stages
<a name="poc-stages"></a>

We recommend that you use the following stages to implement your PoC and validate the outcome. Don't be afraid to iterate through these PoC phases and adjust the plan PoC even though you invested time in planning beforehand.
+ **Functional testing and load testing** – Ensure that all levels are being thoroughly tested. Simulate failures in all potions of the stack. For example, if you have a cluster with two large nodes and one of them goes down, the other node must take up all the traffic on your cluster. In such a scenario, having a higher number of smaller can result in a smoother recovery from a node failure. Test your workloads at peak loads and above to make sure that the performance is not impacted in such scenarios. During testing, raise issues early so that any potential issues are being evaluated by various stakeholders at the right time.
+ **Verify KPIs and tune** – During the PoC, ensure that you are meeting the KPIs and business outcomes that you defined in your PoC exit criteria. Tune the configurations in such a way that they are meeting the KPIs.
+ **Automate and deploy** – Automation and monitoring are the other key aspects to focus on during the PoC testing. Refine your automation steps, and validate them along with detailed monitoring to give all the stakeholders enough information to confidently evaluate the outcomes of the PoC. Document all the steps, and create a runbook that you can reuse for the production migration.

## Failure simulation
<a name="failure-simulation"></a>

We highly recommend that you simulate a failure scenario and validate whether your design offers the resilience and fault tolerance required to meet your user requirements. You might want to simulate a failure of a data node to see if your cluster has enough resources to handle the recovery gracefully. To check whether your domain could be overwhelmed with large volume ingestion, you can test the buffering settings by simulating a sudden burst of logs from some of your sources. Validate that your design does not exceed any quotas when you scale to a production deployment. For more information, see the Amazon OpenSearch Service documentation on [service quotas](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/limits.html).
