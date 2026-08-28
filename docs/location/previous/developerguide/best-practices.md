---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/best-practices.html
---

# Best practices for Amazon Location Service
<a name="best-practices"></a>

This topic provides best practices to help you use Amazon Location Service. While these best practices can help you take full advantage of the Amazon Location Service, they do not represent a complete solution. You should follow only the recommendations that are applicable for your environment.

**Topics**
+ [Security](#security-best-practice)
+ [Resource management](#resource-best-practice)
+ [Billing and cost management](#cost-best-practice)
+ [Quotas and usage](#quota-best-practice)

## Security
<a name="security-best-practice"></a>

To help manage or even avoid security risks, consider the following best practices:
+ Use identity federation and IAM roles to manage, control, or limit access to your Amazon Location resources. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html) in the *IAM User Guide*.
+ Follow the Principle of Least Privilege to grant only the minimum required access to your Amazon Location Service resources. For more information, see [Managing access using policies](security-iam.md#security_iam_access-manage).
+ For Amazon Location Service resources used in web applications, restrict access using an `aws:referer` IAM condition, limiting use by sites other than those included in the allow-list.
+ Use monitoring and logging tools to track resource access and usage. For more information, see [Logging and Monitoring in Amazon Location Service](security-logging-and-monitoring.md) and [Logging Data Events for Trails ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the AWS CloudTrail User Guide.
+ Use secure connections, such as those that begin with `https://` to add security and protect users against attacks while data is being transmitted between the server and browser.

### Detective security best practices for Amazon Location Service
<a name="security-best-practices-detective"></a>

The following best practices for Amazon Location Service can help detect security incidents:

**Implement AWS monitoring tools**
Monitoring is critical to incident response and maintains the reliability and security of Amazon Location Service resources and your solutions. You can implement monitoring tools from the several tools and services available through AWS to monitor your resources and your other AWS services.
For example, Amazon CloudWatch allows you to monitor metrics for Amazon Location Service and enables you to setup alarms to notify you if a metric meets certain conditions you've set and has reached a threshold you've defined. When you create an alarm, you can set CloudWatch to sent a notification to alert using Amazon Simple Notification Service. For more information, see [Logging and Monitoring in Amazon Location Service](security-logging-and-monitoring.md).

**Enable AWS logging tools**
Logging provides a record of actions taken by a user, role or an AWS service in Amazon Location Service. You can implement logging tools such as AWS CloudTrail to collect data on actions to detect unusual API activity.
When you create a trail, you can configure CloudTrail to log events. Events are records of resource operations performed on or within a resource such as the request made to Amazon Location, the IP address from which the request was made, who made the request, when the request was made, along with additional data. For more information, see [Logging Data Events for Trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the AWS CloudTrail User Guide.

### Preventive security best practices for Amazon Location Service
<a name="security-best-practices-preventive"></a>

The following best practices for Amazon Location Service can help prevent security incidents:

**Use secure connections**
Always use encrypted connections, such as those that begin with `https://` to keep sensitive information secure in transit.

**Implement least privilege access to resources**
When you create custom policies to Amazon Location resources, grant only the permissions required to perform a task. It's recommended to start with a minimum set of permissions and grant additional permissions as needed. Implementing least privilege access is essential to reducing the risk and impact that could result from errors or malicious attacks. For more information, see [Identity and Access Management for Amazon Location Service](security-iam.md).

**Use globally-unique IDs as device IDs**
Use the following conventions for device IDs.
+ Device IDs must be unique.
+ Device IDs should not be secret, because they can be used as foreign keys to other systems.
+ Device IDs should not contain personally-identifiable information (PII), such as phone device IDs or email addresses.
+ Device IDs should not be predictable. Opaque identifiers like UUIDs are recommended.

**Do not include PII in device position properties**
When sending device updates (for example, using [DevicePositionUpdate](https://docs.aws.amazon.com/location/previous/APIReference/API_DevicePositionUpdate.html)), do not include personally-identifiable information (PII) such as phone number or email address in the `PositionProperties`.

## Resource management
<a name="resource-best-practice"></a>

To help effectively manage your location resources in Amazon Location Service, consider the following best practices:
+ Use regional endpoints that are central to your expected user base to improve their experience. For information about region endpoints, see [Amazon Location regions and endpoints](location-regions.md).
+ For resources that use data providers, such as map resources and place index resources, make sure to follow the terms of use agreement of the specific data provider. For more information, see [Data providers](what-is-data-provider.md).
+ Minimize the creation of resources by having one resource for each configuration of map, place index, or routes. Within a region, you typically need only one resource per data provider or map style. Most applications use existing resources, and do not create resources at run time.
+ When using different resources in a single application, such as a map resource and a route calculator, use the same data provider in each resource to ensure that the data matches. For example, that a route geometry you create with your route calculator aligns with the streets on the map drawn using the map resource.

## Billing and cost management
<a name="cost-best-practice"></a>

To help manage your costs and billing, consider the following best practice:
+ Use monitoring tools, such as Amazon CloudWatch, to track your resource usage. You can set alerts that notify you when usage is about to exceed your specified limits. For more information, see [Creating a Billing Alarm to Monitor Your Estimated AWS Charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*.

## Quotas and usage
<a name="quota-best-practice"></a>

You AWS account includes quotas that set a default limit your usage amount. You can set up alarms to alert you when your usage is getting close to your limit, and you can request a raise to a quota, when you need it. For information about how to work with quotas, see the following topics.
+ [Amazon Location Service quotas](location-quotas.md)
+ [Use CloudWatch to monitor usage against quotas](monitoring-using-cloudwatch.md#alarms-on-quotas)
+ [ Visualizing your service quotas and setting alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.html) in the *Amazon CloudWatch User Guide*.

You can create alarms to give you advance warning when you are close to exceeding your limits. We recommend setting alarms for each quota in each AWS Region where you use Amazon Location. For example, you can monitor your use of the `SearchPlaceIndexForText` operation, and create an alarm when you exceed 80 percent of your current quota.

When you get an alarm warning about your quota, you must decide what to do. You might be using additional resources because your customer base has grown. In that case you may want to request an increase to your quota, such as a 50 percent increase in the quota for an API call in that Region. Or, maybe there's an error in your service that causes you to make additional unnecessary calls to Amazon Location. In that case you'd want to solve the problem in your service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
