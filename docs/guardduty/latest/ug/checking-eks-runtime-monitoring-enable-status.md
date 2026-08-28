---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/checking-eks-runtime-monitoring-enable-status.html
---

# Checking EKS Runtime Monitoring configuration status
<a name="checking-eks-runtime-monitoring-enable-status"></a>

Use the following APIs or AWS CLI commands to check the existing configuration status of EKS Runtime Monitoring.

**To check existing EKS Runtime Monitoring configuration status in your account**
+ Run [GetDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetDetector.html) to check the configuration status of your own account.
+ Alternatively, you can run the following command by using AWS CLI:

  ```
  aws guardduty get-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}}
  ```

  Make sure to replace the detector ID of your AWS account and the current Region. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

**To check existing EKS Runtime Monitoring configuration status for your organization (as a delegated GuardDuty administrator account only)**
+ Run [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html) to check the configuration status of your organization.

  Alternatively, you can run the following command using AWS CLI:

  ```
  aws guardduty describe-organization-configuration --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}}
  ```

  Make sure to replace the detector ID with the detector ID of your delegated GuardDuty administrator account and the Region with your current Region. To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
