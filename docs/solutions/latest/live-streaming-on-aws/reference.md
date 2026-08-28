---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/reference.html
---

# Reference
<a name="reference"></a>

Live Streaming on AWS reference documentation

This section includes information about an optional feature for collecting unique metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

<a name="anonymized-data-collection"></a>== Anonymized data collection

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID -** The AWS solution identifier
+  **Unique ID (UUID) -** Randomly generated, unique identifier for each Live Streaming on AWS deployment
+  **Timestamp -** Data-collection timestamp
+  **Example: Instance Data:** Count of the state and type of instances that are managed by the EC2 Scheduler in each AWS Region

Example data:

Running: {`t2.micro:2`}, {`m3.large:2`}

Stopped: {`t2.large:1`}, {`m3.xlarge:3`}

AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

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

1. Select **Create stack**.

1. On the **Create stack** page, specify template section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in Launch the guide.

<a name="contributors"></a>== Contributors
+ Tom Nightingale
+ Tom Gilman
+ Joan Morgan
+ Eddie Goynes
+ Kiran Patel
+ Aijun Peng
+ San Dim Ciin

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
