---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/disabling-eks-runtime-monitoring.html
---

# Disabling EKS Runtime Monitoring after migrating to Runtime Monitoring
<a name="disabling-eks-runtime-monitoring"></a>

After you have ensured that the existing settings for your account or organization have been replicated to Runtime Monitoring, you can disable EKS Runtime Monitoring.

**To disable EKS Runtime Monitoring**
+ **To disable EKS Runtime Monitoring in your own account**

  Run the [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API with your own regional {{detector-id}}.

  Alternatively, you can use the following AWS CLI command. Replace {{12abc34d567e8fa901bc2d34e56789f0}} with your own regional {{detector-id}}.

  ```
  aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --features '[{"Name" : "EKS_RUNTIME_MONITORING", "Status" : "DISABLED"}]'
  ```
+ **To disable EKS Runtime Monitoring for member accounts in your organization**

  Run the [UpdateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API with the regional {{detector-id}} of the delegated GuardDuty administrator account of the organization.

  Alternatively, you can use the following AWS CLI command. Replace {{12abc34d567e8fa901bc2d34e56789f0}} with the regional {{detector-id}} of the delegated GuardDuty administrator account of the organization and {{111122223333}} with the AWS account ID of the member account for which you want to disable this feature.

  ```
  aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --account-ids {{111122223333}} --features '[{"Name" : "EKS_RUNTIME_MONITORING", "Status" : "DISABLED"}]'
  ```
+ **To update EKS Runtime Monitoring auto-enable settings for your organization**

  Perform the following step only if you have configured the EKS Runtime Monitoring auto-enablement settings to either new (`NEW`) or all (`ALL`) member accounts in the organization. If you had already configured it as `NONE`, then you can skip this step.
**Note**
Setting the EKS Runtime Monitoring auto-enable configuration to `NONE` means that EKS Runtime Monitoring will not be enabled automatically for any existing member account or when a new member account joins your organization.

  Run the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API with the regional {{detector-id}} of the delegated GuardDuty administrator account of the organization.

  Alternatively, you can use the following AWS CLI command. Replace {{12abc34d567e8fa901bc2d34e56789f0}} with the regional {{detector-id}} of the delegated GuardDuty administrator account of the organization. Replace the {{EXISTING\_VALUE}} with your current configuration for auto-enabling GuardDuty.

  ```
  aws guardduty update-organization-configuration --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --auto-enable-organization-members {{EXISTING_VALUE}} --features '[{"Name" : "EKS_RUNTIME_MONITORING", "AutoEnable": "NONE"}]'
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
