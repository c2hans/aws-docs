---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-mobile-tracking-android.html
---

# Android Mobile Tracking SDK
<a name="loc-mobile-tracking-android"></a>

The Amazon Location mobile tracking SDK provides utilities which help easily authenticate, capture device positions, and send position updates to Amazon Location Trackers. The SDK supports local filtering of location updates with configurable update intervals. This reduces data costs and optimizes intermittent connectivity for your Android applications.

The Android tracking SDK is available on GitHub: [Amazon Location Mobile Tracking SDK for Android](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-android). Additionally, both the mobile authentication SDK and the AWS SDK are available on the [AWS Maven repository](https://central.sonatype.com/artifact/software.amazon.location/tracking). The Android tracking SDK is designed to work with the general AWS SDK.

This section covers the following topics for the Amazon Location mobile tracking Android SDK:

**Topics**
+ [Installation](#loc-mobile-tracking-install-android)
+ [Usage](#loc-mobile-tracking-usage-android)
+ [Filters](#loc-mobile-tracking-android-filters)
+ [Android Mobile SDK tracking functions](#loc-mobile-tracking-functions)
+ [Examples](#loc-mobile-tracking-example-android)

## Installation
<a name="loc-mobile-tracking-install-android"></a>

To install the SDK, add the following lines to the dependencies section of your build.gradle file in Android Studio:

```
implementation("software.amazon.location:tracking:0.0.1")
implementation("software.amazon.location:auth:0.0.1")
implementation("com.amazonaws:aws-android-sdk-location:2.72.0")
```

## Usage
<a name="loc-mobile-tracking-usage-android"></a>

This procedure shows you how to use the SDK to authenticate and create the `LocationTracker` object:

**Note**
This procedure assumes you have imported the library mentioned in the [Installation](#loc-mobile-tracking-install-android) section.

1. Import the following classes in your code:

   ```
   import software.amazon.location.tracking.LocationTracker
   import software.amazon.location.tracking.config.LocationTrackerConfig
   import software.amazon.location.tracking.util.TrackingSdkLogLevel
   import com.amazonaws.services.geo.AmazonLocationClient
   import software.amazon.location.auth.AuthHelper
   import software.amazon.location.auth.LocationCredentialsProvider
   ```

1. Next create an `AuthHelper`, since the `LocationCredentialsProvider` parameter is required for creating a `LocationTracker` object:

   ```
   // Create an authentication helper using credentials from Cognito
   val authHelper = AuthHelper(applicationContext)
   val locationCredentialsProvider : LocationCredentialsProvider = authHelper.authenticateWithCognitoIdentityPool("My-Cognito-Identity-Pool-Id")
   ```

1. Now, use the `LocationCredentialsProvider` and `LocationTrackerConfig` to create a `LocationTracker` object:

   ```
   val config = LocationTrackerConfig(
       trackerName = "MY-TRACKER-NAME",
       logLevel = TrackingSdkLogLevel.DEBUG,
       accuracy = Priority.PRIORITY_HIGH_ACCURACY,
       latency = 1000,
       frequency = 5000,
       waitForAccurateLocation = false,
       minUpdateIntervalMillis = 5000,
   )
   locationTracker = LocationTracker(
       applicationContext,
       locationCredentialsProvider,
       config,
   )
   ```

## Filters
<a name="loc-mobile-tracking-android-filters"></a>

The Amazon Location mobile tracking Android SDK has three inbuilt location filters.
+ `TimeLocationFilter`: Filters the current location to be uploaded based on a defined time interval.
+ `DistanceLocationFilter`: Filters location updates based on a specified distance threshold.
+ `AccuracyLocationFilter`: Filters location updates by comparing the distance moved since the last update with the current location's accuracy.

This example adds filters in the `LocationTracker` at the creation time:

```
val config = LocationTrackerConfig(
    trackerName = "MY-TRACKER-NAME",
    logLevel = TrackingSdkLogLevel.DEBUG,
    accuracy = Priority.PRIORITY_HIGH_ACCURACY,
    latency = 1000,
    frequency = 5000,
    waitForAccurateLocation = false,
    minUpdateIntervalMillis = 5000,
    locationFilters = mutableListOf(TimeLocationFilter(), DistanceLocationFilter(), AccuracyLocationFilter())
)
locationTracker = LocationTracker(
    applicationContext,
    locationCredentialsProvider,
    config,
)
```

This example enables and disables filter at runtime with `LocationTracker`:

```
// To enable the filter
locationTracker?.enableFilter(TimeLocationFilter())

// To disable the filter
locationTracker?.disableFilter(TimeLocationFilter())
```

## Android Mobile SDK tracking functions
<a name="loc-mobile-tracking-functions"></a>

The Amazon Location mobile tracking SDK for Android includes the following functions:
+ **Class**: `LocationTracker`

  `constructor(context: Context,locationCredentialsProvider: LocationCredentialsProvider,trackerName: String)`, or `constructor(context: Context,locationCredentialsProvider: LocationCredentialsProvider,clientConfig: LocationTrackerConfig)`

  This is an initializer function to create a `LocationTracker` object. It requires instances of `LocationCredentialsProvider` , `trackerName` and optionally an instance of `LocationTrackingConfig`. If the config is not provided it will be initialized with default values.
+ **Class**: `LocationTracker`

  `start(locationTrackingCallback: LocationTrackingCallback)`

  Starts the process of accessing the user's location and sending it to an Amazon Location tracker.
+ **Class**: `LocationTracker`

  `isTrackingInForeground()`

  Checks if location tracking is currently in progress.
+ **Class**: `LocationTracker`

  `stop()`

  Stops the process of tracking the user's location.
+ **Class**: `LocationTracker`

  `startTracking()`

  Starts the process of accessing the user's location and sending it to the AWS tracker.
+ **Class**: `LocationTracker`

  `startBackground(mode: BackgroundTrackingMode, serviceCallback: ServiceCallback)`

  Starts the process of accessing the user's location and sending it to the AWS tracker while the application is in the background. BackgroundTrackingMode has the following options:
  + `ACTIVE_TRACKING`: This option actively tracks a user's location updates.
  + `BATTERY_SAVER_TRACKING`: This option tracks user's location updates every 15 minutes.
+ **Class**: `LocationTracker`

  `stopBackgroundService()`

  Stops the process of accessing the user's location and sending it to the AWS tracker while the application is in the background.
+ **Class**: `LocationTracker`

  `getTrackerDeviceLocation()`

  Retrieves the device location from Amazon Location services.
+ **Class**: `LocationTracker`

  `getDeviceLocation(locationTrackingCallback: LocationTrackingCallback?)`

  Retrieves the current device location from the fused location provider client and uploads it to Amazon Location tracker.
+ **Class**: `LocationTracker`

  `uploadLocationUpdates(locationTrackingCallback: LocationTrackingCallback?)`

  Uploads the device location to Amazon Location services after filtering based on the configured location filters.
+ **Class**: `LocationTracker`

  `enableFilter(filter: LocationFilter)`

  Enables a particular location filter.
+ **Class**: `LocationTracker`

  `checkFilterIsExistsAndUpdateValue(filter: LocationFilter)`

  Disable particular location filter.
+ **Class**: `LocationTrackerConfig`

  `LocationTrackerConfig( // Required var trackerName: String, // Optional var locationFilters: MutableList = mutableListOf( TimeLocationFilter(), DistanceLocationFilter(), ), var logLevel: TrackingSdkLogLevel = TrackingSdkLogLevel.DEBUG, var accuracy: Int = Priority.PRIORITY_HIGH_ACCURACY, var latency: Long = 1000, var frequency: Long = 1500, var waitForAccurateLocation: Boolean = false, var minUpdateIntervalMillis: Long = 1000, var persistentNotificationConfig: NotificationConfig = NotificationConfig()) `

  This initializes the `LocationTrackerConfig` with user-defined parameter values. If a parameter value is not provided, it will be set to a default value.
+ **Class**: `LocationFilter`

  `shouldUpload(currentLocation: LocationEntry, previousLocation: LocationEntry?): Boolean`

  The `LocationFilter` is a protocol that users can implement for their custom filter implementation. You need to implement the `shouldUpload` function to compare previous and current location and return if the current location should be uploaded.

## Examples
<a name="loc-mobile-tracking-example-android"></a>

The following code sample shows the mobile tracking SDK functionality.

This example uses the `LocationTracker` to start and stop tracking in background:

```
// For starting the location tracking
locationTracker?.startBackground(
BackgroundTrackingMode.ACTIVE_TRACKING,
object : ServiceCallback {
    override fun serviceStopped() {
        if (selectedTrackingMode == BackgroundTrackingMode.ACTIVE_TRACKING) {
            isLocationTrackingBackgroundActive = false
        } else {
            isLocationTrackingBatteryOptimizeActive = false
        }
    }
},
)

// For stopping the location tracking
locationTracker?.stopBackgroundService()
```
