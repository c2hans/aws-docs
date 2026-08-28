---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-register-activity.html
---

# Registering an Activity Type with Amazon SWF
<a name="swf-dg-register-activity"></a>

The following example registers an activity type by using the Amazon SWF API. The name and version that you specify during registration form a unique identifier for the activity type within the domain. The specified domain must have already been registered using the `RegisterDomain` action.

The timeout parameters in this example are duration values specified in seconds. You can use the duration specifier `NONE` to indicate no timeout.

```
https://swf.us-east-1.amazonaws.com
RegisterActivityType
{
  "domain" : "867530901",
  "name" : "activityVerify",
  "version" : "1.0",
  "description" : "Verify the customer credit",
  "defaultTaskStartToCloseTimeout" : "600",
  "defaultTaskHeartbeatTimeout" : "120",
  "defaultTaskList" : { "name" : "mainTaskList" },
  "defaultTaskScheduleToStartTimeout" : "1800",
  "defaultTaskScheduleToCloseTimeout" : "5400"
}
```

## See Also
<a name="registering-activity-type-with-swf-see-also"></a>

[RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html) in the *Amazon Simple Workflow Service API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
