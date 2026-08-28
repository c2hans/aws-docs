---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution, pointers to [related resources](#related-resources), and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Video on Demand on AWS deployment
+  **Timestamp** - Data-collection timestamp
+  **Use Glacier** - Whether Amazon Glacier is used
+  **Workflow Trigger** - The workflow trigger selected
+  **Frame Capture** - Whether thumbnails are created for MediaConvert output
+  **Enable MediaPackage** - Whether MediaPackage is enabled

AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the `video-on-demand-on-aws.template` [AWS CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1. Open the AWS CloudFormation template with a text editor.

1. Modify the AWS CloudFormation template mapping section from:

   ```
   AnonymizedData:
    SendAnonymizedData:
    Data: Yes
   ```

   to:

   ```
   AnonymizedData:
    SendAnonymizedData:
    Data: No
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select Create stack.

1. On the Create stack page, Specify template section, select Upload a template file.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Launch the stack](launch-the-stack.md) in the Deploy the solution section of this guide.

## Related resources
<a name="related-resources"></a>
+  [MediaInfo](https://mediaarea.net/en/MediaInfo)

## Contributors
<a name="contributors"></a>
+ Eddie Goynes
+ Tom Nightingale
+ Joan Morgan
+ San Dim Ciin
+ Eric Thoman
+ David Chung
+ Raul Marquez

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
