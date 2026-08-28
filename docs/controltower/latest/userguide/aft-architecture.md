---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-architecture.html
---

# AFT Architecture
<a name="aft-architecture"></a>

## Order of operations
<a name="aft-operation"></a>

 You run AFT operations in the AFT management account. For a full account provisioning workflow, the order of stages from left to right in the diagram are as follows:

1.  Account requests are created and submitted to the pipeline. You can create and submit more than one account request at a time. Account Factory processes requests in a first-in-first-out order. For more information, see [Submit multiple account requests](https://docs.aws.amazon.com/controltower/latest/userguide/aft-multiple-account-requests.html).

1.  Each account is provisioned. This stage runs in the AWS Control Tower management account.

1.  Global customizations run in the pipelines that are created for each vended account.

1.  If customizations are specified in the initial account provisioning requests, the customizations run only on targeted accounts. If you have an account that's already provisioned, you must initiate further customizations manually in the account's pipeline.

**AWS Control Tower Account Factory for Terraform – account provisioning workflow **

![Figure: AFT Workflow Diagram](http://docs.aws.amazon.com/controltower/latest/userguide/images/high-level-aft-diagram.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
