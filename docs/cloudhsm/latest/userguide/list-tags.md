---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-tags.html
---

# List tags for AWS CloudHSM resources
<a name="list-tags"></a>

You can list tags for a cluster from the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/), the [AWS CLI](https://aws.amazon.com/cli/), or the AWS CloudHSM API.

**To list tags (console)**

1. Open the AWS CloudHSM console at [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home).

1. Choose the cluster whose tags you are listing.

1. Choose **Tags**.

**To list tags (AWS CLI)**
+ At a command prompt, issue the [**list-tags**](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/list-tags.html) command, specifying the ID of the cluster whose tags you are listing. If you don't know the cluster ID, issue the **[describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html)** command.

  ```
  $ aws cloudhsmv2 list-tags --resource-id {{<cluster ID>}}
  {
      "TagList": [
          {
              "Key": "Cost Center",
              "Value": "12345"
          }
      ]
  }
  ```

**To list tags (AWS CloudHSM API)**
+ Send a [ListTags](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ListTags.html) request, specifying the ID of the cluster whose tags you are listing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
