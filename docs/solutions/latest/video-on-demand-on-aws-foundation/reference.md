---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/reference.html
---

# Reference
<a name="reference"></a>

 This section includes information about an optional feature for collecting unique metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

 This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When activated, the following information is collected and sent to AWS each time a video is processed:
+  **Solution ID** - The AWS solution identifier.
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Video on Demand on AWS Foundation deployment.
+  **Timestamp** - Data-collection timestamp.
+  **Job Settings** - The job settings with the source and destination object paths removed. This helps us understand what output groups customers are looking for.

 AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Download the `video-on-demand-on-aws-foundation.template` [AWS CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1.  Open the CloudFormation template with a text editor.

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

1.  Choose **Next** and follow the steps in [Launch the stack](launch-the-stack.md) in the Deploy the solution section of this guide.

## Contributors
<a name="contributors"></a>
+  Tom Nightingale
+  Joan Morgan
+  Eddie Goynes
+  Raul Marquez
