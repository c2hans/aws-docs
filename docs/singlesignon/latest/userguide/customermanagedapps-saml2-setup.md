---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html
---

# Setting up customer managed SAML 2.0 applications
<a name="customermanagedapps-saml2-setup"></a>

If you use customer managed applications that support [SAML 2.0](https://wiki.oasis-open.org/security), you can federate your IdP to IAM Identity Center through SAML 2.0 and use IAM Identity Center to manage user access to those applications. You can select a SAML 2.0 application from a catalog of commonly used applications in the IAM Identity Center console, or you can set up your own SAML 2.0 application.

**Note**
If you have customer managed applications that support OAuth 2.0 and your users need access from these applications to AWS services, you can use trusted identity propagation. With trusted identity propagation, a user can sign in to an application, and that application can pass the users’ identity in requests to access data in AWS services.

**Topics**
+ [Set up an application from the IAM Identity Center application catalog](saasapps.md)
+ [Set up your own SAML 2.0 application](customermanagedapps-set-up-your-own-app-saml2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
