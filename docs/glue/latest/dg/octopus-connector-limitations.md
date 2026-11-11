---
source_url: https://docs.aws.amazon.com/glue/latest/dg/octopus-connector-limitations.html
---

# Limitations and notes for the Octopus Deploy connector
<a name="octopus-connector-limitations"></a>

The following are limitations and notes for the Octopus Deploy connector:
+ Octopus Deploy is supported as a source only. Writing to Octopus Deploy is not supported.
+ The `tasks` entity returns the tasks for one space. System tasks that don't belong to a space aren't returned.
+ Job bookmarks are not supported.
