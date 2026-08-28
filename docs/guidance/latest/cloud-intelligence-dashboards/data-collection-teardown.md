---
source_url: https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-teardown.html
---

# Teardown
<a name="data-collection-teardown"></a>

**Note**
Please make sure you empty s3 buckets before deletion of CidDataCollectionStack.

1. In the Data Collection Account, go to S3 and search for bucket names that contain "costoptimization" or cid-data, select the radio button next to the bucket name and then click **Empty**.

1. Navigate to CloudFormation console and search for the Stack named **CidDataCollectionStack**, select the radio button next to the Stack and click **Delete**.

1. In the Management Account, go to CloudFormation Console and search for Stack named **CidDataCollectionReadPermissionsStack**, select the radio button next to the Stack and click **Delete**. This will delete IAM Role created in Management Account to be assumed by Lambda for reading data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Intelligence Dashboards on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
