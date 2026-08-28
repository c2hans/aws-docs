---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-delete-system.html
---

# Delete a system
<a name="next-gen-delete-system"></a>

A system cannot be deleted while it has service associations. When you delete a system using the console, it automatically removes the service associations for you. When using the AWS CLI, you must remove all service associations first, then delete the system.

**To delete a system (console)**

1. Open the Next generation Resilience Hub console.

1. In the navigation pane, choose **Systems**.

1. Select the system you want to delete.

1. Choose **Actions**, then choose **Delete**.

1. In the confirmation dialog, select the deletion acknowledgement checkbox and choose **Delete**.

**To delete a system (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 delete-system \
    --system-arn "arn:aws:resiliencehub:{{region}}:{{account-id}}:system/{{system-name}}:{{id}}"
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
