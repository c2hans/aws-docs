---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html
---

# Components of a Configuration Item
<a name="config-item-table"></a>

A *configuration item* represents a point-in-time view of the various attributes of a supported AWS resource that exists in your account. The components of a configuration item include metadata, attributes, relationships, current configuration, and related events. AWS Config creates a configuration item whenever it detects a change to a resource type that it is recording. For example, if AWS Config is recording Amazon S3 buckets, AWS Config creates a configuration item whenever a bucket is created, updated, or deleted. You can also select for AWS Config to create a configuration item at the recording frequency that you set.

A configuration item consists of the following components.

****

| Component | Description | Contains |
| --- | --- | --- |
| Metadata | Information about this configuration item | [See the AWS documentation website for more details](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) |
| Attributes | Resource attributes | [See the AWS documentation website for more details](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) |
| Relationships | How the resource is related to other resources associated with the account | Description of the relationship, such as Amazon EBS volume vol-1234567 is attached to an Amazon EC2 instance i-a1b2c3d4 |
| Current configuration | Information returned through a call to the Describe or List API of the resource | For example, DescribeVolumes API returns the following information about the volume: [See the AWS documentation website for more details](http://docs.aws.amazon.com/config/latest/developerguide/config-item-table.html) |

**Notes**

1. A configuration item relationship does not include network flow or data flow dependencies. Configuration items cannot be customized to represent your application architecture.

1. As of Version 1.3, the relatedEvents field is empty. You can access the [LookupEvents API](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) in the *AWS CloudTrail API Reference* to retrieve the events for the resource.

1. As of Version 1.3, the configurationItemMD5Hash field is empty. You can use the configurationStateId field to ensure you have the latest configuration item.

1. If a resource type does not support tagging or does not include tag information in its describe API response, AWS Config won't capture tag data in the configuration items (CIs) for that resource type. AWS Config will still record these resources. However, any functionality that relies on tag data won't work. This affects tag-based filtering, grouping, or compliance evaluation that relies on tag data.
