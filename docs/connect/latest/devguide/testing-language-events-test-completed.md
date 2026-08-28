---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/testing-language-events-test-completed.html
---

# Test completed
<a name="testing-language-events-test-completed"></a>

Triggered when the test execution ends. This event is observed when the test is terminated.

## Parameters
<a name="testing-language-events-test-completed-parameters"></a>
+ Type - Must always be `TestCompleted`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties - Empty object. No additional properties are required.

```
{
    "Identifier": "unique identifier",
    "Type": "TestCompleted",
    "Actor": "System",
    "Properties": {}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
