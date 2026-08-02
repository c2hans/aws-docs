---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-auth-config.html
---

# Update configuration using AWS AppConfig
<a name="update-auth-config"></a>

In this step, you will collect several configuration values and use them in the authentication configuration section of the solution’s GlobalConfig in AWS AppConfig.

## Save the IAM Identity Center application configuration values
<a name="save-application-config-values"></a>

1. In the IAM Identity Center console in the account where IAM Identity Center is enabled, navigate to the custom SAML 2.0 application created in the [Create a SAML 2.0 application](create-saml-app.md) section.

1. On the custom application’s page, under **Actions**, choose **Edit configuration**. You do not need to edit anything; however, this page contains the authentication configuration values required by the solution.

1. Save the following values to use in the next step:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-auth-config.html)

## Save the IAM Identity Center access portal URL
<a name="save-access-portal-url"></a>

The IAM Identity Center Access Portal URL is used to provide direct links to access sandbox accounts in the solution UI.

You can locate this value in the IAM Identity Center console in the account where IAM Identity Center is enabled from the **Dashboard** page. This page will contain a **Settings summary** that contains the **AWS access portal URL**. Save this value.

## Save the Web app URL
<a name="save-web-app-url"></a>

The Web App URL can be located in the **Hub Account** as an output on the **Compute Stack** in the AWS CloudFormation console. Go to **CloudFormation > Stacks > YourISBComputeStackName** and choose the **Outputs** tab. The Web App URL will be under the output key **CloudFrontDistributionUrl**.

## Updating the global config
<a name="updating-the-global-config"></a>

After you have collected all the necessary configuration values, you can update the solution’s global config with them.

1. Go to the [AWS AppConfig](https://console.aws.amazon.com/systems-manager/appconfig/) console in the **Hub Account**.

1. From the left pane, choose **Applications**.

1. On the Applications page, choose **InnovationSandboxData-Config-Application-XXXXXXX**. The Application details display.

1. Under **Configuration Profiles and Feature Flags**, choose **InnovationSandboxData-Config-GlobalConfigHostedConfiguration-XXXXX** configuration profile, and choose **View details**.

1. Choose **Create version** to begin modifying the current configuration.

1. Set the `maintenanceMode` to `false`. This will allow **manager** and **user** personas to begin to access the solution.

1. In the **auth** section, copy in the corresponding values that you saved in the previous sections ([Save the IAM Identity Center application configuration values](#save-application-config-values), [Save the IAM Identity Center access portal URL](#save-access-portal-url), [Save the Web app URL](#save-web-app-url)).

```
...
# Authentication Configuration
auth:
  idpSignInUrl: " "
  idpSignOutUrl: " "
  idpAudience: "isb"
  webAppUrl: " "
  awsAccessPortalUrl: " "
  sessionDurationInMinutes: 60
...
```

1. Update the **notification** section. Enter a valid email that can send emails from [Amazon Simple Email Service set up in the pre-requisites](prerequisites.md). If you have not completed this prerequisite step automated email notifications will not be sent.

```
...
# Email Notification controls

notification:
  emailFrom: " "
...
```

1. Choose **Create hosted configuration version**.

1. Choose **Start Deployment**, and choose the latest hosted configuration version you just created.

1. Choose **Start Deployment**.

**Note**
When updating these configuration values, be mindful of the formatting, white space, and capitalization; otherwise, the solution may not function properly.
