---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigate-with-resolve-ai.html
---

# Investigate with ResolveAI

ResolveAI is an AI site reliability engineering (SRE) agent, available in AWS Marketplace. When you connect ResolveAI to CloudWatch Omni, members of your space can hand an investigation to ResolveAI from an alert, a chart, or a conversation with the Omni agent. ResolveAI investigates with your space's telemetry and posts the root cause and recommended actions to the investigation in Omni.

For more information about ResolveAI, see the [ResolveAI website](https://resolve.ai/).

**Important**
ResolveAI is a third-party service from an independent company. When you connect ResolveAI, you instruct AWS to share content from your space with ResolveAI. ResolveAI processes that content under its own [terms of service](https://resolve.ai/terms-of-service-product) and [privacy policy](https://resolve.ai/privacy-policy), and is responsible for its data retention, sub-processors, and processing Regions. For details, see the [ResolveAI Trust Center](https://trust.resolve.ai). Review these terms before you connect.

## How ResolveAI works with Omni
<a name="omni-investigate-with-resolve-ai-how-it-works"></a>

When someone in your space starts an investigation with ResolveAI, Omni sends ResolveAI the context for it: the alert or question, the time window, the affected services from the application map, and recent changes. ResolveAI reads the space's logs, traces, and alerts, and the application map if you allow it, through a read-only IAM role that Omni creates in your account. ResolveAI then posts the root cause and recommended actions to the investigation. Your team reviews the recommendations and decides which ones to apply.

Every member of the space can see ResolveAI's findings, which can include excerpts of your logs. ResolveAI reads all of the space's logs, traces, and alerts, independent of the data scopes on member grants. We recommend that you connect ResolveAI to a space whose data every member can already see.

## Before you begin
<a name="omni-investigate-with-resolve-ai-prerequisites"></a>

To connect ResolveAI to your space, verify that you have the following:
+ An Omni space that's receiving telemetry. For more information, see [Set up Omni](omni-set-up-omni.md).
+ The Space Admin permission level in that space. For more information, see [Control access to your space](omni-control-access-to-your-space.md).
+ Permission to create IAM roles in the space's account. Omni creates the role that ResolveAI uses, and the [CloudWatchOmniSpaceAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniSpaceAccessPolicy.html) managed policy includes the permissions for it. If your organization uses service control policies (SCPs), verify that they allow `iam:CreateRole`, `iam:PutRolePolicy`, and `iam:GetRoleTemplateVersion`.
+ A ResolveAI account. You can subscribe in AWS Marketplace during setup. For more information, see [What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html) To use an existing account, sign in as an administrator of your ResolveAI organization.

## Connecting ResolveAI to your space
<a name="omni-investigate-with-resolve-ai-connect"></a>

When you enable ResolveAI for Omni, you enable it for the whole space. As part of the setup, you sign in to ResolveAI, review the access that ResolveAI gets, and complete the connection.

**Step 1: Open Integrations**

1. In CloudWatch Omni, choose **Settings**, and then choose the **Integrations** tab.

1. Under **Sub agents**, in **Third-party agents**, choose **Connect** next to **ResolveAI**.

   The **Connect ResolveAI** panel opens. It describes ResolveAI and how it works with Omni.

**Step 2: Subscribe or sign in**
+ Under **Choose how to connect**, do one of the following:
  + If you're new to ResolveAI, choose **Subscribe on AWS Marketplace** and complete the subscription. Then return to Omni and choose **Sign in with ResolveAI**.
  + If you already use ResolveAI, choose **Sign in with ResolveAI**.

**Step 3: Authorize Amazon CloudWatch in ResolveAI**

1. On the ResolveAI page, sign in with your ResolveAI account.

1. Review the access that Amazon CloudWatch requests, and choose **Allow**.

After authorization, ResolveAI returns you to Omni, which shows the ResolveAI workspace that you signed in to. Omni creates the IAM role that ResolveAI uses. Its name starts with `CloudWatchExternalAgentIntegration-resolve-`. ResolveAI assumes the role from its own AWS account, with an external ID that's unique to your connection.

**Step 4: Review access and connect**

1. Review **What ResolveAI can access**. To choose whether ResolveAI can read the application map, choose **Change what it can read**.

1. Review **Before you connect**.

1. Select **I agree and instruct AWS to share content from this Omni Space with ResolveAI, and to let ResolveAI access content in this Space through the role described above, as configured here. I confirm I am authorized to give this instruction for my organization.**

1. Choose **Connect ResolveAI**.

After you connect, Omni gives the role a read-only access grant in the space. The **Integrations** tab shows ResolveAI as **Connected · read-only**, with your ResolveAI workspace name.

**Note**
Omni manages the IAM role that it creates for ResolveAI. If the role is changed, delete it, and then choose **Finish connecting**. Omni creates the role again.

## Giving members access to ResolveAI
<a name="omni-investigate-with-resolve-ai-let-members-start"></a>

Members start ResolveAI investigations with a grant that includes the `cloudwatch:InvokeIntegration` action for the ResolveAI integration. Omni adds this grant for the Space Admin who connects ResolveAI, when they sign in through IAM Identity Center. Add the grant for the other members who start investigations. For more information, see [Custom grant actions](omni-custom-grant-actions.md).

To use ResolveAI by default when you choose **Investigate**, choose ResolveAI under **Default investigation agent** on the **Personalize** tab in **Settings**.

## Starting an investigation
<a name="omni-investigate-with-resolve-ai-start"></a>

You can start a ResolveAI investigation from an alert, a chart, or a thread:
+ **From an alert** – In the alert's detail panel, choose **Actions**, **Investigate**, and then **ResolveAI**.
+ **From a chart** – Open the chart's menu, and choose **Investigate this signal**. ResolveAI starts from the chart's service or query.
+ **From a thread** – Ask the Omni agent to investigate with ResolveAI. For example: `Investigate why checkout is slow with ResolveAI`.

When more than one agent is connected, **Investigate** lists the agents so that you can choose ResolveAI.

## Viewing results
<a name="omni-investigate-with-resolve-ai-view-results"></a>

ResolveAI investigations appear in the **Investigations** list, with **ResolveAI** in the **Sub agent** column. Choose an investigation to open it. ResolveAI fills in the following sections as it reports:
+ **Problem statement** – What happened, the impact, and the key evidence.
+ **Root cause analysis** – Each root cause that ResolveAI found, with its causal chain and supporting evidence.
+ **Mitigation** – The actions that ResolveAI recommends, for your team to review and apply.
+ **Findings & evidence** – What ResolveAI found, with the evidence for each finding.
+ **Timeline** – How the investigation progressed.

To see ResolveAI's full reasoning, choose **Open in ResolveAI**, and sign in with your ResolveAI account.

**Important**
ResolveAI uses generative AI to produce its findings. Verify findings before you act on them.

## Reviewing ResolveAI's access
<a name="omni-investigate-with-resolve-ai-review-access"></a>

To see what ResolveAI can access, go to the **Integrations** tab in **Settings**, and choose **Manage** for ResolveAI. The panel shows the connection status, your ResolveAI workspace, the IAM role, the data that ResolveAI can read, and its permissions.

AWS CloudTrail logs each query that ResolveAI runs as a session of the ResolveAI role.

## Disconnecting ResolveAI
<a name="omni-investigate-with-resolve-ai-disconnect"></a>

You can revoke ResolveAI's access at any time. Revoking access requires permission to list and delete access grants, which the Space Admin permission level includes.

**To disconnect ResolveAI**

1. On the **Integrations** tab in **Settings**, choose **Manage** for ResolveAI.

1. For **Actions**, choose **Revoke access**.

1. To confirm, choose **Revoke access**.

When you revoke access, Omni removes ResolveAI's access grant and the members' ResolveAI grants, and disconnects your ResolveAI workspace. Completed investigations stay in Omni. The IAM role that Omni created stays in your account, and you can delete it in IAM.

## Troubleshooting
<a name="omni-investigate-with-resolve-ai-troubleshooting"></a>

If the connection stops before it completes, the **Integrations** tab shows **Connection not finished**. Choose **Manage**, fix the cause, and then choose **Actions**, **Finish connecting**. To start over, choose **Revoke access**.

The following table lists the errors that you might see when you connect or disconnect ResolveAI.

| Error | Cause | Solution |
| --- | --- | --- |
| CONNECTION\_EXISTS | ResolveAI is already connected in this account and Region. | Use the existing connection, or revoke access and connect again. |
| AUTHORIZATION\_FAILED | The sign-in expired, was used more than once, or was completed by a different identity. | Choose Connect, and sign in again. |
| PARTNER\_NOT\_AVAILABLE | ResolveAI needs to be enabled for this account. | Contact your AWS account team. |
| ROLE\_CREATION\_NOT\_PERMITTED | Omni needs permission to create the role. For the permissions, see [Before you begin](#omni-investigate-with-resolve-ai-prerequisites). | Ask your IAM administrator for the permissions, and then choose Finish connecting. |
| ROLE\_NAME\_TAKEN | Another role already uses the name of the ResolveAI role. | Delete or rename that role, and then choose Finish connecting. |
| ROLE\_EDITED | The role that Omni created was changed. | Delete the role, and then choose Finish connecting. Omni creates the role again. |
| ROLE\_LIMIT\_EXCEEDED | Your account reached its quota for IAM roles. | Delete unused roles, or request a quota increase. Then choose Finish connecting. |
| PARTNER\_PERMISSION\_DENIED | Connecting requires an administrator of your ResolveAI organization. | Revoke access, and connect again as a ResolveAI administrator. |
| PARTNER\_API\_NOT\_ENABLED | Your ResolveAI organization needs this integration enabled. | Contact ResolveAI. |
| PARTNER\_CREDENTIAL\_REJECTED | ResolveAI rejected the connection, for example after access was revoked in ResolveAI. | Revoke access, and connect again. |
| PARTNER\_UNAVAILABLE, PARTNER\_PROTOCOL\_ERROR | ResolveAI was unavailable, or returned an unexpected response. | Choose Finish connecting again. |
| GRANTS\_ACCESS\_DENIED | Revoking access requires permission to delete the access grants for the ResolveAI role. | Ask a Space Admin to revoke access. |
| CONCURRENT\_UPDATE | Someone connected and revoked access at the same time. | Try again. |

ResolveAI appears in the **Investigate** menu when the **Integrations** tab shows it as **Connected** and your grant includes `cloudwatch:InvokeIntegration` for the ResolveAI integration. To reset the connection, revoke access and connect again.
