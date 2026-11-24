---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-monitor.html
---

# Monitor a documentation portal with CloudWatch RUM

You can attach an Amazon CloudWatch RUM app monitor to a documentation portal to collect client-side data from your consumers' sessions: page views, load times, errors, and navigation paths. For more information, see [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html).

**To monitor a portal**

1. In the CloudWatch console, create a RUM app monitor in the portal's Region. For the application domain, enter the portal's domain name.

1. On the portal detail page, choose **Edit portal**, choose the app monitor under **RUM app monitor**, and save.

1. Publish the portal. Data appears in the RUM console as consumers visit.

Standard CloudWatch RUM charges apply.
