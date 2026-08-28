---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/anonymized-data-collection.html
---

# Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each solution deployment
+  **Timestamp** - Data-collection timestamp

We collect metrics directly from the various resources in the solution. These are filtered for the last 24 hours. The name of each metric comes from the service and is defined by that service. **DeleteEfsFiles** and **StartGlueJob** are our counts.

AWS owns the data gathered through this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before deploying using AWS CDK.

1. Locate the [mappings.py](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/blob/main/source/cdk_solution_helper_py/helpers_cdk/aws_solutions/cdk/mappings.py) in your local

1. set the value of the **send\_anonymous\_usage\_data** input parameter in the ** *init* ** method to **False**

1. Follow the deployment steps documented in the readme.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
