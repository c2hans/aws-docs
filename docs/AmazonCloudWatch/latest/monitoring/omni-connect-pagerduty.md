---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-connect-pagerduty.html
---

# Connect PagerDuty

An integration connects Amazon CloudWatch Omni to a tool your team already uses. When you connect PagerDuty, your alerts can page your on-call responders through the PagerDuty services and escalation policies that you already have. You manage the integration in **Settings**, on the **Integrations** page. Your connection applies to your whole space.

After you connect PagerDuty and add services, you choose the service on each alert when you set its destinations. For information about alert destinations, see [Alerts](omni-alerts.md).

The alert's access profile must also grant this integration, or Omni doesn't deliver the alert's notifications. Omni checks the grant when you save the alert's notifications and again on every delivery, so revoking it stops notifications for alerts that were already working. If an alert fires but no incident opens in PagerDuty, check the profile. For information about profiles, see [Access profiles](omni-access-profiles.md).

Within one Region, an AWS account can have one PagerDuty connection. To connect a different PagerDuty account, disable the integration and connect again.

## Install the Amazon CloudWatch Omni app in PagerDuty
<a name="omni-connect-pagerduty-install-app"></a>

A PagerDuty Admin or the Account Owner must install the Amazon CloudWatch Omni app on your PagerDuty account before anyone in your space connects PagerDuty for the first time. You install it once for each PagerDuty account. After an Admin installs the app, anyone in your space can connect PagerDuty.

To go straight to the app in PagerDuty, open the [Amazon CloudWatch Omni app install page for US accounts](https://app.pagerduty.com/oauth-apps/PESW2TW) or the [Amazon CloudWatch Omni app install page for EU accounts](https://app.eu.pagerduty.com/oauth-apps/PESW2TW), and then follow the last step of the following procedure.

**To install the app**

1. In **Settings**, choose **Integrations**.

1. On the **PagerDuty** card, for **Service region**, select the service region of your PagerDuty account.

1. Choose **Install the app in PagerDuty**. The app's page opens in PagerDuty.

1. Sign in as a PagerDuty Admin or the Account Owner, review the scopes, and choose **Install on your account**. If you aren't an Admin, choose **Copy install link** and send it to an Admin.

PagerDuty installs the app and opens the app's page in your PagerDuty account. You can now connect PagerDuty.

For more information, see [Scoped OAuth apps](https://docs.pagerduty.com/integrations/apps/scoped-oauth-apps) in the PagerDuty documentation.

## Connect your PagerDuty account
<a name="omni-connect-pagerduty-connect"></a>

**To connect PagerDuty**

1. In **Settings**, choose **Integrations**.

1. On the **PagerDuty** card, for **Service region**, select the service region of your PagerDuty account. Select **EU** if you sign in to PagerDuty at a `.eu.pagerduty.com` address. Otherwise, select **US**.

1. Choose **Enable**. PagerDuty opens.

1. Sign in to PagerDuty and approve the Amazon CloudWatch Omni app for your PagerDuty account. If Omni then says that PagerDuty didn't grant access, ask a PagerDuty Admin to install the app, and then connect again. For instructions on installing the app, see [Install the Amazon CloudWatch Omni app in PagerDuty](#omni-connect-pagerduty-install-app).

Back in Omni, the **PagerDuty** card shows **Connected**, with the PagerDuty account, its service region, and the integration's ARN. If the card says that the sign-in took too long or didn't complete, choose **Enable** again.

## Add the services that Omni can page
<a name="omni-connect-pagerduty-add-services"></a>

Connecting doesn't add any services. An alert can page only a service that you add this way, and other services don't appear in the service list.

**To add services**

1. On the connected **PagerDuty** card, choose **Add services**. PagerDuty opens.

1. Select the services. PagerDuty adds an integration for the Amazon CloudWatch Omni app to each one.

1. When PagerDuty says that the services were added, close the tab and return to Omni.

You can add more services at any time, from the card or from the link under the service list on an alert's PagerDuty destination.

## What Omni can access in PagerDuty
<a name="omni-connect-pagerduty-what-omni-can-access"></a>

You give Omni read-only access to your PagerDuty account, with the `services.read` and `event_orchestrations.read` scopes. Omni reads your services to offer them as destinations, and reads the routing key of the Amazon CloudWatch Omni app's integration on a service when it sends a notification. Omni can't change your PagerDuty configuration. Events for an EU account stay in PagerDuty's EU service region.

## Grant the alert's profile access to PagerDuty
<a name="omni-connect-pagerduty-grant-access"></a>

If you save a PagerDuty notification rule before the alert's access profile has the grant, Omni rejects the save. Choose **Grant permission** to open the add-grant form already filled in for the alert's profile, and then save the rule again. A new grant can take a few minutes to take effect.

The grant allows `cloudwatch:InvokeIntegration` on the PagerDuty integration's ARN, and can limit it to specific services by their service IDs. If you author grants through the API instead of the console, replace these values in the following example with your own:
+ {{region}}, {{account-id}}, and {{integration-id}}: the parts of your PagerDuty integration's ARN.
+ {{PABC123}} and {{PDEF456}}: the IDs of the PagerDuty services that the alert can page.

The following example grant allows `cloudwatch:InvokeIntegration` on a PagerDuty integration, limited to two services:

```json
{
  "name": "pagerduty-alert-integration",
  "permission": "CUSTOM",
  "scopedActions": [
    {
      "actions": ["cloudwatch:InvokeIntegration"],
      "resources": [
        {
          "resourceType": "Integration",
          "resourceArns": ["arn:aws:cloudwatch:{{region}}:{{account-id}}:integration/{{integration-id}}"]
        }
      ],
      "contextConditions": { "serviceIds": ["{{PABC123}}", "{{PDEF456}}"] }
    }
  ]
}
```
+ To allow every service in the PagerDuty account, leave out `contextConditions`.
+ One `scopedActions` entry can restrict `channelNames` or `serviceIds`, but not both. Grant Slack and PagerDuty in separate entries.

## Events that PagerDuty receives
<a name="omni-connect-pagerduty-events"></a>

Omni sends one PagerDuty Events API v2 event for each alert state that a rule notifies on.

The following table shows the event action and severity that Omni sends to PagerDuty for each alert state.

| Alert state | Event action | Severity |
| --- | --- | --- |
| Critical | trigger | critical |
| Warning | trigger | warning |
| No data | trigger | error |
| OK | resolve | info |

By default, all events from one alert share a deduplication key, the alert's ARN, so each alert opens one incident. A later Critical event raises the incident's severity, and an OK event resolves it. To resolve incidents automatically, include OK in the rule's alert states. In the rule's **PagerDuty additional settings**, you can set your own deduplication key, which Omni uses instead of the alert's ARN, and the class, group, and component fields that PagerDuty event rules match on.

## Disconnect an integration
<a name="omni-connect-pagerduty-disconnect-an-integration"></a>

On the integration's card in **Settings**, on the **Integrations** page, choose **Disable**. When you disconnect PagerDuty, you stop alert notifications to PagerDuty. The alerts themselves keep evaluating, and their other destinations keep working. You can reconnect with **Enable**. Disconnecting doesn't remove the grants on the integration or the Amazon CloudWatch Omni app's integrations on your PagerDuty services.

## Who can manage integrations
<a name="omni-connect-pagerduty-who-can-manage-integrations"></a>

Integrations apply to the whole space. One person connects, and the connection works for everyone in the space. Whether a member can connect, change, or disconnect an integration is governed by their grants: the integration create, update, and delete actions. See [Custom grant actions](omni-custom-grant-actions.md).
