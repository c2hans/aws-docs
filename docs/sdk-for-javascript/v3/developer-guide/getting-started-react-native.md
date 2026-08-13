---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-react-native.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Getting started in React Native
<a name="getting-started-react-native"></a>

This tutorial shows you how you can create a React Native app using [React Native CLI](https://reactnative.dev/docs/environment-setup).

![JavaScript code example that applies to React Native.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/browsericon.png)

**This tutorial shows you:**
+ How to install and include the AWS SDK for JavaScript version 3 (V3) modules that your project uses.
+ How to write code that connects to Amazon Simple Storage Service (Amazon S3) to create and delete an Amazon S3 bucket.

## The Scenario
<a name="getting-started-react-scenario"></a>

Amazon S3 is a cloud service that enables you to store and retrieve any amount of data at any time, from anywhere on the web. React Native is a development framework that enables you to create mobile applications. This tutorial shows you how you can create a React Native app that connects to Amazon S3 to create and delete an Amazon S3 bucket.

The app uses the following AWS SDK for JavaScript APIs:
+ [`CognitoIdentityClient`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cognito-identity/) constructor
+ [`S3`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/) constructor

## Prerequisite tasks
<a name="getting-started-react-setup"></a>

**Note**
If you've already completed any of the following steps through other tutorials or existing configuration, skip those steps.

This section provides the minimal setup needed to complete this tutorial. You shouldn't consider this to be a full setup. For that, see [Set up the SDK for JavaScript](setting-up.md).
+ Install the following tools:
  + [npm](https://docs.npmjs.com/getting-started/)
  + [Node.js](https://nodejs.org/en/download/)
  + [Xcode](https://developer.apple.com/xcode/) if you're testing on iOS
  + [Android Studio](https://developer.android.com/studio/) if you're testing on Android
+ Set up your [React Native development environment](https://reactnative.dev/docs/environment-setup)
+ Set up the project environment to run these Node TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on[ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/nodegetstarted/README.md).
+ You must establish how your code authenticates with AWS when developing with AWS services. For more information, see [SDK authentication with AWS](getting-your-credentials.md).
**Note**
The IAM role for this example should be set to use **AmazonS3FullAccess** permissions.

## Step 1: Create an Amazon Cognito Identity Pool
<a name="getting-started-react-create-identity-pool"></a>

In this exercise, you create and use an Amazon Cognito Identity pool to provide unauthenticated access to your app for the Amazon S3 service. Creating an identity pool also creates two AWS Identity and Access Management (IAM) roles, one to support users authenticated by an identity provider and the other to support unauthenticated guest users.

In this exercise, we will only work with the unauthenticated user role to keep the task focused. You can integrate support for an identity provider and authenticated users later.

**To create an Amazon Cognito Identity pool**

1. Sign in to the AWS Management Console and open the Amazon Cognito console at [Amazon Web Services Console](https://console.aws.amazon.com/cognito/).

1. Choose **Identity Pools** on the console opening page.

1. On the next page, choose **Create new identity pool**.
**Note**
If there are no other identity pools, the Amazon Cognito console will skip this page and open the next page instead.

1. In **Configure identity pool trust**, choose **Guest access** for user authentication.

1. In **Configure permissions**, choose **Create a new IAM role** and enter a name (for example, *getStartedReactRole*) in the **IAM role name**.

1. In **Configure properties**, enter a name (for example, *getStartedReactPool*) in **Identity pool name**.

1. In **Review and create**, confirm the selections that you made for your new identity pool. Select **Edit** to return to the wizard and change any settings. When you're done, select **Create identity pool**.

1. Note the identity pool ID and the Region for this newly created identity pool. You need these values to replace {{region}} and {{identityPoolId}} in your browser script.

After you create your Amazon Cognito identity pool, you're ready to add permissions for Amazon S3 that are needed by your React Native app.

## Step 2: Add a Policy to the Created IAM Role
<a name="getting-started-react-iam-role"></a>

To enable browser script access to Amazon S3 to create and delete an Amazon S3 bucket, use the unauthenticated IAM role created for your Amazon Cognito identity pool. This requires you to add an IAM policy to the role. For more information about IAM roles, see [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

**To add an Amazon S3 policy to the IAM role associated with unauthenticated users**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. Choose the name of the role that you want to modify (for example, *getStartedRole*), and then choose the **Permissions** tab.

1. Choose **Add permissions** and then choose **Attach policies**.

1. In the **Add permissions** page for this role, find and then select the check box for **AmazonS3ReadOnlyAccess**.
**Note**
You can use this process to enable access to any AWS service.

1. Choose **Add permissions**.

After you create your Amazon Cognito identity pool and add permissions for Amazon S3 to your IAM role for unauthenticated users, you are ready to build the app.

## Step 3: Create app using create-react-native-app
<a name="react-prerequisites"></a>

Create a React Native App by running the following command.

```
npx react-native init ReactNativeApp --npm
```

## Step 4: Install the Amazon S3 package and other dependencies
<a name="getting-started-react-install-dependencies"></a>

Inside the directory of the project, run the following commands to install the Amazon S3 package.

```
npm install @aws-sdk/client-s3
```

This command installs the Amazon S3 package in your project, and updates `package.json` to list Amazon S3 as a project dependency. You can find information about this package by searching for "@aws-sdk" on the [https://www.npmjs.com/](https://www.npmjs.com/)npm website.

These packages and their associated code are installed in the `node_modules` subdirectory of your project.

For more information about installing Node.js packages, see [Downloading and installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally) and [Creating Node.js modules](https://docs.npmjs.com/creating-node-js-modules) on the [npm (Node.js package manager) website](https://www.npmjs.com/). For information about downloading and installing the AWS SDK for JavaScript, see [Install the SDK for JavaScript](setting-up.md#installing-jssdk).

Install other dependencies required for authentication.

```
npm install @aws-sdk/client-cognito-identity @aws-sdk/credential-provider-cognito-identity
```

## Step 5: Write the React Native code
<a name="getting-started-react-write-native-code"></a>

Add the following code to the `App.tsx`. Replace {{identityPoolId}} and {{region}} with the identity pool ID and Region where your Amazon S3 bucket will be created.

```
import React, { useCallback, useState } from "react";
import { Button, StyleSheet, Text, TextInput, View } from "react-native";
import "react-native-get-random-values";
import "react-native-url-polyfill/auto";

import {
  S3Client,
  CreateBucketCommand,
  DeleteBucketCommand,
} from "@aws-sdk/client-s3";
import { fromCognitoIdentityPool } from "@aws-sdk/credential-providers";

const client = new S3Client({
  // The AWS Region where the Amazon Simple Storage Service (Amazon S3) bucket will be created. Replace this with your Region.
  region: "us-east-1",
  credentials: fromCognitoIdentityPool({
    // Replace the value of 'identityPoolId' with the ID of an Amazon Cognito identity pool in your Amazon Cognito Region.
    identityPoolId: "us-east-1:edbe2c04-7f5d-469b-85e5-98096bd75492",
    // Replace the value of 'region' with your Amazon Cognito Region.
    clientConfig: { region: "us-east-1" },
  }),
});

enum MessageType {
  SUCCESS = 0,
  FAILURE = 1,
  EMPTY = 2,
}

const App = () => {
  const [bucketName, setBucketName] = useState("");
  const [msg, setMsg] = useState<{ message: string; type: MessageType }>({
    message: "",
    type: MessageType.EMPTY,
  });

  const createBucket = useCallback(async () => {
    setMsg({ message: "", type: MessageType.EMPTY });

    try {
      await client.send(new CreateBucketCommand({ Bucket: bucketName }));
      setMsg({
        message: `Bucket "${bucketName}" created.`,
        type: MessageType.SUCCESS,
      });
    } catch (e) {
      console.error(e);
      setMsg({
        message: e instanceof Error ? e.message : "Unknown error",
        type: MessageType.FAILURE,
      });
    }
  }, [bucketName]);

  const deleteBucket = useCallback(async () => {
    setMsg({ message: "", type: MessageType.EMPTY });

    try {
      await client.send(new DeleteBucketCommand({ Bucket: bucketName }));
      setMsg({
        message: `Bucket "${bucketName}" deleted.`,
        type: MessageType.SUCCESS,
      });
    } catch (e) {
      setMsg({
        message: e instanceof Error ? e.message : "Unknown error",
        type: MessageType.FAILURE,
      });
    }
  }, [bucketName]);

  return (
    <View style={styles.container}>
      {msg.type !== MessageType.EMPTY && (
        <Text
          style={
            msg.type === MessageType.SUCCESS
              ? styles.successText
              : styles.failureText
          }
        >
          {msg.message}
        </Text>
      )}
      <View>
        <TextInput
          onChangeText={(text) => setBucketName(text)}
          autoCapitalize={"none"}
          value={bucketName}
          placeholder={"Enter Bucket Name"}
        />
        <Button color="#68a0cf" title="Create Bucket" onPress={createBucket} />
        <Button color="#68a0cf" title="Delete Bucket" onPress={deleteBucket} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  successText: {
    color: "green",
  },
  failureText: {
    color: "red",
  },
});

export default App;
```

The code first imports required React, React Native, and AWS SDK dependencies.

Inside the function App:
+ The S3Client object is created, specifying the credentials using Amazon Cognito Identity Pool created earlier.
+ The methods `createBucket` and `deleteBucket` create and delete the specified bucket, respectively.
+ The React Native View displays a text input field for the user to specify an Amazon S3 bucket name, and buttons to create and delete the specified Amazon S3 bucket.

The full JavaScript page is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/reactnative/ReactNativeApp/App.tsx).

## Step 6: Run the Example
<a name="getting-started-react-native-run-sample"></a>

**Note**
Remember to sign in\! If you are using IAM Identity Center to authenticate, remember to sign in using the AWS CLI `aws sso login` command.

To run the example, run `web`, `ios`, or `android` command using npm.

Here is an example output of running `ios` command on macOS.

```
$ npm run ios

> ReactNativeApp@0.0.1 ios /Users/trivikr/workspace/ReactNativeApp
> react-native run-ios

info Found Xcode workspace "ReactNativeApp.xcworkspace"
info Launching iPhone 11 (iOS 14.2)
info Building (using "xcodebuild -workspace ReactNativeApp.xcworkspace -configuration Debug -scheme ReactNativeApp -destination id=706C1A97-FA38-407D-AD77-CB4FCA9134E9")
success Successfully built the app
info Installing "/Users/trivikr/Library/Developer/Xcode/DerivedData/ReactNativeApp-cfhmsyhptwflqqejyspdqgjestra/Build/Products/Debug-iphonesimulator/ReactNativeApp.app"
info Launching "org.reactjs.native.example.ReactNativeApp"

success Successfully launched the app on the simulator
```

Here is an example output of running `android` command on macOS.

```
$ npm run android

> ReactNativeApp@0.0.1 android
> react-native run-android

info Running jetifier to migrate libraries to AndroidX. You can disable it using "--no-jetifier" flag.
Jetifier found 970 file(s) to forward-jetify. Using 12 workers...
info Starting JS server...
info Launching emulator...
info Successfully launched emulator.
info Installing the app...

> Task :app:stripDebugDebugSymbols UP-TO-DATE
Compatible side by side NDK version was not found.

> Task :app:installDebug
02:18:38 V/ddms: execute: running am get-config
02:18:38 V/ddms: execute 'am get-config' on 'emulator-5554' : EOF hit. Read: -1
02:18:38 V/ddms: execute: returning
Installing APK 'app-debug.apk' on 'Pixel_3a_API_30_x86(AVD) - 11' for app:debug
02:18:38 D/app-debug.apk: Uploading app-debug.apk onto device 'emulator-5554'
02:18:38 D/Device: Uploading file onto device 'emulator-5554'
02:18:38 D/ddms: Reading file permission of /Users/trivikr/workspace/ReactNativeApp/android/app/build/outputs/apk/debug/app-debug.apk as: rw-r--r--
02:18:40 V/ddms: execute: running pm install -r -t "/data/local/tmp/app-debug.apk"
02:18:41 V/ddms: execute 'pm install -r -t "/data/local/tmp/app-debug.apk"' on 'emulator-5554' : EOF hit. Read: -1
02:18:41 V/ddms: execute: returning
02:18:41 V/ddms: execute: running rm "/data/local/tmp/app-debug.apk"
02:18:41 V/ddms: execute 'rm "/data/local/tmp/app-debug.apk"' on 'emulator-5554' : EOF hit. Read: -1
02:18:41 V/ddms: execute: returning
Installed on 1 device.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/6.2/userguide/command_line_interface.html#sec:command_line_warnings

BUILD SUCCESSFUL in 6s
27 actionable tasks: 2 executed, 25 up-to-date
info Connecting to the development server...
8081
info Starting the app on "emulator-5554"...
Starting: Intent { cmp=com.reactnativeapp/.MainActivity }
```

Enter the bucket name you want to create or delete and click on either **Create Bucket** or **Delete Bucket**. The respective command will be sent to Amazon S3, and success or error message will be displayed.

![Success message showing bucket test-bucket-name-123 created with Create Bucket and Delete Bucket options.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/react-app-running.png)

## Possible Enhancements
<a name="getting-started-react-native-variations"></a>

Here are variations on this application you can use to further explore using the AWS SDK for JavaScript in a React Native app.
+ Add a button to list Amazon S3 buckets, and provide a delete button next to each bucket listed.
+ Add a button to put text object into a bucket.
+ Integrate an external identity provider like Facebook or Amazon to use with the authenticated IAM role.
