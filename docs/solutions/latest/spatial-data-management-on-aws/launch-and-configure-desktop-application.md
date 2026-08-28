---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/launch-and-configure-desktop-application.html
---

# Launch and Configure Desktop Application
<a name="launch-and-configure-desktop-application"></a>

Before you can create projects and upload assets, you need to launch the desktop application and create a profile.

## Get Your Portal URL
<a name="get-portal-url"></a>

Your IT Administrator should provide you with the portal URL. If you need to retrieve it yourself, you can get it from AWS CloudFormation:

1. Open the AWS CloudFormation console

1. Select your Spatial Data Management stack

1. Choose the **Outputs** tab

1. Copy the value for `PortalUrl`

Alternatively, use the AWS CLI:

```
aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <YOUR STACK> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `PortalStackNested`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`PortalCloudFrontDistributionUrl`].OutputValue' --output text
```

For more information on accessing the portal URL, see [Deploy the solution](deploy-the-solution.md).

## Create Your Profile
<a name="create-profile"></a>

1. Launch the Spatial Data Management desktop application

1. On the welcome screen, choose **Add Profile** or **Create New Profile**

1. Enter the profile details:
   +  **Profile Name** – Enter a descriptive name (for example, `Production` or `My Deployment`)
   +  **Portal URL** – Paste the portal URL you copied from CloudFormation outputs

1. Choose **Save** or **Create**

1. Sign in with your Amazon Cognito credentials

1. If prompted, change your temporary password

Your profile is now configured and you are ready to start using the application.

![Create profile on your client application](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/first-time-profile-setup.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
