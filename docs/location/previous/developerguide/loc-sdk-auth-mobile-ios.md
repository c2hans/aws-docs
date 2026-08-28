---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth-mobile-ios.html
---

# iOS Mobile Authentication SDK
<a name="loc-sdk-auth-mobile-ios"></a>

These utilities help you authenticate when making Amazon Location Service API calls from your iOS applications. This specifically helps when using [Amazon Cognito](https://docs.aws.amazon.com/location/previous/developerguide/authenticating-using-cognito.html) or [API keys](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) as the authentication method.

The iOS mobile authentication SDK is available on github: [Amazon Location Service Mobile Authentication SDK for iOS](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/tree/main).

## Installation
<a name="loc-sdk-auth-mobile-Android-install"></a>

Install the SDK in an Xcode project:

1. Go to **File**, then select **Add Package Dependencies** in your XCode project.

1. Type the package URL: [https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/) into the search bar and press the enter key.

1. Select the `amazon-location-mobile-auth-sdk-ios` package and press **Add Package**.

1. Select the `AmazonLocationiOSAuthSDK` package product and press **Add Package**.

## Authentication Functions
<a name="loc-sdk-auth-mobile-ios-functions"></a>

The authentication helper SDK has the following functions:
+ `authHelper.authenticateWithApiKey("My-Amazon-Location-API-Key"): LocationCredentialsProvider`: This function returns a `LocationCredentialsProvider` initialized to work with an API Key.
+ `authHelper.authenticateWithCognitoIdentityPool("My-Cognito-Identity-Pool-Id"): LocationCredentialsProvider`: This function returns a `LocationCredentialsProvider` initialized to work with an Amazon Cognito identity pool.

## Usage
<a name="loc-sdk-auth-mobile-ios-usage"></a>

To use the mobile authentication SDK, add the following statements to your activity:

```
import AmazonLocationiOSAuthSDK
import AWSLocationXCF
```

You have two options when creating the authentication helper and location client provider instances. You can create an instance using [Amazon Location API keys](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) or [Amazon Cognito](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html).
+ To create an authentication helper instance using an Amazon Location API Key, declare the helper class as follows:

  ```
  let authHelper = AuthHelper()
  let locationCredentialsProvider = authHelper.authenticateWithAPIKey(apiKey: "{{My-Amazon-Location-API-Key}}", region: "{{account-region}}")
  ```
+ To create an authentication helper instance using Amazon Cognito, declare the helper class as follows:

  ```
  let authHelper = AuthHelper()
  let locationCredentialsProvider = authHelper.authenticateWithCognitoUserPool(identityPoolId: "{{My-Amazon-Location-API-Key}}", region: "{{account-region}}")
  ```

You can create an Amazon Location client instance using the location credentials provider and make calls to the Amazon Location service. The following example searches for places near a specified latitude and longitude.

```
let locationClient = AWSLocation.default()
let searchPlaceIndexForPositionRequest = AWSLocationSearchPlaceIndexForPositionRequest()!
searchPlaceIndexForPositionRequest.indexName = "My-Place-Index-Name"
searchPlaceIndexForPositionRequest.position = [30.405423, -97.718833]
let nearbyPlaces = locationClient.searchPlaceIndex(forPosition: searchPlaceIndexForPositionRequest)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
