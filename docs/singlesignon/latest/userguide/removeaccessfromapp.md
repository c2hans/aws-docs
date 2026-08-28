---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/removeaccessfromapp.html
---

# Remove user access to SAML 2.0 applications
<a name="removeaccessfromapp"></a>

Use this procedure to remove user access to SAML 2.0 applications in the application catalog or custom SAML 2.0 applications. For more information on authentication sessions and durations, see [Understanding authentication sessions in IAM Identity Center](authconcept.md).

**To remove user access to an application**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Applications**.

1. In the list of applications, choose the application from which you want to remove user access.

1. On the application details page, in the **Assigned users** section, select the user or group that you want to remove and then choose the **Remove access** button.

1. In the **Remove access** dialog box, verify the user or group name. Then choose **Remove access**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
