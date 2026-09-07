---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/delivery.html
---

# Delivery applications
<a name="delivery"></a>

The following is an illustration of a delivery application architecture using Amazon Location.

With this architecture, you can:
+ Initiate events based on proximity of delivery agents so that pickups are ready in time and customers can be notiﬁed when their delivery is arriving.
+ Display driver locations, as well as pick-up and drop-oﬀ locations in near-real time on a map to show dispatch teams the big picture.
+ Store the locations of delivery agents so that you can act on them in your backend application or analyze them over time.
+ Analyze location history to identify trends and opportunities for optimization.

![Architecture diagram showing delivery tracking workflow using AWS services like Lambda , EventBridge , and Location Services.](https://docs.aws.amazon.com/location/previous/developerguide/images/delivery.PNG)

The following is an overview of the steps required to build a delivery application:

1. Create your geofence collections and link tracked devices to the collection. For more information see, [Geofencing an area of interest using Amazon Location](geofence-an-area.md).

1. Create an AWS Lambda function to automatically add and remove geofences as your orders are booked.

1. Configure Amazon EventBridge to send notifications or initiate a processes. For more information, see [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md).

1. Display tracked assets and active geofences on a map. For more information, see [Using maps](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html).

1. Save location data to long-term storage for further analysis.

1. Once you have built your application, you can use Amazon CloudWatch and AWS CloudTrail to manage your application. For more information, see [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).
