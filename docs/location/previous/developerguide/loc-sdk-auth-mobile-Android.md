---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth-mobile-Android.html
---

# Android Mobile Authentication SDK
<a name="loc-sdk-auth-mobile-Android"></a>

These utilities help you authenticate when making Amazon Location Service API calls from your Android applications. This specifically helps when using [Amazon Cognito](https://docs.aws.amazon.com//location/previous/developerguide/authenticating-using-cognito.html) or [API keys](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) as the authentication method.

The Android mobile authentication SDK is available on github: [Amazon Location Service Mobile Authentication SDK for Android](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-android/tree/main). Additionally, both the mobile authentication SDK and the AWS SDK are available on the [AWS Maven repository](https://central.sonatype.com/artifact/software.amazon.location/tracking).

## Installation
<a name="loc-sdk-auth-mobile-Android-install"></a>

To use the mobile authentication SDK, add the following import statements to your `build.gradle` file in Android Studio.

```
implementation("software.amazon.location:auth:0.0.1")
implementation("com.amazonaws:aws-android-sdk-location:2.72.0")
```

## Authentication Functions
<a name="loc-sdk-auth-mobile-Android-functions"></a>

The authentication helper SDK has the following functions:
+ `authHelper.authenticateWithApiKey("My-Amazon-Location-API-Key"): LocationCredentialsProvider`: This function returns a `LocationCredentialsProvider` initialized to work with an API Key.
+ `authHelper.authenticateWithCognitoIdentityPool("My-Cognito-Identity-Pool-Id"): LocationCredentialsProvider`: This function returns a `LocationCredentialsProvider` initialized to work with an Amazon Cognito identity pool.

## Usage
<a name="loc-sdk-auth-mobile-Android-usage"></a>

To use the SDK in your code, import the following classes:

```
import com.amazonaws.services.geo.AmazonLocationClient
import software.amazon.location.auth.AuthHelper
import software.amazon.location.auth.LocationCredentialsProvider
```

You have two options when creating the authentication helper and location client provider instances. You can create an instance using [Amazon Location API keys](https://docs.aws.amazon.com//location/previous/developerguide/using-apikeys.html) or [Amazon Cognito](https://docs.aws.amazon.com//location/previous/developerguide/using-apikeys.html).
+ To create an authentication helper instance using an Amazon Location API Key, declare the helper class as follows:

  ```
  var authHelper = AuthHelper(applicationContext)
  var locationCredentialsProvider : LocationCredentialsProvider = authHelper.authenticateWithApiKey("{{My-Amazon-Location-API-Key}}")
  ```
+ To create an authentication helper instance using Amazon Cognito, declare the helper class as follows:

  ```
  var authHelper = AuthHelper(applicationContext)
  var locationCredentialsProvider : LocationCredentialsProvider = authHelper.authenticateWithCognitoIdentityPool("{{My-Cognito-Identity-Pool-Id}}")
  ```

You can create an Amazon Location client instance using the location credentials provider and make calls to the Amazon Location service. The following example searches for places near a specified latitude and longitude.

```
var locationClient = authHelper.getLocationClient(locationCredentialsProvider.getCredentialsProvider())
var searchPlaceIndexForPositionRequest = SearchPlaceIndexForPositionRequest().withIndexName("{{My-Place-Index-Name}}").withPosition(arrayListOf(30.405423, -97.718833))
var nearbyPlaces = locationClient.searchPlaceIndexForPosition(searchPlaceIndexForPositionRequest)
```
