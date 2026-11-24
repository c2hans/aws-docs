---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/meta-ads-integration.html
---

# Meta ads integration

Meta ads is Meta's advertising platform for Facebook, Instagram, Messenger, and the Audience Network. The Meta ads AI connector gives AWS Quick access to the ads Model Context Protocol (MCP) server. You can create, manage, and analyze campaigns in natural language without switching to Ads Manager. For example, you can review last week's campaign performance, find underperforming ad sets, check catalog health, or draft a new campaign.

The connector is available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Sydney), and Asia Pacific (Tokyo).

You can use two authentication methods for Meta ads. Choose the method that best fits your organization's security requirements:
+ **Default OAuth app** – Uses a Meta app managed by AWS. No additional credentials are needed. Users sign in directly with their Facebook account.
+ **Custom OAuth app** – Uses a Meta app that your organization owns. This option gives your organization full control over the app, including its permissions and App Review.

For more information about the authentication methods that AWS Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="meta-ads-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration:
+ A Meta business account with access to the ad accounts that you want to connect. To create or change campaigns, your role on the ad account must allow editing, such as **Advertiser** or **Admin**.
+ For **Custom OAuth app**: A Meta developer account and a Meta app with the **Create & manage ads with ads MCP server** use case. The app must list the AWS Quick callback URL as a valid OAuth redirect URI. For instructions, see [Configuring Meta](#meta-ads-source-setup).
+ For AWS Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Meta
<a name="meta-ads-source-setup"></a>

If you're using **Default OAuth app** authentication, skip this section and see [Setting up the connector in AWS Quick](#meta-ads-quicksuite-setup).

For Custom OAuth app authentication, create a Meta app and configure it to work with AWS Quick.

1. Sign in to [Meta for Developers](https://developers.facebook.com/), and then create a new app or open an existing one.

1. Add the **Create & manage ads with ads MCP server** use case.

1. Under **Facebook Login for Business** > **Settings**, for **Valid OAuth Redirect URIs**, enter the AWS Quick callback URL. Replace {{region}} with your AWS Region, for example `us-east-1`:

   `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`

   If you use AWS Quick at `quick.aws.com`, also add `https://quick.aws.com/sn/oauthcallback`.

1. Request the permissions that the connector uses. The minimum permissions are `ads_mcp_management` and `ads_read`. To use every tool in AWS Quick, also request `ads_management`, `business_management`, `catalog_management`, `pages_show_list`, `pages_manage_ads`, and `instagram_basic`. Users who don't have a role on your app can sign in only after Meta grants Advanced Access through App Review.

1. Under **App settings** > **Basic**, record the **App ID** and **App secret**. You need these values when you configure the connector in AWS Quick.

**Development mode**
While a Meta app is in **Development** mode, only Facebook users who have a role on the app (admin, developer, or tester) can connect. Switch the app to **Live** after Meta approves App Review.

For more information, see [Create an app](https://developers.facebook.com/docs/development/create-an-app/) and [App Review](https://developers.facebook.com/docs/app-review/) on the Meta for Developers website.

## Setting up the connector in AWS Quick
<a name="meta-ads-quicksuite-setup"></a>

You can connect from the **Available** tab with Default OAuth app authentication, or create a connector for your team with either authentication method.

### Connect from the Available tab
<a name="meta-ads-quick-connect"></a>

To use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the AWS Quick console, choose **Customize**, and then choose **Connectors**.

1. On the **Available** tab, find **Meta ads** and choose **Connect**.

1. Sign in with Facebook. Choose the Pages, businesses, Instagram accounts, and ad accounts that AWS Quick can access. Grant the requested permissions, and then choose **Continue**.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab, as described in the following section.

### Create a connector for your team
<a name="meta-ads-full-setup"></a>

Use the **Create for your team** tab to create a connector with either authentication method.

1. In the AWS Quick console, choose **Customize**, and then choose **Connectors**.

1. On the **Create for your team** tab, find and choose **Meta ads**.

1. For **Name**, enter a name for your connector.

1. (Optional) Choose **\+ Add Description**, and then enter a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields:

   1. For **Default OAuth app**, no additional credentials are needed.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The App ID from your Meta app.
      + **Client secret** – The App secret from your Meta app.
      + **Token URL** – The token endpoint. Default: `https://graph.facebook.com/v23.0/oauth/access_token`
      + **Authorization URL** – The authorization endpoint. Default: `https://www.facebook.com/v23.0/dialog/oauth`
      + **Redirect URL** – Prefilled with the AWS Quick callback URL. Make sure that this exact URL is in your Meta app's **Valid OAuth Redirect URIs**. If it's missing or differs, for example in the Region, Facebook rejects the sign-in with a redirect URI error.

1. Choose **Next**.

To finish, authorize and publish the connector as described in the following section.

### Authorize and publish the connector
<a name="meta-ads-authorize-publish"></a>

After you choose **Next**, a Facebook authorization window opens.

1. In the Facebook authorization window, choose the Pages, businesses, Instagram accounts, and ad accounts that AWS Quick can access. Review the requested permissions, and then choose **Continue**.

1. On the **Review** page, review the available actions for the connector, and then choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization, or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="meta-ads-integration-actions"></a>

After you set up the connector, you can use Meta ads tools in AWS Quick to analyze and manage your advertising. Meta updates the tool set regularly, so the exact list in your connector can differ. The tools fall into the following groups:

**Meta ads tool groups**

| Group | What you can do |
| --- | --- |
| Accounts and assets | List ad accounts, Pages, Instagram accounts, ad images and videos, and an ad account's activity log. |
| Campaigns, ad sets, and ads | View your campaign structure, preview ads, and create, update, activate, or pause campaigns, ad sets, ads, and creatives. |
| Performance insights | View performance trends, anomaly signals, auction ranking, industry benchmarks, and opportunity scores. |
| Audiences | View, create, and update custom audiences. |
| Catalogs | Manage product catalogs, product sets, feeds, and feed rules, and check catalog and dynamic ads health. |
| Measurement | Read and manage pixel events and parameters, datasets, and custom conversions, and run A/B and lift tests. |
| Help | Search the Ad Library and Meta's help articles. |

**Changes and ad spend**
The connector can make changes in your ad accounts that can affect ad spend. Before AWS Quick creates a campaign, changes a budget, or runs another write action, it asks for your permission. Read-only actions, such as pulling performance insights, run without asking. Meta creates new campaigns, ad sets, and ads as paused. They don't deliver until you activate them.

For more information about the Meta ads MCP server, see [Connect an MCP client to Meta](https://developers.facebook.com/documentation/mcp/connect-an-mcp-client) on the Meta for Developers website.

## Managing and troubleshooting
<a name="meta-ads-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

The following issues can occur when you set up or use the connector.

### Sign-in fails
<a name="meta-ads-troubleshoot-signin"></a>

Verify that you can sign in to Facebook directly and that your account has access to at least one ad account. For Custom OAuth app, confirm that the **Valid OAuth Redirect URIs** in your Meta app match the AWS Quick callback URL.

### App isn't available during sign-in
<a name="meta-ads-troubleshoot-app-unavailable"></a>

This issue applies to Custom OAuth app. Meta shows an app not available error when the Meta app is in **Development** mode and the user doesn't have a role on it. Add the user as a tester, or switch the app to **Live** after Meta approves App Review.

### Invalid client credentials
<a name="meta-ads-troubleshoot-credentials"></a>

This issue applies to Custom OAuth app. Verify that the Client ID and Client secret match the App ID and App secret in your Meta app.

### Insufficient permissions
<a name="meta-ads-troubleshoot-permissions"></a>

If actions return authorization errors, verify that the user granted the requested permissions and selected the right ad accounts during sign-in. Also verify that the Meta app has Advanced Access for those permissions. To change what you shared, disconnect and sign in again.

### An ad account is missing
<a name="meta-ads-troubleshoot-missing-account"></a>

During Facebook sign-in, Meta shares only the businesses and ad accounts that you select. Disconnect, sign in again, and select the missing account.
