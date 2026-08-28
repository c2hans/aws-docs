---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/testing-language-events-test-initiated.html
---

# Test initiated
<a name="testing-language-events-test-initiated"></a>

Triggered when the test execution begins. This is typically used to set up initial conditions such as override system behaviors before the actual flow execution starts.

## Parameters
<a name="testing-language-events-test-parameters"></a>
+ Identifier - Unique identifier for the event. (API need to specify this identifier in order for the UI to render properly)
+ Type - Must always be `TestInitiated`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties - Empty object. No additional properties are required.

```
{
    "Identifier": "unique identifier",
    "Type": "TestInitiated",
    "Actor": "System",
    "Properties": {}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
