---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots-deleting.html
---

# Deleting a graph snapshot
<a name="graph-snapshots-deleting"></a>

 Deleting a graph snapshot is an important task in managing and maintaining your Neptune graph database. The AWS Neptune Console and Command Line Interface (CLI) or Software Development Kit (SDK) provide the necessary tools to accomplish this.

------
#### [ CLI/SDK ]

**Delete a snapshot**

```
aws neptune-graph delete-graph-snapshot \
--snapshot-id <SNAPSHOT_ID>
```

------
#### [ Neptune Console ]

1.  Expand **Analytics** and choose **Snapshots**.

1.  Select the snapshot you want to delete, and choose the **Delete** button.

1.  Type "confirm" in the text box to confirm you want to delete the snapshot, then choose the **Delete** button.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
