---
source_url: https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-cost-attribution.html
---

# Session level cost attribution
<a name="notebooks-spark-cost-attribution"></a>

From Apache Spark version 3.5 release version onward, Athena allows tracking costs for each session. You can define cost allocation tags when starting a session and the reported costs for a session will appear in Cost Explorer or on AWS Billing cost allocation reports. You can also apply cost allocation tags at the Workgroup level and those get copied over to any sessions started on that workgroup.

## Using Session Level Cost Attribution
<a name="notebooks-spark-cost-attribution-usage"></a>

By default, any cost allocation tags specified at the workgroup level is copied over to interactive sessions started on that workgroup.

To disable tags to be copied from the Workgroup when starting an interactive session from the AWS CLI:

```
aws athena start-session \
  --region "REGION" \
  --work-group "WORKGROUP" \
  --tags '[
    {
      "Key": "tag_key",
      "Value": "tag_value"
    }
  ]' \
  --no-copy-work-group-tags
```

To enable tags to be copied from the Workgroup when starting an interactive session from the AWS CLI:

```
aws athena start-session \
  --region "REGION" \
  --work-group "WORKGROUP" \
  --copy-work-group-tags
```

## Considerations and Limitations
<a name="notebooks-spark-cost-attribution-considerations"></a>
+ Session tags overrides workgroup tags with the same keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
