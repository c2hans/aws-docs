---
source_url: https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html
---

# AWS Cloud Map service instances
<a name="working-with-instances"></a>

A service instance contains information about how to locate a resource, such as a web server, for an application. After you register instances, you locate them by using DNS queries or the AWS Cloud Map [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html) API action. The resources you can register include, but aren't limited to, the following:
+ Amazon EC2 instances
+ Amazon DynamoDB tables
+ Amazon S3 buckets
+ Amazon Simple Queue Service (Amazon SQS) queues
+ APIs deployed on top of Amazon API Gateway

You can specify attribute values for services instances, and clients can use these attributes to filter the resources that AWS Cloud Map returns. For example, an application can request resources in a particular deployment stage, like BETA or PROD. You can also use attributes for versioning.

The following procedures describe how you can register resources in your application as service instances, view a list of registered instances in a service, edit certain instance parameters, and deregister an instance.

**Topics**
+ [Registering a resource as an AWS Cloud Map service instance](registering-instances.md)
+ [Listing AWS Cloud Map service instances](listing-instances.md)
+ [Updating an AWS Cloud Map service instance](updating-instances.md)
+ [Deregistering an AWS Cloud Map service instance](deregistering-instances.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
