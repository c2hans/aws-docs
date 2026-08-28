---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-validate-pilot.html
---

# Step 9: Validate the pilot
<a name="pb-es68-validate-pilot"></a>

Compare document counts and spot-check content on the Amazon OpenSearch Service domain before you widen scope:

```
console clusters cat-indices --refresh
console clusters curl target /<PILOT_INDEX>/_count
console clusters curl target /<PILOT_INDEX>/_search?size=5&pretty
```

Run representative application queries against the target to confirm clients can find the expected indexes and fields. Because the type-mapping sanitization transformer merges Elasticsearch 6.8 types into a single index, verify that documents from each original type are present and queryable as you expect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
