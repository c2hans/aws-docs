---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-list-describe-systems.html
---

# List and describe systems
<a name="next-gen-list-describe-systems"></a>

**To view your systems (console)**

1. Open the Next generation Resilience Hub console.

1. In the navigation pane, choose **Systems**.

1. The systems list shows all systems in your account with their name, number of services, and creation date.

1. To view details for a specific system, choose the system name.

**To list systems (AWS CLI)**
+ Run the following commands:

  ```
  aws resiliencehubv2 list-systems

  aws resiliencehubv2 get-system \
    --system-arn "arn:aws:resiliencehub:{{region}}:{{account-id}}:system/{{system-name}}:{{id}}"
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
