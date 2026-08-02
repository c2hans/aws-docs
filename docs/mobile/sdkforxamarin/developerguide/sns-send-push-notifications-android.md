---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns-send-push-notifications-android.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Send Push Notifications (Xamarin Android)
<a name="sns-send-push-notifications-android"></a>

This document explains how to send push notifications to a Xamarin Android application using Amazon Simple Notification Service (SNS) and the AWS Mobile SDK for .NET and Xamarin.

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

You must complete all of the instructions on the [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) before beginning this tutorial.

### Set Permissions for SNS
<a name="set-permissions-for-sns"></a>

Follow Step 2 in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to attach the policy mentioned below to your application’s roles. This will give your application the proper permissions to access SNS:

1. Go to the [IAM Console](https://console.aws.amazon.com/iam/home) and select the IAM role that you want to configure.

1. Click **Attach Policy**, select the AmazonSNSFullAccess policy and click **Attach Policy**.

**Warning**
Using AmazonSNSFullAccess is not recommended in a production environment. We use it here to allow you to get up and running quickly. For more information about specifying permissions for an IAM role, see [Overview of IAM Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_permissions.html).

### Enable Push Notifications on Google Cloud
<a name="enable-push-notifications-on-google-cloud"></a>

First, add a new Google API project:

1. Go to the [Google Developers Console](https://console.developers.google.com).

1. Click **Create Project**.

1. In the **New Project** box, enter a project name, take note of the project ID (you will need it later) and click **Create**.

Next, enable the Google Cloud Messaging (GCM) service for your project:

1. In the [Google Developers Console](https://console.developers.google.com), your new project should already be selected. If not, select it in the drop-down at the top of the page.

1. Select **APIs & auth** from the side bar on the left-hand side of the page.

1. In the search box, type “Google Cloud Messaging for Android” and click the **Google Cloud Messaging for Android** link.

1. Click **Enable API**.

Finally, obtain an API Key:

1. In the Google Developers Console, select **APIs & auth** > **Credentials**.

1. Under **Public API access**, click **Create new key**.

1. In the **Create a new key** dialog, click **Server key**.

1. In the resulting dialog, click **Create** and copy the API key displayed. You will use this API key to perform authentication later on.

### Use Project ID to Create a Platform ARN in SNS Console
<a name="use-project-id-to-create-a-platform-arn-in-sns-console"></a>

1. Go to the [SNS Console](https://console.aws.amazon.com/sns/v2/home).

1. Click **Applications** on the left-hand side of the screen.

1. Click **Create platform application** to create a new SNS platform application.

1. Enter an **Application Name**.

1. Select **Google Cloud Messaging (GCM)** for **Push notification platform**.

1. Paste the API key into the text box labeled **API key**.

1. Click **Create platform application**.

1. Select the Platform Application you just created and copy the Application ARN.

### Add NuGet Package for SNS to Your Project
<a name="add-nuget-package-for-sns-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the Amazon Simple Notification Service NuGet package to your project.

## Create an SNS client
<a name="create-an-sns-client"></a>

```
var snsClient = new AmazonSimpleNotificationServiceClient(credentials, region);
```

## Register Your Application for Remote Notifications
<a name="register-your-application-for-remote-notifications"></a>

In order to register for remote notifications on Android, you will need to create a BroadcastReceiver which can receive Google Cloud messages. Change the package name below where prompted to do so:

```
[BroadcastReceiver(Permission = "com.google.android.c2dm.permission.SEND")]
[IntentFilter(new string[] {
      "com.google.android.c2dm.intent.RECEIVE"
}, Categories = new string[] {
      "com.amazonaws.sns" /* change to match your package */
})]
[IntentFilter(new string[] {
      "com.google.android.c2dm.intent.REGISTRATION"
}, Categories = new string[] {
      "com.amazonaws.sns" /* change to match your package */
})]
[IntentFilter(new string[] {
      "com.google.android.gcm.intent.RETRY"
}, Categories = new string[] {
      "com.amazonaws.sns" /* change to match your package */
})]
public class GCMBroadcastReceiver: BroadcastReceiver {
      const string TAG = "PushHandlerBroadcastReceiver";
      public override void OnReceive(Context context, Intent intent) {
              GCMIntentService.RunIntentInService(context, intent);
              SetResult(Result.Ok, null, null);
      }
}

[BroadcastReceiver]
[IntentFilter(new[] {
      Android.Content.Intent.ActionBootCompleted
})]
public class GCMBootReceiver: BroadcastReceiver {
      public override void OnReceive(Context context, Intent intent) {
              GCMIntentService.RunIntentInService(context, intent);
              SetResult(Result.Ok, null, null);
      }
}
```

Below is the service that receives the push notification from the BroadcastReceiver and displays the notification on the device’s notification bar:

```
[Service]
 public class GCMIntentService: IntentService {
  static PowerManager.WakeLock sWakeLock;
  static object LOCK = new object();

  public static void RunIntentInService(Context context, Intent intent) {
    lock(LOCK) {
      if (sWakeLock == null) {
        // This is called from BroadcastReceiver, there is no init.
        var pm = PowerManager.FromContext(context);
        sWakeLock = pm.NewWakeLock(
        WakeLockFlags.Partial, "My WakeLock Tag");
      }
    }

    sWakeLock.Acquire();
    intent.SetClass(context, typeof(GCMIntentService));
    context.StartService(intent);
  }

  protected override void OnHandleIntent(Intent intent) {
    try {
      Context context = this.ApplicationContext;
      string action = intent.Action;

      if (action.Equals("com.google.android.c2dm.intent.REGISTRATION")) {
        HandleRegistration(intent);
      } else if (action.Equals("com.google.android.c2dm.intent.RECEIVE")) {
        HandleMessage(intent);
      }
    } finally {
      lock(LOCK) {
        //Sanity check for null as this is a public method
        if (sWakeLock != null) sWakeLock.Release();
      }
    }
  }

  private void HandleRegistration(Intent intent) {
    string registrationId = intent.GetStringExtra("registration_id");
    string error = intent.GetStringExtra("error");
    string unregistration = intent.GetStringExtra("unregistered");

    if (string.IsNullOrEmpty(error)) {
      var response = await SnsClient.CreatePlatformEndpointAsync(new CreatePlatformEndpointRequest {
        Token = registrationId,
        PlatformApplicationArn = "YourPlatformArn" /* insert your platform application ARN here */
      });
    }
  }

  private void HandleMessage(Intent intent) {
    string message = string.Empty;
    Bundle extras = intent.Extras;
    if (!string.IsNullOrEmpty(extras.GetString("message"))) {
      message = extras.GetString("message");
    } else {
      message = extras.GetString("default");
    }

    Log.Info("Messages", "message received = " + message);
    ShowNotification(this, "SNS Push", message);
    //show the message

  }

  public void ShowNotification(string contentTitle,
  string contentText) {
    // Intent
    Notification.Builder builder = new Notification.Builder(this)
      .SetContentTitle(contentTitle)
      .SetContentText(contentText)
      .SetDefaults(NotificationDefaults.Sound | NotificationDefaults.Vibrate)
      .SetSmallIcon(Resource.Drawable.Icon)
      .SetSound(RingtoneManager.GetDefaultUri(RingtoneType.Notification));

    // Get the notification manager:
    NotificationManager notificationManager = this.GetSystemService(Context.NotificationService) as NotificationManager;

    notificationManager.Notify(1001, builder.Build());
  }
}
```

## Send a Message from the SNS Console to Your Endpoint
<a name="send-a-message-from-the-sns-console-to-your-endpoint"></a>

1. Go to the [SNS Console > Applications](https://console.aws.amazon.com/sns/v2/home).

1. Select your platform application, select an endpoint, and click **Publish to endpoint**.

1. Type in a text message in the text box and click **Publish message** to publish a message.
