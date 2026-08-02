---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-mobile-tracking-ios.html
---

# iOS Mobile Tracking SDK
<a name="loc-mobile-tracking-ios"></a>

The Amazon Location mobile tracking SDK provides utilities which help easily authenticate, capture device positions, and send position updates to Amazon Location Trackers. The SDK supports local filtering of location updates with configurable update intervals. This reduces data costs and optimizes intermittent connectivity for your iOS applications.

The iOS tracking SDK is available on GitHub: [Amazon Location Mobile Tracking SDK for iOS](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios).

This section covers the following topics for the Amazon Location mobile tracking iOS SDK:

**Topics**
+ [Installation](#loc-mobile-tracking-install-ios)
+ [Usage](#loc-mobile-tracking-usage-ios)
+ [Filters](#loc-mobile-tracking-ios-filters)
+ [iOS Mobile SDK tracking functions](#loc-mobile-tracking-functions)
+ [Examples](#loc-mobile-tracking-example-ios)

## Installation
<a name="loc-mobile-tracking-install-ios"></a>

Use the following procedure to install the mobile tracking SDK for iOS:

1. In your Xcode project, go to **File** and select **Add Package Dependencies**.

1. Type the following URL: [https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios/](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios/) into the search bar and press the enter key.

1. Select the `amazon-location-mobile-tracking-sdk-ios` package and click on **Add Package**.

1. Select the `AmazonLocationiOSTrackingSDK` package product and click on **Add Package**.

## Usage
<a name="loc-mobile-tracking-usage-ios"></a>

The following procedure shows you how to create an authentication helper using credentials from Cognito.

1. After installing the library, you need to add one or both of the descriptions into your `info.plist` file:

   ```
   Privacy - Location When In Use Usage Description
   Privacy - Location Always and When In Use Usage Description
   ```

1. Next, import the AuthHelper in your class:

   ```
   import AmazonLocationiOSAuthSDKimport AmazonLocationiOSTrackingSDK
   ```

1. Then you will create an `AuthHelper` object and use it with the AWS SDK, by creating an authentication helper using credentials from Amazon Cognito.

   ```
   let authHelper = AuthHelper()
   let locationCredentialsProvider = authHelper.authenticateWithCognitoUserPool(identityPoolId: "{{My-Cognito-Identity-Pool-Id}}", region: "{{My-region}}") //example: us-east-1
   let locationTracker = LocationTracker(provider: locationCredentialsProvider, trackerName: "{{My-tracker-name}}")

   // Optionally you can set ClientConfig with your own values in either initialize or in a separate function
   // let trackerConfig = LocationTrackerConfig(locationFilters: [TimeLocationFilter(), DistanceLocationFilter()],

   trackingDistanceInterval: 30,
   trackingTimeInterval: 30,
   logLevel: .debug)

   // locationTracker = LocationTracker(provider: credentialsProvider, trackerName: "My-tracker-name",config: trackerConfig)
   // locationTracker.setConfig(config: trackerConfig)
   ```

## Filters
<a name="loc-mobile-tracking-ios-filters"></a>

The Amazon Location mobile tracking iOS SDK has three inbuilt location filters.
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

## iOS Mobile SDK tracking functions
<a name="loc-mobile-tracking-functions"></a>

The Amazon Location mobile tracking SDK for iOS includes the following functions:
+ **Class**: `LocationTracker`

  `init(provider: LocationCredentialsProvider, trackerName: String, config: LocationTrackerConfig? = nil)`

  This is an initializer function to create a `LocationTracker` object. It requires instances of `LocationCredentialsProvider` , `trackerName` and optionally an instance of `LocationTrackingConfig`. If the config is not provided it will be initialized with default values.
+ **Class**: `LocationTracker`

  `setTrackerConfig(config: LocationTrackerConfig)`

  This sets Tracker's config to take effect at any point after initialization of location tracker
+ **Class**: `LocationTracker`

  `getTrackerConfig()`

  This gets the location tracking config to use or modify in your app.

  Returns: `LocationTrackerConfig`
+ **Class**: `LocationTracker`

  `getDeviceId()`

  Gets the location tracker's generated device Id.

  Returns: `String?`
+ **Class**: `LocationTracker`

  `startTracking()`

  Starts the process of accessing the user's location and sending it to the AWS tracker.
+ **Class**: `LocationTracker`

  `resumeTracking()`

  Resumes the process of accessing the user's location and sending it to the AWS tracker.
+ **Class**: `LocationTracker`

  `stopTracking()`

  Stops the process of tracking the user's location.
+ **Class**: `LocationTracker`

  `startBackgroundTracking(mode: BackgroundTrackingMode)`

  Starts the process of accessing the user's location and sending it to the AWS tracker while the application is in the background. `BackgroundTrackingMode` has the following options:
  + `Active:` This option doesn't automatically pauses location updates.
  + `BatterySaving:` This option automatically pauses location updates
  + `None:` This option overall disables background location updates
+ **Class**: `LocationTracker`

  `resumeBackgroundTracking(mode: BackgroundTrackingMode)`

  Resumes the process of accessing the user's location and sending it to the AWS tracker while the application is in the background.
+ **Class**: `LocationTracker`

  `stopBackgroundTracking()`

  Stops the process of accessing the user's location and sending it to the AWS tracker while the application is in the background.
+ **Class**: `LocationTracker`

  `getTrackerDeviceLocation(nextToken: String?, startTime: Date? = nil, endTime: Date? = nil, completion: @escaping (Result<GetLocationResponse, Error>)`

  Retrieves the uploaded tracking locations for the user's device between start and end date and time.

  Returns: `Void`
+ **Class**: `LocationTrackerConfig`

  `init()`

  This initializes the LocationTrackerConfig with default values.
+ **Class**: `LocationTrackerConfig`

  `init(locationFilters: [LocationFilter]? = nil, trackingDistanceInterval: Double? = nil, trackingTimeInterval: Double? = nil, trackingAccuracyLevel: Double? = nil, uploadFrequency: Double? = nil, desiredAccuracy: CLLocationAccuracy? = nil, activityType: CLActivityType? = nil, logLevel: LogLevel? = nil)`

  This initializes the `LocationTrackerConfig` with user-defined parameter values. If a parameter value is not provided it will be set to a default value.
+ **Class**: `LocationFilter`

  `shouldUpload(currentLocation: LocationEntity, previousLocation: LocationEntity?, trackerConfig: LocationTrackerConfig)`

  The `LocationFilter` is a protocol that users can implement for their custom filter implementation. A user would need to implement `shouldUpload` function to compare previous and current location and return if the current location should be uploaded.

## Examples
<a name="loc-mobile-tracking-example-ios"></a>

This sections details examples of using the Amazon Location Mobile Tracking SDK for iOS.

**Note**
Ensure that the necessary permissions are set in the `info.plist` file. These are the same permissions listed in the [Usage](#loc-mobile-tracking-usage-ios) section.

The following example demonstrates functionality for tracking device location and retrieving tracked locations:

```
Privacy - Location When In Use Usage Description
Privacy - Location Always and When In Use Usage Description
```

Start tracking the location:

```
do {
    try locationTracker.startTracking()
    }
catch TrackingLocationError.permissionDenied {
        // Handle permissionDenied by showing the alert message or opening the app settings
        }
```

Resume tracking the location:

```
do {
    try locationTracker.resumeTracking()
    }
catch TrackingLocationError.permissionDenied {
    // Handle permissionDenied by showing the alert message or opening the app settings
    }
```

Stop tracking the location:

```
locationTracker.stopTracking()
```

Start background tracking:

```
do {
    locationTracker.startBackgroundTracking(mode: .Active) // .Active, .BatterySaving, .None
    }
catch TrackingLocationError.permissionDenied {
   // Handle permissionDenied by showing the alert message or opening the app settings
   }
```

Resume background tracking:

```
do {
    locationTracker.resumeBackgroundTracking(mode: .Active)
    }
catch TrackingLocationError.permissionDenied {
    // Handle permissionDenied by showing the alert message or opening the app settings
    }
```

To stop background tracking:

```
locationTracker.stopBackgroundTracking()
```

Retrieve device's tracked locations from the tracker:

```
func getTrackingPoints(nextToken: String? = nil) {
let startTime: Date = Date().addingTimeInterval(-86400) // Yesterday's day date and time
let endTime: Date = Date()
locationTracker.getTrackerDeviceLocation(nextToken: nextToken, startTime: startTime, endTime: endTime, completion: { [weak self] result in
    switch result {
    case .success(let response):

        let positions = response.devicePositions
        // You can draw positions on map or use it further as per your requirement

        // If nextToken is available, recursively call to get more data
        if let nextToken = response.nextToken {
            self?.getTrackingPoints(nextToken: nextToken)
        }
    case .failure(let error):
        print(error)
    }
})
}
```
