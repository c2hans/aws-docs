---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/launch-and-configure-desktop-application.html
---

# Launch and Configure Desktop Application

Before you can create projects and upload assets, you need to launch the desktop application and create a profile.

## Get Your Portal URL
<a name="get-portal-url"></a>

Your IT Administrator should provide you with the portal URL. If you need to retrieve it yourself, you can get it from AWS CloudFormation:

1. Open the AWS CloudFormation console

1. Select your Spatial Data Management stack

1. Choose the **Outputs** tab

1. Copy the value for `PortalUrl`

Alternatively, use the AWS CLI:

```bash
aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <YOUR STACK> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `PortalStackNested`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`PortalCloudFrontDistributionUrl`].OutputValue' --output text
```

For more information on accessing the portal URL, see [Deploy the Solution](deploy-the-solution.md).

## Create Your Profile
<a name="create-profile"></a>

1. Launch the Spatial Data Management desktop application.

1. On **Find your portal** (step 1 of 3), enter your **Portal URL**. This is the URL you copied from the CloudFormation outputs.

1. Select **I confirm this URL is from a trusted source**, and choose **Next**.

1. On **Name your profile** (step 2 of 3), enter a **Profile name** and choose **Next**. A name has 1 to 100 letters, numbers, hyphens, or underscores, with no spaces, for example `demo-env`. The profile is not public and is stored only on your computer.

1. Complete **Review and launch**, step 3 of 3.

1. Sign in with your Amazon Cognito credentials

1. If prompted, change your temporary password

Your profile is now configured and you are ready to start using the application.

![Step 1 of 3 of the desktop application profile setup: Find your portal](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/first-time-profile-setup.png)

![Step 2 of 3 of the desktop application profile setup: Name your profile](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/first-time-profile-name.png)
