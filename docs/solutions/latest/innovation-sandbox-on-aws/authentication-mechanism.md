---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/authentication-mechanism.html
---

# Authentication mechanism
<a name="authentication-mechanism"></a>

Innovation Sandbox on AWS uses the [Single Sign On service](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) from [AWS IAM Identity center](https://aws.amazon.com/iam/identity-center/) for authentication. The authentication is done via a browser with redirects using the [SAML 2.0](https://aws.amazon.com/identity/saml/) protocol.

You must register the web application with the custom SAML 2.0 application, and update the application with the SAML 2.0 application details. Users log in to the web UI from the Applications tab on the [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html), or programmatically using credentials provided by the IAM Identity Center.
