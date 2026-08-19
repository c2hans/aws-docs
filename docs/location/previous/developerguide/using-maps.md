---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html
---

# Using Amazon Location Maps in your application
<a name="using-maps"></a>

**Note**
We released a new version of the Maps API, see the updated [Maps Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) or [Maps API](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) for revised information.

Amazon Location maps are cost-effective and interactive. You can replace an existing map in your application to save money, or add a new one to display location-based data visually, such as your store location.

![Example map style in an app, showing parks mapped in central Seattle](http://docs.aws.amazon.com/location/previous/developerguide/images/maps_park_example.png)

Amazon Location Service lets you choose a data provider for map operations by creating and configuring a map resource. The map resource configures the data provider and the style that is used to render the map.

After you create your resource, you can send requests by using the AWS SDK directly, or by using a library made specifically for rendering maps in your environment.

**Note**
For an overview of map concepts, see [Learn about Maps resources in Amazon Location Service](map-concepts.md).

**Topics**
+ [Prerequisites for using Amazon Location maps](map-prerequisites.md)
+ [Display a map in your application with Amazon Location](display-map.md)
+ [Drawing data features on a map](drawing-on-a-map.md)
+ [Setting extents for a map using MapLibre](setting-map-extents.md)
+ [Managing your map resources with Amazon Location](managing-maps.md)
