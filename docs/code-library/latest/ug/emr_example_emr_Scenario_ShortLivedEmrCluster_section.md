---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/emr_example_emr_Scenario_ShortLivedEmrCluster_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Create a short-lived Amazon EMR cluster and run a step using an AWS SDK
<a name="emr_example_emr_Scenario_ShortLivedEmrCluster_section"></a>

The following code example shows how to create a short-lived Amazon EMR cluster that runs a step and automatically terminates after the step completes.

------
#### [ Python ]

**SDK for Python (Boto3)**
 Create a short-lived Amazon EMR cluster that estimates the value of pi using Apache Spark to parallelize a large number of calculations. The job writes output to Amazon EMR logs and to an Amazon Simple Storage Service (Amazon S3) bucket. The cluster terminates itself after completing the job.
+ Create an Amazon S3 bucket and upload a job script.
+ Create AWS Identity and Access Management (IAM) roles.
+ Create Amazon Elastic Compute Cloud (Amazon EC2) security groups.
+ Create a short-lived cluster and run a single job step.
 This example is best viewed on GitHub. For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/emr).

**Services used in this example**
+ Amazon EMR

------
