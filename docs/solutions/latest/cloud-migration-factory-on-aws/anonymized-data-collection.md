---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/anonymized-data-collection.html
---

# Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When activated, the following information is collected and sent to AWS:
+  **Solution ID:** The AWS solution identifier
+  **Unique ID (UUID):** Randomly generated, unique identifier for each Cloud Migration Factory on AWS solution deployment
+  **Timestamp:** Data-collection timestamp
+  **Status:** Status is migrated once a server is launched in AWS MGN with this solution
+  **Region:** The AWS Region where the solution is deployed

**Note**
AWS will own the data gathered via this survey. Data collection will be subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the [AWS CloudFormation template](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution.template) to your local hard drive.

1. Open the AWS CloudFormation template with a text editor.

1. Modify the AWS CloudFormation template mapping section from:

   ```
   Send:
    AnonymousUsage:
    Data: 'Yes'
   ```

   to:

   ```
   Send:
    AnonymousUsage:
    Data: 'No'
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Launch the stack](launch-the-stack.md) in the Automated deployment section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
