---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-saml-app-config.html
---

# Update the SAML application configuration
<a name="update-saml-app-config"></a>

After deploying the Data stack, update the SAML 2.0 application you created earlier with the actual ACS URL and audience values from the Data stack outputs. To enable IdP-initiated sign-in from the AWS access portal, you also set the **Application start URL** to the solution’s web UI URL.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) in the **Hub** account.

1. Choose the Data stack, and then choose the **Outputs** tab.

1. Note the values for `CognitoAcsUrl` and `CognitoAudience`.

1. Choose the Compute stack, choose the **Outputs** tab, and note the web UI URL (the `CloudFrontDistributionUrl` value). If you configured a custom domain, use that domain instead. For more information, see [Logging into the web UI](log-in-webui.md).

1. Sign in to the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/) in the account where IAM Identity Center is configured.

1. From the left pane, under **Application assignments**, choose **Applications**.

1. On the Applications page, on the **Customer managed** tab, choose the SAML application you created in [Create a SAML 2.0 application](create-saml-app.md).

1. Choose **Actions**, then choose **Edit configuration**.

1. Under **Application metadata**, update the following fields:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-saml-app-config.html)

1. Choose **Submit** to save the updated configuration.

**Note**
The **Application start URL** enables IdP-initiated sign-in, so users can launch the solution from the AWS access portal. If you leave it empty, service provider-initiated sign-in (starting from the web UI URL) still works, but the application does not appear as a launchable tile in the AWS access portal.

**Important**
If these values do not match the Data stack outputs, users will receive a *SAML assertion audience mismatch* error when attempting to sign in to the web application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
