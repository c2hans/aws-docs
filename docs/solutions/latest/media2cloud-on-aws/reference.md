---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

 This solution includes an option to send operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each deployment
+  **Timestamp** - Media file upload timestamp
+  **Format** - The format of the uploaded media file
+  **Size** - The size of the file the solution processes
+  **Duration** - The length of the uploaded video file

 AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Download the `media2cloud.template` [AWS CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1.  Open the AWS CloudFormation template with a text editor.

1.  Modify the AWS CloudFormation template mapping section from:

   ```
   Send:
       AnonymizedUsage:
         Data: "Yes"
   ```

    to:

   ```
   Send:
       AnonymizedUsage:
         Data: "No"
   ```

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Select **Create stack**.

1.  On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1.  Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1.  Choose **Next** and follow the steps in [Launch the stack](step-1-launch-the-stack.md) in the Deployment section of this guide.

## Contributors
<a name="contributors"></a>
+  Ken Shek
+  Liam Morrison
+  Adam Sutherland
+  Aramide Kehinde
+  Jason Dvorkin
+  Noor Hassan
+  San Dim Ciin
+  Eddie Goynes
+  Raul Marquez

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
