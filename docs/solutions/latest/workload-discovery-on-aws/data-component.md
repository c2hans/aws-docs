---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/data-component.html
---

# Data component
<a name="data-component"></a>

 **Workload Discovery on AWS data component**

![workload discovery data component](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-data-component.png)

The web UI sends requests to the AppSync API, which invokes either the `Gremlin Resolver` or `Search Resolver` Lambda functions. These functions process the requests and query Amazon Neptune or OpenSearch Service to retrieve data about the provided resources. AWS AppSync also supports requests for the estimated cost data from the AWS CUR.

The [discovery component](discovery-component.md) sends requests to the AppSync API to read from and persist data in the Amazon Neptune and OpenSearch Service databases. The API receives requests from the AWS Fargate task in the discovery component. The API is then authenticated using an IAM role that provides access to the databases.
