---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html
---

# Using Maps (V1) in your application
<a name="using-maps"></a>

**Important**
**This page documents the previous Maps API (V1). Use it only for existing applications.** The Maps V2 API is the latest version. Use it for all new applications; see the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.
The latest operations are `GetTile`, `GetStyleDescriptor`, `GetStaticMap`, `GetSprites`, and `GetGlyphs`. These operations are under the `geo-maps` namespace. They are exposed as `@aws-sdk/client-geo-maps` for JavaScript and `boto3.client('geo-maps')` for Python.
The map resources and tutorials described below are previous-generation. Use them only for existing applications.

Amazon Location maps are cost-effective and interactive. You can replace an existing map in your application to save money, or add a new one to display location-based data visually, such as your store location.

![Example map style in an app, showing parks mapped in central Seattle](https://docs.aws.amazon.com/location/previous/developerguide/images/maps_park_example.png)

Amazon Location Service lets you choose a data provider for map operations by creating and configuring a map resource. The map resource configures the data provider and the style that is used to render the map.

After you create your resource, you can send requests by using the AWS SDK directly, or by using a library made specifically for rendering maps in your environment.

**Note**
For an overview of map concepts, see [Maps (V1) concepts](map-concepts.md).

**Topics**
+ [Prerequisites for using Amazon Location maps](map-prerequisites.md)
+ [Display a map in your application with Amazon Location](display-map.md)
+ [Drawing data features on a map](drawing-on-a-map.md)
+ [Setting extents for a map using MapLibre](setting-map-extents.md)
+ [Managing your map resources (V1)](managing-maps.md)
