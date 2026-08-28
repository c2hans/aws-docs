---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit.html
---

# Running Spark jobs with spark-submit
<a name="spark-submit"></a>

Amazon EMR releases 6.10.0 and higher support `spark-submit` as a command-line tool that you can use to submit and execute Spark applications to an Amazon EMR on EKS cluster.

**Note**
Amazon EMR calculates pricing on Amazon EKS based on vCPU and memory consumption. This calculation applies to driver and executor pods. This calculation starts from when you download your Amazon EMR application image until the Amazon EKS pod terminates and is rounded to the nearest second. Pricing applies whenever pods run using an image derived from the Amazon EMR runtime, regardless of whether the image is stored in the public Amazon EMR Amazon ECR registry or your own private registry, and regardless of how the job is orchestrated (for example, the StartJobRun API, the Spark operator, or spark-submit).

**Topics**
+ [Setting up spark-submit for Amazon EMR on EKS](spark-submit-setup.md)
+ [Getting started with spark-submit for Amazon EMR on EKS](spark-submit-gs.md)
+ [Verify Spark driver service account security requirements for spark-submit](spark-submit-security.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
