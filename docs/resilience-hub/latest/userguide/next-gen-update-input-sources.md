---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-update-input-sources.html
---

# Update input sources
<a name="next-gen-update-input-sources"></a>

To change where the next generation of Resilience Hub looks for resources, add or remove input sources on the service. See [Add input sources to a service](next-gen-add-input-source.md) for instructions on adding input sources.

**To remove an input source (console)**

1. Open the Next generation Resilience Hub console and navigate to your service.

1. Choose the **Configuration** tab.

1. Choose **Edit**.

1. Remove existing input source selections.

1. Choose **Save changes**.

**To remove an input source (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 delete-input-source \
    --service-arn "{{service-arn}}" \
    --input-source-id "{{input-source-id}}"
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
