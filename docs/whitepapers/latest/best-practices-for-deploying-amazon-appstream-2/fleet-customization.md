---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/fleet-customization.html
---

# Fleet customization
<a name="fleet-customization"></a>

## Fleet type
<a name="fleet-type"></a>

When creating a fleet, customers must choose a fleet type. Each fleet type provides different benefits for user experience, cost and maintenance overhead. Regardless of the fleet type chosen, each option supports both the Windows and Linux platform types, and Desktop View or Application View.

Customers can now choose from the following fleet types:
+  **Always-On** — This fleet type provides users with instant-on access to their apps. You will be charged for all running instances in your fleet even if no users are streaming apps.
+  **On-Demand** — Select this fleet type to optimize your streaming costs. With an on-demand fleet, users will experience a start time of about one to two minutes for their session. However, you will only be charged the streaming instance fees when users are connected, and a small hourly fee for each instance in the fleet that is not streaming apps.
+  **Elastic** — Elastic fleets can be used for applications that don’t require installation and can be run from a virtual hard disk (VHD). Elastic fleets don’t support WorkSpaces Applications images, nor do they require scaling policies. You are charged only for the duration of a streaming session.

*Table 2 — Amazon WorkSpaces Applications fleet types*

| Fleet type | When to use | User experience |  Pricing model | Notes  |
| --- | --- | --- | --- | --- |
|  **Always-On**  | Your users require instant access to applications when they start a session. You will not have significant excess capacity in your fleet, perhaps because your usage patterns are predictable and you can reliably control costs with scaling policies. | Instant access to applications | You pay full price for every instance that is available in your fleet (regardless of whether it's being used for a session). | Supports custom image and scaling policies. |
|  **On-Demand**  | You must maintain significant excess capacity in your fleetsYou want the most cost optimized environment and don’t want to pay full price for unused capacityYour users can wait one to two minutes to access their applications after starting a session.You are using larger instance types. The hourly cost of a running instance is much more expensive than the stopped instance fee. | Users wait one to two minutes to access their applications after starting a session. | You pay full price only for streaming instances with an active session, and then a small hourly cost for idle instances. | Supports custom image and scaling policies. |
|  **Elastic**  | Your application and its dependencies are smaller than \~1.5 GB. Every time a user starts a session in an Elastic fleet, your virtual hard disk (VHD) file must be downloaded from Amazon S3 into the session. As a result, larger VHD files (i.e. greater than 1.5 GB in size) will result in a poor end user experience.Your application is portable. That is, your application and all its dependencies can be placed onto a VHD and launched from the VHD.You do not require domain joined streaming instances (domain joining is not currently available with Elastic fleets)You want to pay only for active sessions (i.e. you don’t pay for unused capacity in your fleet).Your users can wait 45 seconds or more to access their applications after starting a session.You want AWS to manage scaling for you (no scaling policies to manage). | User waits 45 seconds to 3 minutes to access applications after starting session (wait time is dependent on size of Virtual Hard Disk). | You are charged only for the duration of a streaming session. Because there is no concept of idle instances with Elastic fleets, you incur no charges for unused instances. | Does not support custom image (customer provides VHD with applications) or scaling policies. Currently supports `stream.standard.small` and `stream.standard.medium` instances. If your use case requires a different instance type, please contact your AWS account team. |

![An diagram showing fleet type use cases and requirements..](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/use-case-and-requirements.png)

## Fleet sizing
<a name="fleet-sizing"></a>

### Minimum capacity and scheduled scaling
<a name="minimum-capacity-and-scheduled-scaling"></a>

 When sizing your WorkSpaces Applications fleet, there are several considerations that directly translate to user experience and cost. The value entered for **Minimum capacity** ensures that the number of WorkSpaces Applications instances will seldom be less than this value. After an WorkSpaces Applications session is ended, if the total WorkSpaces Applications instances are less than the **Minimum capacity** value, a new fleet instance starts. As always, it is important to remember one WorkSpaces Applications instance maps directly to one user session, directly influencing the value for **Minimum capacity**.

 Entering a value for **Minimum capacity** that is beyond the anticipated concurrency results in increased cost, although user experience is not impacted. A value that is too low results in low costs, but impacts user experience when total requests exceed the available capacity. Administrators will observe “Insufficient Capacity” errors in this type of situation. For example, waiting for `PendingCapacity` become `AvailableCapacity` is an inefficient use of the user’s time when the number of anticipated connections at the start of the day is a predictably consistent value.

 Start with a minimum capacity that accommodates typical off-peak hours, and then use [*scheduled scaling policy*](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html) to effectively reset the minimum capacity prior to the start of the work day. Do not forgot to create another scheduled scaling policy to revert the Minimum capacity to the off-peak hours. For more information about scaling policies and how to implement them, refer to the [*Fleet auto-scaling strategies*](fleet-auto-scaling-strategies.md) section in this document.

### Maximum capacity and service quotas
<a name="maximum-capacity-and-service-quotas"></a>

 Setting maximum capacity might appear to be an arbitrary value, but when properly forecasted and set, it optimizes total resource consumption and cost. A value entered that is higher than the [*service quota for the WorkSpaces Applications fleet*](https://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html) in your AWS account can appear to be valid, but, when auto scaling events attempt to scale resources to the maximum capacity, they fail to launch, as the maximum capacity value exceeds the available service quota. Ensure that a service quota request is placed for the desired maximum capacity to ensure automatic scaling functions as your organization anticipates.

 Another important consideration when setting a maximum capacity value is cost. For more information, refer to the [*Optimizing costs with fleet type choice*](cost-optimization.md#optimizing-costs-with-fleet-type-choice) section of this document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
