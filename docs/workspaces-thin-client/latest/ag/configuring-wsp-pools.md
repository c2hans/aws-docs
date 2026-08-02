---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-wsp-pools.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Configuring WorkSpaces Pools for WorkSpaces Thin Client
<a name="configuring-wsp-pools"></a>

For WorkSpaces Thin Client to be used with Amazon WorkSpaces Pools, your SAML 2.0 identity provider (IdP) will need to be configured to access the WorkSpaces Pools directory. Amazon WorkSpaces Pools directories are a non-persistent pool of WorkSpaces assigned to a group of users.

**Note**
Configurations must be made before using the console for the first time.

## Before you begin
<a name="configuring-wsp-pools-before-begin"></a>

Make sure that you have an AWS account to create or administer a WorkSpace. Device users, however, don't need an AWS account to connect to and use their WorkSpaces.

Review and understand the concepts listed in [ Before You Begin Using Active Directory with WorkSpaces Pools](https://docs.aws.amazon.com//workspaces/latest/adminguide/active-directory-prerequisites.html) in the *Amazon WorkSpaces Administration Guide* before you proceed with your configuration.

## Create a WorkSpaces Pool
<a name="create-wsp-pool"></a>

Set up and create a pool from which user applications are launched and streamed.

**Note**
You should create a directory before you create a WorkSpaces Pool. For more information, see [ Configure SAML 2.0 and create a WorkSpaces Pools directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-directory-pools.html) directory.

**To set up and create a pool**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home/](https://console.aws.amazon.com/workspaces/v2/home/).

1. In the navigation pane, choose **WorkSpaces**, **Pools**.

1. Choose **Create WorkSpaces Pools**.

1. Under **Onboarding** (optional), you can choose **Recommend options to me based on my use case** to get recommendations on the type of WorkSpaces you want to use. You can skip this step if you know that you want to use WorkSpaces Pools.

1. Under **Configure WorkSpaces**, enter the following details:
   + For **Name**, enter a unique name identifier for the pool. Special characters aren't allowed.
   + For **Description**, enter a description for the pool (maximum of 256 characters).
   + For **Bundle**, choose from the following the bundle type that you want to use for your WorkSpaces.
     + **Use a base WorkSpaces bundle** – Choose one of the bundles from the drop down. For more information about the bundle type you selected, choose **Bundle details**. To compare bundles offered for pools, choose **Compare all bundles**.
     + **Use your own custom bundle** – Choose a bundle that you previously created. To create a custom bundle, see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html).
**Note**
BYOL is currently unavailable for WorkSpaces Pools.
   + For **Maximum session duration in minutes**, choose the maximum amount of time that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance. The maximum session duration that you can set in the WorkSpaces Pools console is 5760 minutes (96 hours). The maximum session duration that you can set using the WorkSpaces Pools API and CLI is 432000 seconds (120 hours).
   + For **Disconnect timeout in minutes**, choose the amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
   + If a user ends the session by choosing **End Session** or **Logout** on the pools toolbar, the disconnect timeout doesn’t apply. Instead, the user is prompted to save any open documents, and then immediately disconnected from the streaming instance. The instance the user was using is then terminated.
   + For **Idle disconnect timeout in minutes**, choose the amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the **Disconnect timeout in minutes** time interval begins. Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in **Disconnect timeout in minutes** has elapsed, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. Setting this value to 0 disables it. When this value is disabled, users are not disconnected due to inactivity.
**Note**
Users are considered idle when they stop providing keyboard or mouse input during their streaming session. For domain-joined pools, the countdown for the idle disconnect timeout doesn't begin until users log in with their Active Directory domain password or with a smart card. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in **Idle disconnect timeout in minutes** elapses, they are disconnected.
   + For **Scheduled capacity policies** (optional), choose **Add new schedule capacity**. Indicate the start and end date and time for when to provision the minimum and maximum number of instances for your pool based on the minimum number of expected concurrent users.
   + For **Manual scaling policies** (optional), specify the scaling policies for pools to use to increase and decrease the capacity of your pool. **Expand Manual** scaling policies to add new scaling policies.
**Note**
The size of your pool is limited by the minimum and maximum capacity that you specified.
     + Choose **Add new scale out policies** and enter the values for adding specified instances if the specified capacity utilization is less or more than the specified threshold value.
     + Choose **Add new scale in policies** and enter the values for removing specified instances if the specified capacity utilization is less or more than the specified threshold value.
   + For **Tags**, specify the key pair value that you want to use. A key can be a general category, such as "project," "owner," or "environment," with specific associated values.

1. On the **Select directory page**, choose the directory that you created. To create a directory, choose **Create directory**. For more information, see [Manage directories for WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-pools-directory.html).

1. Choose **Create WorkSpace Pool**.

## Configuring WorkSpaces Thin Client access
<a name="configure-web-pools"></a>

Configuring web access for WorkSpaces Pools to use WorkSpaces Thin Client, you will need to use the AWS command land interface.

1. Install or update the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Configure your [AWS CLI settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

1. Open the AWS CLI.

1. Run the following replacing `WORKSPACES_DIRECTORY_ID` and `REGION` with the appropriate information:

   ```
   aws workspaces modify-workspace-access-properties --resource-id {{WORKSPACES_DIRECTORY_ID}}  --workspace-access-properties '{"DeviceTypeWorkSpacesThinClient":"ALLOW"}' --region {{REGION}}
   ```
