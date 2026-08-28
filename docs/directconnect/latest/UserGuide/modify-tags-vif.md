---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/modify-tags-vif.html
---

# Add or remove Direct Connect virtual interface tags
<a name="modify-tags-vif"></a>

Tags provide a way to identify the virtual interface. You can add or remove a tag using either the Direct Connect console or using the command line or API if you are the account owner for the virtual interface.

**To add or remove a virtual interface tag**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1.  Select the virtual interface and then choose **Edit**.

1. Add or remove a tag.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Edit virtual interface**.

**To add a tag or remove a tag using the command line**
+ [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/tag-resource.html) (AWS CLI)
+ [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/directconnect/untag-resource.html) (AWS CLI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
