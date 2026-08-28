---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/edit-schema-mapping.html
---

# Editing a schema mapping
<a name="edit-schema-mapping"></a>

You can only edit a schema mapping before you associate it to a workflow. After you've associated a schema mapping to a workflow, you can't edit it. You can clone a schema mapping if you want to use an existing configuration to create a new schema mapping.

**To edit a schema mapping:**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Data preparation**, choose **Schema mappings**.

1. Choose the schema mapping.

1. Choose **Edit**.

1. On the **Specify schema details** page, make any necessary changes and then choose **Next**.

1. On the **Choose matching technique** page, make any necessary changes and then choose **Next**.

1. On the **Map input fields** page, make any necessary changes and then choose **Next**.

1. On the **Group data** page, make any necessary changes and then choose **Next**.
**Note**
Normalization is only supported for the **Full name**, **Full address**, **Full phone**, and **Email address**.
If you want to normalize the **Full name** sub-types, then assign the following subtypes to the **Full name** group: **First name**, **Middle name**, and **Last name**.
If you want to normalize the **Full address** sub-types, then assign the following subtypes to the **Full address** group: **Street address 1**, **Street address 2**: **Street address 3 name**, **City name**, **State**, **Country**, and **Postal code**.
If you want to normalize the **Full phone** sub-types, then assign the following subtypes to the **Full phone** group: **Phone number**, and **Phone country code**.

1. On the **Review and save** page, make any necessary changes and then choose **Edit schema mapping**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
