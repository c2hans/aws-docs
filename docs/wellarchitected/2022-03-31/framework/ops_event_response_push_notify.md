---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_event_response_push_notify.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP05 Enable push notifications
<a name="ops_event_response_push_notify"></a>

 Communicate directly with your users (for example, with email or SMS) when the services they use are impacted, and again when the services return to normal operating conditions, to enable users to take appropriate action.

 **Common anti-patterns:**
+  Your application is experiencing a distributed denial of service incident and has been unresponsive for days. There is no error message. You have not sent a notification email. You have not sent text notifications. You have not shared information on social media. You customers are frustrated and looking for other vendors who can support them.
+  On Monday, your application had issues following a patch and was down for a couple of hours. On Tuesday, your application had issues following a code deployment and was unreliable for a couple of hours. On Wednesday, your application had issues following a code deployment to mitigate a security vulnerability associated to the failed patch and was unavailable for a couple of hours. On Thursday, your frustrated customers started looking for another vendor who could support them.
+  Your application is going to be down for maintenance this weekend. You don't inform your customers. Some of your customers had scheduled activities involving the use of your application. They are very frustrated upon discovery that your application is not available.

 **Benefits of establishing this best practice:** By defining notifications, triggers for notifications, and procedures for notifications you enable your customer to be informed and respond when issues with your workload impact them.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Enable push notifications: Communicate directly with your users (for example, with email or SMS) when the services they use are impacted, and when the services return to normal operating conditions, to enable users to take appropriate action.
  +  [Amazon SES features](https://aws.amazon.com/ses/details/)
  +  [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
  +  [Set up Amazon SNS notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon SES features](https://aws.amazon.com/ses/details/)
+  [Set up Amazon SNS notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html)
+  [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
