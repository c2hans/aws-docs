---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/using-amazon-location.html
---

# How to use Amazon Location Service
<a name="using-amazon-location"></a>

**Note**
We released a new version of the Places, Maps, and Routes APIs, see the updated [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) for revised information and new topics, such as [Geofences](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html) and [Trackers](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html).

You can use Amazon Location Service capabilities to complete geographic and location-related tasks. You can then combine these tasks to address more complex uses cases such as geomarketing, delivery, and asset tracking.

When you're ready to build location features into your application, use the following methods to use the Amazon Location Service functionality, depending on your goals and inclinations:
+ **Exploration tools** – If you want to experiment with Amazon Location resources, the following tools are the fastest way to access and try out the APIs:
  + The [Amazon Location console](https://console.aws.amazon.com/location/home) provides a variety of quick-access tools. You can create and manage your resources and try the APIs using [the Explore page](https://console.aws.amazon.com/location/explore/home). The console is also useful for creating resources (typically a one-time task) in preparation for using any of the other methods described later.
  + The [AWS Command Line Interface](https://aws.amazon.com/cli/) (CLI) lets you create resources and access the Amazon Location APIs using a terminal. The AWS CLI handles authentication when you configure it with your credentials.
  + You can see [code examples and tutorials](samples.md) that show how to perform tasks using the Amazon Location Service APIs. This includes [an example](example-explore.md) that mimics much of the functionality of the Explore page in the console.
+ **Platform SDKs** – If you aren't visualizing data on a map, you can use any of the [AWS standard tools](https://aws.amazon.com/tools/) to build on AWS.
  + The following SDKs are available: C\+\+, Go, Java, JavaScript, .NET, Node.js, PHP, Python, and Ruby.
+ **Frontend SDKs and libraries** – If you want to use Amazon Location to build an application on a mobile platform or visualize data on a map on any platform, you have the following options:
  + The AWS Amplify libraries integrate Amazon Location within [ iOS](https://docs.amplify.aws/guides/location-service/setting-up-your-app/q/platform/ios), [ Android](https://docs.amplify.aws/guides/location-service/setting-up-your-app/q/platform/android), and [ JavaScript](https://docs.amplify.aws/guides/location-service/setting-up-your-app/q/platform/js) web applications.
  + The MapLibre libraries let you render client-side maps into [iOS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-ios.html), [Android](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-android.html), and [JavaScript](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-gl-js.html) web applications using Amazon Location.
  + Tangram ES libraries enable you to render 2D and 3D maps from vector data using OpenGL ES within [iOS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-ios.html) and [Android](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-android.html) web applications. There is also Tangram for[ JavaScript](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-js.html) web applications.
+ **Sending direct HTTPS requests** – If you are working with a programming language for which there is no SDK available, or if you want more control over how you send a request to AWS, you can access Amazon Location by sending direct HTTPS requests authenticated by the Signature Version 4 signing process. For more information on the[ Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html), see the* AWS General Reference*.

This chapter describes many of the tasks that are common to applications using location data. The [common use cases](https://docs.aws.amazon.com/location/previous/developerguide/common-usecases.html) section describes how to combine these with other AWS services to achieve more complex use cases.

**Topics**
+ [Prerequisites for using Amazon Location Service](gs-prereqs.md)
+ [Using Maps (V1) in your application](using-maps.md)
+ [Searching place and geolocation data with Places (V1)](searching-for-places.md)
+ [Calculating routes with Routes (V1)](calculating-routes.md)
+ [Geofencing an area of interest using Amazon Location](geofence-an-area.md)
+ [Tag your Amazon Location Service resources](tagging.md)
+ [Grant access to Amazon Location Service](how-to-access.md)
+ [Monitor Amazon Location Service](monitoring.md)
+ [Create Amazon Location Service resources with AWS CloudFormation](creating-resources-with-cloudformation.md)
