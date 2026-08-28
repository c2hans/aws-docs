---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/topics-sharing.html
---

# Sharing Quick Sight Topics
<a name="topics-sharing"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  Amazon Quick administrators and authors  |

After you create and publish a Topic, share it with others in your organization. Sharing a Topic allows your users to ask questions in Amazon Quick chat and use the Topic as a data model in analysis sheets.

**To share a Topic**

1. From the Topic page, select the ellipsis menu and choose **Share**.

1. Search for and add specific users or groups.

1. Set permission levels (**Owner** or **Viewer**) and choose **Done**.

| Permission Level | Can Ask Questions | Can Modify Topic | Can Use in Analysis |
| --- | --- | --- | --- |
| Owner | Yes | Yes | Yes |
| Viewer | Yes | No | Yes |

Quick Sight enforces row-level security (RLS) and column-level security (CLS) at the dataset level. Access controls are preserved through the Topic's semantic layer, regardless of how users access the Topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
