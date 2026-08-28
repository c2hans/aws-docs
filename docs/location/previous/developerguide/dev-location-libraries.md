---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html
---

# How to use Amazon Location SDK and libraries
<a name="dev-location-libraries"></a>

The Amazon Location SDK is a set of open source libraries that provide useful functionality for developing Amazon Location applications. The following functionality is included:
+ **Amazon Location client** – The Amazon Location objects in the AWS SDK v3 are bundled and packaged for ease of use in web development.
+ **Authentication** – The authentication utility simplifies the authentication (using Amazon Cognito or API keys) when building a web page, [JavaScript](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-sdk-auth), [iOS](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-sdk-auth-mobile-ios), or [Android](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-sdk-auth-mobile-Android) application for Amazon Location Service.
+ **Tracking** – The mobile tracking SDKs are available for [iOS](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-mobile-tracking-ios) and [Android](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-mobile-tracking-android). This SDK makes it easier for mobile applications to interact with Amazon Location Trackers.
+ **Amazon Location GeoJSON functions** – The [GeoJSON conversion utilities](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html#loc-sdk-geojson) make it easy to convert between the industry-standard [GeoJSON](https://geojson.org/) formatted data, and the Amazon Location API formats.

The Amazon Location SDK is a set of functions that can make using the Amazon Location Service in an application simpler. You can install and import these functions into your JavaScript application. The following sections describe the Amazon Location client, and the authentication and GeoJSON helper libraries.

**Topics**
+ [Amazon Location client](loc-sdk-client.md)
+ [JavaScript Authentication helper](loc-sdk-auth.md)
+ [GeoJSON conversion helpers](loc-sdk-geojson.md)
+ [Android Mobile Authentication SDK](loc-sdk-auth-mobile-Android.md)
+ [iOS Mobile Authentication SDK](loc-sdk-auth-mobile-ios.md)
+ [Android Mobile Tracking SDK](loc-mobile-tracking-android.md)
+ [iOS Mobile Tracking SDK](loc-mobile-tracking-ios.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
