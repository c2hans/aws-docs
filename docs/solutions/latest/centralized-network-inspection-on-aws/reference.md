---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/reference.html
---

# Reference
<a name="reference"></a>

 This section includes information about an optional feature for collecting unique metrics for this guidance and a list of builders who contributed to this guidance.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

 This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS guidance identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Centralized Network Inspection on AWS deployment
+  **Timestamp** - Data-collection timestamp
+  **Number of CloudFormation Stacks deployed in the account**
+  **Number of Firewalls managed**
+  **Number of Firewall Policies managed**
+  **Number of stateful rule groups deployed**
+  **Number of stateless rule groups deployed**
+  **Number of Suricata rules deployed**
+  **Network Firewall Destination Type**
+  **Network Firewall Log Type**

 AWS owns the data gathered though this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Open the CloudFormation template created in [Step 1 Build deployment assets](step-1-build-deployment-assets.md) with a text editor.

1.  Modify the CloudFormation template mapping section from:

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

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Select **Create stack**.

1.  On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1.  Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1.  Choose **Next** and follow the steps in [Launch the stack](step-2-launch-the-stack.md) in the Deploy the guidance section of this guide.

## Contributors
<a name="contributors"></a>
+  Lalit Grover
+  Nikhil Reddy
+  Aaron Schuetter

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
