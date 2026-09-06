---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This solution includes information about an optional feature for collecting unique metrics for this solution and a list of builders who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each deployment
+  **Timestamp** - Data-collection timestamp
+  **Example: Instance Data** - Count of the state and type of instances managed by the EC2 Scheduler in each AWS Region

Example data:

Running:{t2.micro: 2}, {m3.large: 2} Stopped:{t2.large: 1}, {m3.xlarge:3}

AWS owns the data gathered through this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the [CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Modify the CloudFormation template mapping section from:

```
AnonymizedData:
 SendAnonymizedData:
 Data: Yes
```

```
AnonymizedData:
 SendAnonymizedData:
 Data: No
```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack page, Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local hard drive.

1. Choose **Next** and follow the steps in [Launch the stack](launch-the-stack.md)

## Contributors
<a name="contributors"></a>
+ Akash Garg
+ Brad Hong
+ Colin McCoy
+ David Chung
+ Di Gao
+ Eddie Goynes
+ Eric Thoman
+ James Wang
+ Jiali Zhang
+ Michael Nguyen
+ Raul Marquez
+ Ryan Love
+ San Dim Ciin
+ Spencer Sutton
