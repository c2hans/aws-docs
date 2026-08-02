---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html
---

# Managing security agent automatically for Amazon EKS resources
<a name="managing-gdu-agent-eks-automatically"></a>

Runtime Monitoring supports enabling the security agent through GuardDuty automated configuration and manually. This section provides the steps to enable automated agent configuration for Amazon EKS clusters.

Before proceeding, make sure that you have followed the [Prerequisites for Amazon EKS cluster support](prereq-runtime-monitoring-eks-support.md).

Based on your preferred approach on how to [Manage security agent through GuardDuty](how-runtime-monitoring-works-eks.md#eks-runtime-using-gdu-agent-management-auto), choose the steps in the following sections accordingly.

## Configuring Automated agent for multi-account environments
<a name="eks-runtime-monitoring-agent-manage-multiple-account"></a>

In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable Automated agent configuration for the member accounts, and manage Automated agent for the EKS clusters belonging to the member accounts in their organization. The GuardDuty member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account account manages their member accounts using AWS Organizations. For more information about multi-account environments, see [Managing multiple accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

### Configuring Automated agent configuration for delegated GuardDuty administrator account
<a name="eks-runtime-configure-agent-delegated-admin"></a>

| **Preferred approach to manage GuardDuty security agent** | **Steps** |
| --- | --- |
| Manage security agent through GuardDuty<br />(Monitor all EKS clusters) | If you chose **Enable for all accounts** in the Runtime Monitoring section, then you have the following options:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)<br />If you chose **Configure accounts manually** in the Runtime Monitoring section, then do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)<br />Choose **Save**. |
| Monitor all EKS clusters but exclude some of them (using exclusion tags) | From the following procedures, choose one of the scenarios that apply to you.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor selective EKS clusters using inclusion tags | Regardless of how you chose to enable Runtime Monitoring, the following steps will help you monitor selective EKS clusters in your account:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Manage the GuardDuty security agent manually | Regardless of how you chose to enable Runtime Monitoring, you can manage the security agent manually for your EKS clusters.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |

### Auto-enable Automated agent for all member accounts
<a name="eks-runtime-monitoring-agent-auto-enable-existing-member-accounts"></a>

**Note**
It may take up to 24 hours to update the configuration for the member accounts.

| **Preferred approach to manage GuardDuty security agent** | **Steps** |
| --- | --- |
| Manage security agent through GuardDuty<br />(Monitor all EKS clusters) | This topic is to enable Runtime Monitoring for all member accounts and therefore, the following steps assume that you must have chosen **Enable for all accounts** in the Runtime Monitoring section.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor all EKS clusters but exclude some of them (using exclusion tags) | From the following procedures, choose one of the scenarios that apply to you.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor selective EKS clusters using inclusion tags | Regardless of how you chose to enable Runtime Monitoring, the following steps will help you monitor selective EKS clusters for all member accounts in your organization:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Manage the GuardDuty security agent manually | Regardless of how you chose to enable Runtime Monitoring, you can manage the security agent manually for your EKS clusters.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |

### Enabling automated agent for all existing active member accounts
<a name="eks-runtime-monitoring-agent-all-active-members"></a>

**Note**
It may take up to 24 hours to update the configuration for the member accounts.

**To manage GuardDuty security agent for existing active member accounts in your organization**
+ For GuardDuty to receive the runtime events from the EKS clusters that belong to the existing active member accounts in the organization, you must choose a preferred approach to manage the GuardDuty security agent for these EKS clusters. For more information about each of these approaches, see [Approaches to manage GuardDuty security agent in Amazon EKS clusters](how-runtime-monitoring-works-eks.md#eksrunmon-approach-to-monitor-eks-clusters).
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)

### Auto-enable automated agent configuration for new members
<a name="eks-runtime-monitoring-agent-auto-enable-new-members"></a>

| **Preferred approach to manage GuardDuty security agent** | **Steps** |
| --- | --- |
| Manage security agent through GuardDuty<br />(Monitor all EKS clusters) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)  |
| Monitor all EKS clusters but exclude some of them (using exclusion tags) | From the following procedures, choose one of the scenarios that apply to you.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor selective EKS clusters using inclusion tags | Regardless of how you chose to enable Runtime Monitoring, the following steps will help you monitor selective EKS clusters for the new member accounts in your organization.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Manage the GuardDuty security agent manually | Regardless of how you chose to enable Runtime Monitoring, you can manage the security agent manually for your EKS clusters.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |

### Configuring Automated agent for active member accounts selectively
<a name="eks-runtime-monitoring-agent-selectively-member-accounts"></a>

| **Preferred approach to manage GuardDuty security agent** | **Steps** |
| --- | --- |
| Manage security agent through GuardDuty<br />(Monitor all EKS clusters) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor all EKS clusters but exclude some of them (using exclusion tags) | From the following procedures, choose one of the scenarios that apply to you.[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Monitor selective EKS clusters using inclusion tags | Regardless of how you chose to enable Runtime Monitoring, the following steps will help you monitor selective EKS clusters that belong to the selected accounts:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html) |
| Manage the GuardDuty security agent manually | [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)  |

## Configuring Automated agent for standalone account
<a name="eks-runtime-monitoring-agent-manage-standalone-account"></a>

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to your account. For more information, see [Enabling Runtime Monitoring for multiple-account environments](enable-runtime-monitoring-multiple-acc-env.md).

After you enable Runtime Monitoring, ensure to install GuardDuty security agent through automated configuration or manual deployment. As a part of completing all the steps listed in the following procedure, make sure to install the security agent.

Based on your preference to monitor all or selective Amazon EKS resources, choose a preferred method and follow the steps in the following table.

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. Under the **Configuration** tab, choose **Enable** to enable automated agent configuration for your account.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)
