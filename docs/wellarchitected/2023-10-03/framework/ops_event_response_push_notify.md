---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_event_response_push_notify.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP05 Define a customer communication plan for outages
<a name="ops_event_response_push_notify"></a>

 Define and test a communication plan for system outages that you can rely on to keep your customers and stakeholders informed during outages. Communicate directly with your users both when the services they use are impacted and when services return to normal.

 **Desired outcome:**
+  You have a communication plan for situations ranging from scheduled maintenance to large unexpected failures, including invocation of disaster recovery plans.
+  In your communications, you provide clear and transparent information about systems issues to help customers avoid second guessing the performance of their systems.
+  You use custom error messages and status pages to reduce the spike in help desk requests and keep users informed.
+  The communication plan is regularly tested to verify that it will perform as intended when a real outage occurs.

 **Common anti-patterns:**
+ A workload outage occurs but you have no communication plan. Users overwhelm your trouble ticket system with requests because they have no information on the outage.
+ You send an email notification to your users during an outage. It doesn’t contain a timeline for restoration of service so users cannot plan around the outage.
+ There is a communication plan for outages but it has never been tested. An outage occurs and the communication plan fails because a critical step was missed that could have been caught in testing.
+  During an outage, you send a notification to users with too many technical details and information under your AWS NDA.

 **Benefits of establishing this best practice:**
+  Maintaining communication during outages ensures that customers are provided with visibility of progress on issues and estimated time to resolution.
+  Developing a well-defined communications plan verifies that your customers and end users are well informed so they can take required additional steps to mitigate the impact of outages.
+  With proper communications and increased awareness of planned and unplanned outages, you can improve customer satisfaction, limit unintended reactions, and drive customer retention.
+  Timely and transparent system outage communication builds confidence and establishes trust needed to maintain relationships between you and your customers.
+  A proven communication strategy during an outage or crisis reduces speculation and gossip that could hinder your ability to recover.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Communication plans that keep your customers informed during outages are holistic and cover multiple interfaces including customer facing error pages, custom API error messages, system status banners, and health status pages. If your system includes registered users, you can communicate over messaging channels such as email, SMS or push notifications to send personalized message content to your customers.

 **Customer communication tools**

 As a first line of defense, web and mobile applications should provide friendly and informative error messages during an outage as well as have the ability to redirect traffic to a status page. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a fully managed content delivery network (CDN) that includes capabilities to define and serve custom error content. Custom error pages in CloudFront are a good first layer of customer messaging for component level outages. CloudFront can also simplify managing and activating a status page to intercept all requests during planned or unplanned outages.

 Custom API error messages can help detect and reduce impact when outages are isolated to discrete services. [Amazon API Gateway](https://aws.amazon.com/api-gateway/) allows you to configure custom responses for your REST APIs. This allows you to provide clear and meaningful messaging to API consumers when API Gateway is not able to reach backend services. Custom messages can also be used to support outage banner content and notifications when a particular system feature is degraded due to service tier outages.

 Direct messaging is the most personalized type of customer messaging. [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) is a managed service for scalable multichannel communications. Amazon Pinpoint allows you to build campaigns that can broadcast messages widely across your impacted customer base over SMS, email, voice, push notifications, or custom channels you define. When you manage messaging with Amazon Pinpoint, message campaigns are well defined, testable, and can be intelligently applied to targeted customer segments. Once established, campaigns can be scheduled or started by events and they can easily be tested.

 **Customer example**

 When the workload is impaired, AnyCompany Retail sends out an email notification to their users. The email describes what business functionality is impaired and provides a realistic estimate of when service will be restored. In addition, they have a status page that shows real-time information about the health of their workload. The communication plan is tested in a development environment twice per year to validate that it is effective.

 **Implementation steps**

1.  Determine the communication channels for your messaging strategy. Consider the architectural aspects of your application and determine the best strategy for delivering feedback to your customers. This could include one or more of the guidance strategies outlined including error and status pages, custom API error responses, or direct messaging.

1.  Design status pages for your application. If you’ve determined that status or custom error pages are suitable for your customers, you’ll need to design your content and messaging for those pages. Error pages explain to users why an application is not available, when it may become available again, and what they can do in the meantime. If your application uses Amazon CloudFront you can serve [custom error responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.html) or use Lambda at Edge to [translate errors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-update-error-status-examples) and rewrite page content. CloudFront also makes it possible to swap destinations from your application content to a static [Amazon S3](https://aws.amazon.com/s3/) content origin containing your maintenance or outage status page .

1.  Design the correct set of API error statuses for your service. Error messages produced by API Gateway when it can’t reach backend services, as well as service tier exceptions, may not contain friendly messages suitable for display to end users. Without having to make code changes to your backend services, you can configure API Gateway [custom error responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.html) to map HTTP response codes to curated API error messages.

1.  Design messaging from a business perspective so that it is relevant to end users for your system and does not contain technical details. Consider your audience and align your messaging. For example, you may steer internal users towards a workaround or manual process that leverages alternate systems. External users may be asked to wait until the system is restored, or subscribe to updates to receive a notification once the system is restored. Define approved messaging for multiple scenarios including unexpected outages, planned maintenance, and partial system failures where a particular feature may be degraded or unavailable.

1.  Templatize and automate your customer messaging. Once you have established your message content, you can use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html) or other tools to automate your messaging campaign. With Amazon Pinpoint you can create customer target segments for specific affected users and transform messages into templates. Review the [Amazon Pinpoint tutorial](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tutorials.html) to get an understanding of how-to setup a messaging campaign.

1.  Avoiding tightly coupling messaging capabilities to your customer facing system. Your messaging strategy should not have hard dependencies on system data stores or services to verify that you can successfully send messages when you experience outages. Consider building the ability to send messages from more than [one Availability Zone or Region](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html) for messaging availability. If you are using AWS services to send messages, leverage data plane operations over [control plane operation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_avoid_control_plane.html) to invoke your messaging.

 **Level of effort for the implementation plan:** High. Developing a communication plan, and the mechanisms to send it, can require a significant effort.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS07-BP03 Use runbooks to perform procedures](ops_ready_to_support_use_runbooks.md) - Your communication plan should have a runbook associated with it so that your personnel know how to respond.
+  [OPS11-BP02 Perform post-incident analysis](ops_evolve_ops_perform_rca_process.md) - After an outage, conduct post-incident analysis to identify mechanisms to prevent another outage.

 **Related documents:**
+ [ Error Handling Patterns in Amazon API Gateway and AWS Lambda](https://aws.amazon.com/blogs/compute/error-handling-patterns-in-amazon-api-gateway-and-aws-lambda/)
+ [ Amazon API Gateway responses ](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gatewayResponse-definition.html#supported-gateway-response-types)

 **Related examples:**
+ [AWS Health Dashboard ](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/)
+ [ Summary of the AWS Service Event in the Northern Virginia (US-EAST-1) Region ](https://aws.amazon.com/message/12721/)

 **Related services:**
+ [AWS Support](https://aws.amazon.com/premiumsupport/)
+ [AWS Customer Agreement ](https://aws.amazon.com/agreement/)
+ [ Amazon CloudFront ](https://aws.amazon.com/cloudfront/)
+ [ Amazon API Gateway ](https://aws.amazon.com/api-gateway/)
+ [ Amazon Pinpoint ](https://aws.amazon.com/pinpoint/)
+ [ Amazon S3 ](https://aws.amazon.com/s3/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
