---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-eventbridge-examples.html
---

# Example event patterns and events
<a name="next-gen-eventbridge-examples"></a>

Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that monitor events from the next generation of Resilience Hub.

**Select all failure mode assessment completion events**
The following pattern matches all completed assessments.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Completed"]
}
```

**Select all failure mode assessment failure events**
The following pattern matches all failed assessments.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Failed"]
}
```

**Select all new dependency discovered events**
The following pattern matches all new dependency events.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["New Dependency Discovered"]
}
```

**Select all events from the next generation of Resilience Hub**
The following pattern matches all events regardless of type.

```
{
  "source": ["aws.resiliencehub"]
}
```

**Select assessment events with high-severity findings**
The following pattern matches assessments that identified at least one high-severity finding.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Completed"],
  "detail": {
    "highSeverityCount": [{"numeric": [">", 0]}]
  }
}
```

The following sections provide example events for each event type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
