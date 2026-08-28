---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-architecture.html
---

# Amazon SQS access control architecture
<a name="sqs-creating-custom-policies-architecture"></a>

The following diagram describes the access control for your Amazon SQS resources.

![Describes access control for your Amazon SQS resources.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/AccessPolicyLanguage_Arch_Overview.png)

![In the previous diagram, section number one.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-1-red.png) You, the resource owner.

![In the previous diagram, section number two.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-2-red.png) Your resources contained within the AWS service (for example, Amazon SQS queues).

![In the previous diagram, section number three.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-3-red.png) Your policies. It is a good practice to have one policy per resource. The AWS service provides an API you use to upload and manage your policies.

![In the previous diagram, section number four.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-4-red.png) Requesters and their incoming requests to the AWS service.

![In the previous diagram, section number five.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/number-5-red.png) The access policy language evaluation code. This is the set of code within the AWS service that evaluates incoming requests against the applicable policies and determines whether the requester is allowed access to the resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
