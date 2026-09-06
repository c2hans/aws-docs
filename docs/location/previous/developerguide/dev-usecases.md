---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/dev-usecases.html
---

# Scenarios and use cases
<a name="dev-usecases"></a>

Amazon Location Service is a service that runs in the AWS Cloud. You may call it from your own Amazon EC2 instances in the cloud, but many mapping applications will run on devices, or a combination of devices and the cloud. The following lists just a few typical scenarios and how you might approach developing them.
+ A backend application that helps you to optimize routes for drivers in your fleet.

  You can write an application that runs on [Amazon EC2](https://docs.aws.amazon.com/ec2/) in the AWS Cloud that uses the Amazon Location Service to [calculate route matrices](calculate-route-matrix.md) as an input to a route optimizer for your fleet. Use the [AWS SDK](location-actions.md#sdk-general-information-section) to make calls to Amazon Location.
+ A web application that allows your customers to find the locations of your business.

  You can create a website that runs on Amazon EC2 instances, including a location-based application. Use the [AWS SDK for JavaScript](location-actions.md#sdk-general-information-section) to develop a web application to look up locations using [places search](searching-for-places.md), and display results on a [map](using-maps.md) using MapLibre. Use the Amazon Location SDK to make programming with location easier.
+ Add location features to an existing iOS or Android application.

  You can use the AWS SDK for Swift (iOS) or [Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin) (Android) to make calls to Amazon Location to add [places search](searching-for-places.md) and [maps](using-maps.md) functionality to your application. Use MapLibre to render maps. There are additional [AWS SDKs](location-actions.md#sdk-general-information-section) available for other languages.
+ Track assets (devices or vehicles), and get updates when they are enter or exit areas that you define.

  An application to track devices consists of several parts.
  + Each device that you are tracking must have a [tracker](start-tracking.md) resource created to track it. It must send position updates to Amazon Location Service, for example, by using [MQTT](tracking-using-mqtt.md).
  + Create [geofences](add-geofences.md) to define areas that you want to get enter and exit events for your assets.
  + You can use [Amazon EC2](https://docs.aws.amazon.com/ec2/) or [AWS Lambda](https://docs.aws.amazon.com/lambda/) to respond to your events as assets enter or exit the geofence areas.
  + You can expand upon this to create web or device applications to track and display your asset locations on maps.

The following section gives details on tools and libraries available to use with each aspect of the Amazon Location Service.
