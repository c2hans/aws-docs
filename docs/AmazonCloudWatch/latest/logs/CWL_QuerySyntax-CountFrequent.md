---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-CountFrequent.html
---

# countFrequent
<a name="CWL_QuerySyntax-CountFrequent"></a>

Use the `countFrequent` command (also available as `count_frequent`) to compute an approximate count of each unique field-value combination, sorted in descending order. The command emits an `_approxcount` field.

**Syntax**

```
| countFrequent {{field}}[, {{field}} ...]
```

The command uses the following arguments:
+ `{{field}}` – One or more fields to count frequencies for.

**Example**
The following query counts the frequency of method and status combinations.

```
fields method, status
| countFrequent method, status
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
