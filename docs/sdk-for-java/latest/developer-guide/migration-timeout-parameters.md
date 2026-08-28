---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-timeout-parameters.html
---

# Timeout parameter changes
<a name="migration-timeout-parameters"></a>

In version 1, timeout values were specified as integer values representing milliseconds. In version 2, timeout parameters use `java.time.Duration` objects for better type safety and clarity.

You can convert numeric timeout values automatically using the [migration tool](migration-tool.md), or you can convert them manually by wrapping your numeric values with the appropriate `Duration` factory method.

**Example - Set a request timeout in version 1**

```
// Set request timeout in milliseconds
ClientConfiguration clientConfiguration = new ClientConfiguration();
clientConfiguration.setRequestTimeout(5000); // 5 seconds
```

**Example - Set a request timeout in version 2**

```
// Set request timeout using Duration
ClientConfiguration clientConfiguration = new ClientConfiguration();
clientConfiguration.setRequestTimeout(Duration.ofMillis(5000)); // 5 seconds

// Or more clearly:
clientConfiguration.setRequestTimeout(Duration.ofSeconds(5)); // 5 seconds
```

You can use the following `Duration` factory methods for timeout values:
+ `Duration.ofMillis(long millis)` - For millisecond values.
+ `Duration.ofSeconds(long seconds)` - For second values.
+ `Duration.ofMinutes(long minutes)` - For minute values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
