---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/user-engagement-geomarketing.html
---

# User engagement and geomarketing applications
<a name="user-engagement-geomarketing"></a>

The following is an illustration of a user engagement and geomarketing application architecture using Amazon Location:

With this architecture, you can:
+ Initiate events based on the proximity of a target so that you can send oﬀers to nearby customers or engage those who recently left your establishment (called *geotargeting*).
+ Visualize customer device locations on a map to monitor trends over time.
+ Store customer device locations that you can analyze over time.
+ Analyze location history to identify trends and opportunities for optimization.

![Architecture diagram showing location tracking flow from customers through mobile client to AWS services including EventBridge , Lambda , SNS, S3, and Redshift.](http://docs.aws.amazon.com/location/previous/developerguide/images/geomarketing.PNG)

The following is an overview of the steps required to build a user engagement and geomarketing application:

1. Create your geofences in Geofence Collections and link Trackers to them. For more information, see [Geofencing an area of interest using Amazon Location](geofence-an-area.md).

1. Configure Amazon EventBridge to send a notification to customers who enter or exit a geofenced area of interest. For more information, see [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md).

1. Display customer locations and geofences on a map. For more information, see [Using maps](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html).

1. Save location data to long-term storage for further analysis.

1. Once you have built your application, you can use Amazon CloudWatch and AWS CloudTrail to manage your application. For more information, see [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
