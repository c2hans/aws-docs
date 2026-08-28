---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/create-saml-app.html
---

# Create a SAML 2.0 application
<a name="create-saml-app"></a>

In this step, you federate your Identity Provider (IdP) to IAM Identity Center through SAML 2.0, and use IAM Identity Center to manage user access to the solution.

1. Log in to the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. From the left pane, under **Application assignments**, choose **Applications**.

1. On the Applications page, on the **Customer managed** tab, choose **Add application**.

1. On the **Select application type** page, under **Setup preference**, choose **I have an application I want to set up**.

1. Under **Application type**, choose **SAML 2.0**, and choose **Next**.

1. On the **Configure application** page, under **Configure application**,
   + Enter a **Display name** for the application, such as *MyISBApp*,
   + Enter a description.

1. Under **Application metadata**, choose **Manually type your metadata values**, and provide temporary placeholder values for **Application ACS URL** and **Application SAML audience**. You will replace these with the real values after the Data stack is deployed.
   +  **Application ACS URL**: Enter a temporary placeholder URL, such as `https://placeholder.example.com/saml2/idpresponse`. You will replace this with the `CognitoAcsUrl` output from the Data stack in [Update the SAML application configuration](update-saml-app-config.md).
   +  **Application SAML audience**: Enter a temporary placeholder value, such as `urn:amazon:cognito:sp:placeholder`. You will replace this with the `CognitoAudience` output from the Data stack in [Update the SAML application configuration](update-saml-app-config.md).

1. Choose **Submit**. The Application details page displays.

1. Copy the **IAM Identity Center SAML metadata URL** from the application details page — you supply this as the `SamlMetadataUrl` parameter when you deploy the Data stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
