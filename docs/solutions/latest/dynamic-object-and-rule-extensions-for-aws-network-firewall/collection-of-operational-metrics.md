---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/collection-of-operational-metrics.html
---

# Collection of operational metrics
<a name="collection-of-operational-metrics"></a>

 This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID:** AWSSOLUTION/SO0196/1.0.0
+  **Unique ID (UUID):** Randomly generated, unique identifier for each Dynamic Object and Rule Extensions for AWS Network solution deployment
+  **Timestamp:** Data-collection timestamp

 AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the [CloudFormation template](https://solutions-reference.s3.amazonaws.com/content-localization-on-aws/latest/content-localization-on-aws.template) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Modify the CloudFormation template mapping section from:

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

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in the [Deployment](deployment.md) section of this guide.
