---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns-send-push-notifications-ios.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Send Push Notifications (Xamarin iOS)
<a name="sns-send-push-notifications-ios"></a>

This document explains how to send push notifications to a Xamarin iOS application using Amazon Simple Notification Service (SNS) and the AWS Mobile SDK for .NET and Xamarin.

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

### Obtain Membership in the Apple iOS Developer Program
<a name="obtain-membership-in-the-apple-ios-developer-program"></a>

You will need to run your app on a physical device to receive push notifications. To run your app on a device, you must have a membership in the [Apple iOS Developer Program Membership](https://developer.apple.com/programs/ios/). Once you have a membership, you can use Xcode to generate a signing identity. For more information, see Apple’s [App Distribution Quick Start](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/AppStoreDistributionTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40013839) documentation.

### Create an iOS Certificate
<a name="create-an-ios-certificate"></a>

First, you need to create an iOS Certificate. Then, you need to create a provisioning profile configured for push notifications. To do so:

1. Go to the [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action), click **Certificates, Identifiers & Profiles**.

1. Click **Identifiers** under **iOS Apps**, click the plus button in the upper right-hand corner of the web page to add a new iOS App ID, and enter an App ID description.

1. Scroll down to the **Add ID Suffix** section and select **Explicit App ID** and enter your bundle identifier.

1. Scroll down to the **App Services** section and select **Push Notifications**.

1. Click **Continue**.

1. Click **Submit**.

1. Click **Done**.

1. Select the App ID you just created and then click **Edit**.

1. Scroll down to the **Push Notifications** section. Click **Create Certificate** under **Development SSL Certificate**.

1. Follow the instructions to create a Certificate Signing Request (CSR), upload the request, and download an SSL certificate that will be used to communicate with Apple Notification Service (APNS).

1. Return to the **Certificates, Identifiers & Profiles** page. Click **All** under **Provisioning Profiles**.

1. Click the plus button in the upper right-hand corner to add a new provisioning profile.

1. Select **iOS App Development**, and then click **Continue**.

1. Select your App ID, and then click **Continue**.

1. Select your developer certificate, and then click **Continue**.

1. Select your device, and then click **Continue**.

1. Enter a profile name, and then click **Generate**.

1. Download and double-click the provision file to install the provisioning profile.

For more information on provisioning a profile configured for push notifications, see Apple’s [Configuring Push Notifications](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringPushNotifications/ConfiguringPushNotifications.html#//apple_ref/doc/uid/TP40012582-CH32-SW1) documentation.

### Use Certificate to Create Platform ARN in SNS Console
<a name="use-certificate-to-create-platform-arn-in-sns-console"></a>

1. Run the KeyChain access app, select **My Certificates** on the lower left-hand side of the screen, and then right-click the SSL certificate you generated to connect to APNS and select **Export**. You will be prompted to specify a name for the file and a password to protect the certificate. The certificate will be saved in a P12 file.

1. Go to the [SNS Console](https://console.aws.amazon.com/sns/v2/home) and click **Applications** on the left-hand side of the screen.

1. Click **Create platform application** to create a new SNS platform application.

1. Enter an **Application Name**.

1. Select **Apple Development** for **Push notification platform**.

1. Click **Choose File** and select the P12 file you created when you exported your SSL certificate.

1. Enter the password you specified when you exported the SSL certificate and click **Load Credentials From File**.

1. Click **Create platform application**.

1. Select the Platform Application you just created and copy the Application ARN. You will need this in the upcoming steps.

### Add NuGet Package for SNS to Your Project
<a name="add-nuget-package-for-sns-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the Amazon Simple Notification Service NuGet package to your project.

## Create an SNS Client
<a name="create-an-sns-client"></a>

```
var snsClient = new AmazonSimpleNotificationServiceClient(credentials, region);
```

## Register Your Application for Remote Notifications
<a name="register-your-application-for-remote-notifications"></a>

To register an application, call RegisterForRemoteNotifications on your UIApplication object, as shown below. Place the following code in AppDelegate.cs, inserting your platform application ARN where prompted below:

```
public override bool FinishedLaunching(UIApplication app, NSDictionary options) {
// do something
var pushSettings = UIUserNotificationSettings.GetSettingsForTypes (
  UIUserNotificationType.Alert |
  UIUserNotificationType.Badge |
  UIUserNotificationType.Sound,
  null
);
app.RegisterUserNotifications(pushSettings);
app.RegisterForRemoteNotifications();
// do something
  return true;
}

public override void RegisteredForRemoteNotifications(UIApplication application, NSData token) {
  var deviceToken = token.Description.Replace("<", "").Replace(">", "").Replace(" ", "");
  if (!string.IsNullOrEmpty(deviceToken)) {
    //register with SNS to create an endpoint ARN
    var response = await SnsClient.CreatePlatformEndpointAsync(
    new CreatePlatformEndpointRequest {
      Token = deviceToken,
      PlatformApplicationArn = "YourPlatformArn" /* insert your platform application ARN here */
    });
  }
}
```

## Send a Message from the SNS Console to Your Endpoint
<a name="send-a-message-from-the-sns-console-to-your-endpoint"></a>

1. Go to the [SNS Console > Applications](https://console.aws.amazon.com/sns/v2/home).

1. Select your platform application, select an endpoint, and click **Publish to endpoint**.

1. Type in a text message in the text box and click **Publish message** to publish a message.
