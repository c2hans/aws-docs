---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When activated, the following information is collected and sent to AWS:
+ Solution ID - The AWS solution identifier
+ Unique ID (UUID) - Randomly generated, unique identifier for each deployment
+ Timestamp - Data collection timestamp
+ Cost Feature Enabled - Information on whether the user is using the cost feature
+ Number of Accounts - Number of accounts user has onboarded in their deployment
+ Number of Diagrams - Number of diagrams created in each deployment
+ Number of Resources - Number of resources discovered in all onboarded accounts

AWS owns the data gathered through this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the [AWS CloudFormation template](https://solutions-reference.s3.amazonaws.com/workload-discovery-on-aws/latest/workload-discovery-on-aws.template) to your local hard drive.

1. Open the AWS CloudFormation template with a text editor.

1. Modify the AWS CloudFormation template mapping section from:

```
Mappings:
  Solution:
    Metrics:
      CollectAnonymizedUsageMetrics: 'true'
```

to:

```
Mappings:
  Solution:
    Metrics:
      CollectAnonymizedUsageMetrics: 'false'
```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack page**, **Specify template section**, select **Upload a template file.**

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Launch the stack](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/automated-deployment.html).

## Contributors
<a name="contributors"></a>
+ Andrew Price
+ Amr Ahmed
+ Sudeshna Dash
+ Guoneng Zhong
+ John Reynolds
