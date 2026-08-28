---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-change-idp-metadata.html
---

# How to change an external identity provider's metadata in IAM Identity Center
<a name="how-to-change-idp-metadata"></a>

You can change your external identity provider's metadata which you previously supplied to the IAM Identity Center. These changes affect your users' ability to sign in and access AWS resources through IAM Identity Center. The following procedure describes how to update your external IdP's metadata that is stored in IAM Identity Center. To complete this procedure, you'll need an Organization instance of IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md).

**To change an external identity provider's metadata**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab. Choose **Actions** and then choose **Manage Authentication**.

1. In the **Identity provider metadata** section, choose **Edit IdP metadata**. You can make the changes to the IdP sign-in URL and or IdP issuer URL for your external IdP on this page. Choose **Save changes** when you've made all the necessary changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
