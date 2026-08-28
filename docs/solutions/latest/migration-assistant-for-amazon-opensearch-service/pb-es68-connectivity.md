---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-connectivity.html
---

# Step 7: Verify connectivity
<a name="pb-es68-connectivity"></a>

Confirm the Migration Console can reach and authenticate to both clusters before you submit anything:

```
console clusters connection-check
```

To check each side independently:

```
console clusters connection-check --cluster source
console clusters connection-check --cluster target
```

Because the target uses SigV4, also confirm that pod identity is working from the Migration Console pod:

```
aws sts get-caller-identity
```

If any check fails, stop and fix connectivity or authentication first. Do not submit a workflow yet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
