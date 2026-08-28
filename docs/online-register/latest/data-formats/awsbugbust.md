---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awsbugbust.html
---

# Data retrieval APIs for AWS BugBust
<a name="awsbugbust"></a>

AWS BugBust provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="bugbust-GetEvent"></a>[GetEvent](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View customer details about an event | Read |
| <a name="bugbust-GetJoinEventStatus"></a>[GetJoinEventStatus](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the status of a BugBust player's attempt to join a BugBust event | Read |
| <a name="bugbust-ListBugs"></a>[ListBugs](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the bugs that were imported into an event for players to work on | Read |
| <a name="bugbust-ListEventParticipants"></a>[ListEventParticipants](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the participants of an event | Read |
| <a name="bugbust-ListEventScores"></a>[ListEventScores](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the scores of an event's players | Read |
| <a name="bugbust-ListEvents"></a>[ListEvents](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | List BugBust events | List |
| <a name="bugbust-ListProfilingGroups"></a>[ListProfilingGroups](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the profiling groups that were imported into an event for players to work on | Read |
| <a name="bugbust-ListPullRequests"></a>[ListPullRequests](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | View the pull requests used by players to submit fixes to their claimed bugs in an event | Read |
| <a name="bugbust-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/auth-and-access-control-permissions-reference.html) | Lists tag for a Bugbust resource | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
