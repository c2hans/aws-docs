---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-submit-pilot.html
---

# Step 8: Submit the pilot and approve the gates
<a name="pb-es68-submit-pilot"></a>

Submit the pilot workflow and watch it through the interactive manage interface:

```
workflow submit
workflow manage
```

Metadata migration runs as two gated steps: `evaluateMetadata` (previews what would be applied) and `migrateMetadata` (writes the changes to the target). Inspect the evaluation result, then approve the gates in order:

```
workflow approve step 'evaluatemetadata.*'
```

After you have reviewed the evaluation and are satisfied with the candidate indexes, templates, and aliases, approve the metadata migration step:

```
workflow approve step 'migratemetadata.*'
```

The workflow then proceeds to the document backfill for the indexes in your `indexAllowlist`. Use `workflow status` and `workflow log all --follow` if you need to inspect progress or logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
