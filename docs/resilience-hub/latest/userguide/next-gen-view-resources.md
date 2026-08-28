---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-view-resources.html
---

# View discovered resources
<a name="next-gen-view-resources"></a>

**To view resources (console)**

1. Open the Next generation Resilience Hub console and navigate to your service.

1. Choose **Service topology**.

1. The resources graph and resources list show all discovered resources with their type, Region, and associated service function.

1. Use the filters to narrow by Region or service function.

**To list resources (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 list-resources \
    --service-arn "{{service-arn}}"
  ```

  To filter by Region:

  ```
  aws resiliencehubv2 list-resources \
    --service-arn "{{service-arn}}" \
    --aws-region "{{region}}"
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
