---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aossec02-bp02.html
---

# AOSSEC02-BP02 Track OpenSearch Service API calls
<a name="aossec02-bp02"></a>

 Monitor and log all API calls made to your OpenSearch Service, which provides visibility into access and empowers your team to take swift action against unauthorized activity.

 **Level of risk exposed if this best practice is not established:** High

 **Desired outcome:** OpenSearch Service API calls are tracked and logged.

 **Benefits of establishing this best practice:**
+  Improved visibility and control of access to sensitive data
+  Enhanced ability to detect and respond to unauthorized access

## Implementation guidance
<a name="implementation-guidance-15"></a>

 Amazon OpenSearch Service seamlessly integrates with AWS CloudTrail, which logs actions performed by users, roles, or AWS services within OpenSearch Service. The captured calls include calls from the OpenSearch Service console, AWS CLI, or an AWS SDK. If you create a trail, you can enable continuous delivery of CloudTrail events to an S3 bucket, including events for OpenSearch Service. If you don't configure a trail, you can still view the most recent events on the CloudTrail console in Event history.

 Using the information collected by CloudTrail, you can determine the request that was made to OpenSearch Service, the IP address from which the request was made, who made the request, when it was made, and other details.

 All OpenSearch Service configuration API actions are logged by CloudTrail and are documented in the [Amazon OpenSearch Service API Reference](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html). For detail on Amazon OpenSearch Service log entries in AWS CloudTrail, see [Monitoring Amazon OpenSearch Service API calls with AWS CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudtrailauditing.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
