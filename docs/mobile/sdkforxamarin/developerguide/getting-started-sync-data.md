---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/getting-started-sync-data.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Sync User Data with Cognito Sync
<a name="getting-started-sync-data"></a>

Amazon Cognito Sync makes it easy to save mobile user data, such as app preferences or game state in the AWS Cloud without writing any backend code or managing any infrastructure. You can save data locally on users’ devices allowing your applications to work even when the devices are offline. You can also synchronize data across a user’s devices so that their app experience will be consistent regardless of the device they use.

The tutorial below explains how to integrate Sync with your app.

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

You must complete all of the instructions on the [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) before beginning this tutorial.

### Grant Access to Your Cognito Sync Resources
<a name="grant-access-to-your-cognito-sync-resources"></a>

The default policy associated with the unauthenticated and authenticate roles that you created during setup grant your application access to Cognito Sync. No further configuration is required.

### Add NuGet Package for Cognito Sync to Your Project
<a name="add-nuget-package-for-cognito-sync-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the Cognito SyncManager NuGet package to your project.

## Initialize the CognitoSyncManager
<a name="initialize-the-cognitosyncmanager"></a>

Pass your initialized Amazon Cognito credentials provider to the `CognitoSyncManager` constructor:

```
CognitoSyncManager syncManager = new CognitoSyncManager (
    credentials,
    new AmazonCognitoSyncConfig {
        RegionEndpoint = RegionEndpoint.USEast1 // Region
    }
);
```

## Syncing User Data
<a name="syncing-user-data"></a>

To sync unauthenticated user data:

1. Create a dataset.

1. Add user data to the dataset.

1. Synchronize the dataset with the cloud.

### Create a Dataset
<a name="create-a-dataset"></a>

Create an instance of `Dataset`. The openOrCreateDataset method is used to create a new dataset or open an existing instance of a dataset stored locally on the device:

```
Dataset dataset = syncManager.OpenOrCreateDataset("myDataset");
```

### Add User Data to the Dataset
<a name="add-user-data-to-the-dataset"></a>

User data is added in the form of key/value pairs:

```
dataset.OnSyncSuccess += SyncSuccessCallback;
dataset.Put("myKey", "myValue");
```

Cognito datasets function as dictionaries, with values accessible by key:

```
string myValue = dataset.Get("myKey");
```

### Synchronize Dataset
<a name="synchronize-dataset"></a>

To synchronize a dataset, call its synchronize method:

```
dataset.SynchronizeAsync();

void SyncSuccessCallback(object sender, SyncSuccessEventArgs e) {
  // Your handler code here
}
```

All data written to datasets will be stored locally until the dataset is synced. The code in this section assumes you are using an unauthenticated Cognito identity, so when the user data is synced with the cloud it will be stored per device. The device has a device ID associated with it. When the user data is synced to the cloud, it will be associated with that device ID.

For more information on Cognito Sync, see [Amazon Cognito Sync](cognito-sync.md).
