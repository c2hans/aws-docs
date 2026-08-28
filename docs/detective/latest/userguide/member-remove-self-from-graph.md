---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/member-remove-self-from-graph.html
---

# Removing your account from a behavior graph
<a name="member-remove-self-from-graph"></a>

After you accept an invitation, you can remove your account from a behavior graph at any time. When you remove your account from a behavior graph, Amazon Detective stops ingesting data from your account into the behavior graph. Existing data remains in the behavior graph.

Only invited accounts can remove their account from a behavior graph. Organization accounts cannot remove their account from the organization behavior graph.

## Removing your account from a behavior graph (Console)
<a name="member-remove-self-console"></a>

You can use the AWS Management Console to remove your account from a behavior graph.

**To remove your account from a behavior graph (console)**

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/).

1. In the Detective navigation pane, choose **Account management**.

1. Under **My administrator accounts**, for the behavior graph you want to resign from, choose **Resign**.

## Removing your account from a behavior graph (Detective API, AWS CLI)
<a name="member-remove-self-api"></a>

You can use the Detective API or the AWS Command Line Interface to remove your account from a behavior graph.

**To remove your account from a behavior graph (Detective API, AWS CLI)**
+ **Detective API:** Use the [`DisassociateMembership`](https://docs.aws.amazon.com/detective/latest/APIReference/API_DisassociateMembership.html) operation. You must specify the graph ARN.
+ **AWS CLI:** At the command line, run the [`disassociate-membership`](https://docs.aws.amazon.com/cli/latest/reference/detective/disassociate-membership.html) command.

  ```
  aws detective disassociate-membership --graph-arn {{<behavior graph ARN>}}
  ```

  Example:

  ```
  aws detective disassociate-membership --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
