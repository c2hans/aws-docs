---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-create-app.html
---

# Create the base iOS application to use Amazon Location
<a name="qs-ios-create-app"></a>

In this tutorial, you will create an iOS application that embeds a map, and allows the user to find what's at a location on the map.

First, let's create a Swift application using Xcode's project wizard.

**To create an empty application (Xcode)**

1. Open Xcode, and from the menu, choose **File**, **New**, **New Project**.

1. From the **iOS** tab, select **App**, and then choose **Next**.

1. Provide a **Product Name**, an **Organization Identifier**, and in the **Interface** field input `SwiftUI`. Choose **Next** to finalize the selection.

1. Select a location where you will save your project and press **create** button to create the empty application.

Once you have creating the base application, you will need to install the required packages for the sample app.

**Installing required dependencies**

1. In Xcode, right-click on the **project** and choose **Add Packages...**. This will open the Packages window, where you can add packages to your project.

1. In the Packages window, add the following packages:
   + For the Maplibre native package, use this URL: [https://github.com/maplibre/maplibre-gl-native-distribution](https://github.com/maplibre/maplibre-gl-native-distribution). From the URL, add these packages: `maplibre-gl-native-distribution`, and `Mapbox`.
   + For the Amazon Location authentication iOS SDK, use this URL: [https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios). From the URL, add these packages: `amazon-location-mobile-auth-sdk-ios`, and `AmazonLocationiOSAuthSDK`.
   + For the Amazon Location tracking iOS SDK, use this URL: [https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios). From the URL, add these packages: `amazon-location-mobile-tracking-sdk-ios`, and `AmazonLocationiOSTrackingSDK`.
