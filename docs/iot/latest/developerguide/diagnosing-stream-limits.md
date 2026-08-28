---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-stream-limits.html
---

# Diagnosing Stream Limits
<a name="diagnosing-stream-limits"></a>

**Troubleshooting "Stream limit exceeded for your AWS account"**

If you see `"Error: You have exceeded the limit for the number of streams in your AWS account."`, you can clean up the unused streams in your account instead of requesting a limit increase.

To clean up an unused stream that you created using the AWS CLI or SDK:

```
aws iot delete-stream –stream-id {{value}}
```

For more details, see [delete-stream](https://docs.aws.amazon.com/cli/latest/reference/iot/delete-stream.html).

**Note**
You can use the `list-streams` command to find the stream IDs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
