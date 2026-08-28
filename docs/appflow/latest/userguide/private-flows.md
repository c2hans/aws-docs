---
source_url: https://docs.aws.amazon.com/appflow/latest/userguide/private-flows.html
---

# Private Amazon AppFlow flows
<a name="private-flows"></a>

With Amazon AppFlow, you can create private flows between AWS services and supported software as a service (SaaS) applications. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet.

The following SaaS applications are integrated with AWS PrivateLink:
+ Salesforce
+ Singular
+ Snowflake
+ Trend Micro

**Note**
Your SaaS account must be enabled for AWS PrivateLink access. Please check with the administrator for the SaaS application.

When you create a connection using AWS PrivateLink, Amazon AppFlow creates the VPC endpoint service configuration for you. When you no longer need the endpoint service configuration, Amazon AppFlow deletes it.

**Note**
Amazon AppFlow makes metadata API calls to populate a list of objects and fields in the console over the public endpoints. However, the actual data transfer during the flow run happens over Amazon VPC endpoints powered by AWS PrivateLink.

The following diagram illustrates the components of a private flow.

![A private flow using AWS PrivateLink](http://docs.aws.amazon.com/appflow/latest/userguide/images/PrivateLink%20for%20AppFlow.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon AppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
