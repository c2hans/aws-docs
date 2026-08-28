---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/data-retention.html
---

# Data retention in Amazon Location
<a name="data-retention"></a>

The following characteristics relate to how Amazon Location collects and stores data for the service:
+ **Amazon Location Service Trackers** – When you use the Trackers APIs to track the location of entities, their coordinates can be stored. Device locations are stored for 30 days before being deleted by the service.
+ **Amazon Location Service Geofences** – When you use the Geofences APIs to define areas of interest, the service stores the geometries you provided. They must be explicitly deleted.
**Note**
Deleting your AWS account delete all resources within it. For additional information, see the [AWS Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
