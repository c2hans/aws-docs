---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/mapssoattributestocdattributes.html
---

# Mapping user attributes between IAM Identity Center and Microsoft AD directory
<a name="mapssoattributestocdattributes"></a>

You can use the following procedure to specify how your user attributes in IAM Identity Center should map to corresponding attributes in your Microsoft AD directory.

**To map attributes in IAM Identity Center to attributes in your directory**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Attributes for access control** tab, and then choose **Manage Attributes**.

1. On the **Manage attribute for access control** page, find the attribute in IAM Identity Center that you want to map and then type a value in the text box. For example, you might want to map the IAM Identity Center user attribute **`email`** to the Microsoft AD directory attribute **`${mail}`**.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
