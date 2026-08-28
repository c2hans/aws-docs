---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/collection-of-operational-metrics.html
---

# Collection of operational metrics
<a name="collection-of-operational-metrics"></a>

 This guidance includes an option to send anonymous operational metrics to AWS. We use this data to better understand how customers it and related services and products. When activated, the following information is collected and sent to AWS:
+  **Solution ID** - The guidance identifier.
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each deployment.
+  **Timestamp** - Data-collection timestamp.

 AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Download the [AWS CloudFormation template](https://solutions-reference.s3.amazonaws.com/genomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template) to your local hard drive.

1.  Open the AWS CloudFormation template with a text editor.

1.  Modify the AWS CloudFormation template mapping section from:

   ```
   AnonymousData:
       SendAnonymousData:
         Data: Yes
   ```

    to:

   ```
   AnonymousData:
       SendAnonymousData:
         Data: No
   ```

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Select **Create stack**.

1.  On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1.  Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1.  Choose **Next** and follow the steps in [Launch the stack](automated-deployment.md#launch-the-stack) in the Automated Deployment section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
