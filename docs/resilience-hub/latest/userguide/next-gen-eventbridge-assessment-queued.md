---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-eventbridge-assessment-queued.html
---

# Failure mode assessment queued event
<a name="next-gen-eventbridge-assessment-queued"></a>

The following is an example event emitted when an assessment is queued for delayed processing. The assessment is retried and completes within 24 hours.

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Failure Mode Assessment Queued",
  "source": "aws.resiliencehub",
  "account": "111122223333",
  "time": "2026-01-15T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:resiliencehub:us-east-1:111122223333:service/my-service:abc123"
  ],
  "detail": {
    "assessmentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  }
}
```

The `detail` object contains the following fields:

| Field | Description |
| --- | --- |
| assessmentId | The unique identifier of the queued assessment. |

When the queued assessment completes, a separate `Failure Mode Assessment Completed` or `Failure Mode Assessment Failed` event is emitted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
