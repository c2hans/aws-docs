---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/asset-tracking.html
---

# Asset tracking applications
<a name="asset-tracking"></a>

The following is an illustration of an asset tracking application architecture using Amazon Location:

With this architecture, you can:
+ Display asset locations on a map to illustrate the big picture. For example, showing a heat map using historical locations or events to help an operations or planning team.
+ Initiate events based on asset proximity to provide notice to a receiving department to prepare for a shipment arrival and reduce processing time.
+ Store asset locations to initiate actions in your backend applications or to analyze data over time.
+ Analyze location history to identify trends and opportunities for optimization.

![Architecture diagram showing asset tracking flow from mobile clients through AWS services to receiving user.](http://docs.aws.amazon.com/location/previous/developerguide/images/asset-tracking.PNG)

The following provides an overview of the steps required to build an asset tracking application:

1. Create your geofences in Geofence Collections and link Trackers to them. For more information, see [Geofencing an area of interest using Amazon Location](geofence-an-area.md).

1. Configure Amazon EventBridge to send a notification or initiate a process. For more information, see [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md).

1. Display your tracked assets and your active geofences on a map. For more information, see [Using maps](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html).

1. Save location data in long-term storage for further analysis.

1. Once you have built your application, you can use Amazon CloudWatch and AWS CloudTrail to manage your application. For more information, see [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
