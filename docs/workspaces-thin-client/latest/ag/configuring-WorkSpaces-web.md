---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-WorkSpaces-web.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Configuring Amazon WorkSpaces Secure Browser for Amazon WorkSpaces Thin Client
<a name="configuring-WorkSpaces-web"></a>

Amazon WorkSpaces Secure Browser are based on their web portal endpoints on the WorkSpaces Thin Client **Create environment** page within AWS console.

**Note**
Configurations must be made before using the console for the first time. It is not recommended that you modify any prerequisite features after you start using the console.

## Step 1: Verify that your system meets Amazon WorkSpaces Secure Browser required features
<a name="workspaces-web-prequisites"></a>

For WorkSpaces Thin Client Administrator Console to work properly with Amazon WorkSpaces Secure Browser, your system must meet the following specific requirements. This table lists all of these supported features and their requirements.

| Feature | Requirement |
| --- | --- |
| Clipboard | Disable |
| File transfer | Disable |
| Print to local device | Disable |

**Note**
The WorkSpaces Secure Browser extension for single sign-on is not currently supported on WorkSpaces Thin Client.

## Step 2: Set up WorkSpaces Secure Browser portals
<a name="setting-up-WorkSpaces-web-portals"></a>

WorkSpaces Thin Client works with the WorkSpaces Secure Browser VPC in a specific configuration:

1. Create a [VPC](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-vpc.html) using the [AWS CodeBuild Cloudformation template](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudformation-vpc-template.html).

1. Set up your [Identity Provider](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/setup-saml.html).

1. [Create](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-web-portal.html) an Amazon WorkSpaces Secure Browser portal.

1. [Test](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/test-web-portal.html) your new Amazon WorkSpaces Secure Browser portal.
