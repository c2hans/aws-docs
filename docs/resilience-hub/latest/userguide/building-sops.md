---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/building-sops.html
---

# Building an SOP based on AWS Resilience Hub recommendations
<a name="building-sops"></a>

To build an SOP based on AWS Resilience Hub recommendations, you need an AWS Resilience Hub application with a resiliency policy attached to it, and you need to have run a resiliency assessment against that application. The resiliency assessment generates the recommendations for your SOP.

To build an SOP based on AWS Resilience Hub recommendations, you must create an CloudFormation template for the recommended SOPs and include them in your code base.

**Create an CloudFormation template for the SOP recommendations**

1. Open the AWS Resilience Hub console.

1. In the navigation pane, choose **Applications**.

1. From the list of applications, choose the application you want to create an SOP for.

1. Choose **Assessments** tab.

1. Select an assessment from the **Resiliency assessments** table. If you don't have an assessment, complete the procedure in [Running resiliency assessments in AWS Resilience Hub](run-assessment.md) and then return to this step.

1. Under **Operational recommendations**, choose **Standard operating procedures**.

1. Select all the SOP recommendations you want to include.

1. Choose **Create CloudFormation template**. This can take up to a few minutes to create the AWS CloudFormation template.

   Complete the following procedure to include the SOP recommendations in your code base.

**To include the AWS Resilience Hub recommendations in your code base**

1. In **Operational recommendations**, choose **Templates**.

1. In the list of templates, choose the name of the SOP template you just created.

   You can identify the SOPs that are implemented in your application using the following information:
   + **SOP name** – Name of the SOP that you have defined for your application.
   + **Description** – Describes the objective of the SOP.
   + **SSM document** – Amazon S3 URL of the SSM document that contains the SOP definition.
   + **Test run** – Amazon S3 URL of the document that contains the results of the latest test.
   + **Source template** – Provides the Amazon Resource Name (ARN) of the AWS CloudFormation stack that contains the SOP details.

1. Under **Template details**, choose the link in **Templates S3 Path** to open the template object in Amazon S3 console.

1. In Amazon S3 console, from **Objects** table, choose the SOP folder link.

1. To copy the Amazon S3 path, select the check box in front of the JSON file and choose **Copy URL**.

1. Create an AWS CloudFormation stack from AWS CloudFormation console. For more information about creating an AWS CloudFormation stack, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).

   While creating the AWS CloudFormation stack, you must provide the Amazon S3 path that you copied from the previous step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
