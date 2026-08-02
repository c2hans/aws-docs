---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/update-the-stack.html
---

# Update the solution
<a name="update-the-stack"></a>

If you have previously deployed the solution, follow this procedure to update the Cloud Migration Factory on AWS solution CloudFormation stack to get the latest version of the solution’s framework.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your existing Cloud Migration Factory on AWS solution CloudFormation stack, and select **Update**.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link for the [latest template](aws-cloudformation-templates.md).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Launch the stack](launch-the-stack.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template might create AWS Identity and Access Management (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **UPDATE\_COMPLETE** status in approximately 10 minutes.

## Redeploy the API Gateway APIs
<a name="redeploy-api-gateway-apis"></a>

After updating the stack, it is required that you redeploy the API Gateway APIs: admin, login, tools, and user. This ensures that any changes to the configuration are available to all APIs.

1. Sign in to the [Amazon API Gateway console](https://console.aws.amazon.com/apigateway) , select \*APIs \*from the left navigation, and then select the CMF API.

1. From the API Resources, select **Actions**, and select **Deploy API**.

1. Select **Deployment Stage \*of \*prod**, and choose **Deploy**.

1. Repeat steps 1-3 for each of the Cloud Migration Factory on AWS APIs.

**Note**
Updating the solution adds the current versions of the built-in scripts to the deployment, but it won’t set the default versions of the scripts to the latest version. The reason is that we don’t want to overwrite any customizations that might have been applied to the solution.

## Use the latest versions of the scripts
<a name="use-latest-scripts"></a>

To use the latest versions of the scripts:

1. Navigate to the Cloud Migration Factory on AWS console.

1. In the navigation menu, select **Automation,** then select **Scripts**.

1. Goto the Cloud Migration Factory on AWS console.

1. Select **Automation**, then **Scripts**.

1. Select the existing script that you want to update to the latest version. Then select **Actions** and choose \*Change default version. \*

1. For **Script Default Version**, choose the latest version of the script.

1. Choose **Save**.

## Update customized scripts
<a name="update-customized-scripts"></a>

To update scripts that have been customized:

1. Download the updated scripts from the following [repository](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/v3.3.3/default_scripts.zip).

1. Extract the contents to see the individual scripts.

1. From one of the new scripts extract the `mfcommon.py` file.

1. Goto the Cloud Migration Factory on AWS console.

1. Select **Automation**, then **Scripts**.

1. Select the existing script to update, and then select **Actions** and choose \*Download default version. \*

1. Extract the contents of the script archive.

1. Replace the `mfcommon.py` file with the version extracted in Step 3.

1. Compress all the contents of the script, with the new `mfcommon.py` file.

1. Upload this new version, following the instructions in the [Add new version of a script package](scripts-management.md#add-new-version-of-a-script-package) section.

   On the **Automation Scripts** page, for each script you want the latest version to be the default:

   1. Select the script.

   1. From **Actions**, choose **Change default version**.

   1. From **Script Default Version**, choose the latest available version number.

1. Choose **Save**.

## (Private deployment only) Redeploy private web console static content
<a name="redeploy-private-content"></a>

To redeploy private web console static content, complete the steps documented in [Deploy private web console static content](deploy-private-web-console.md) section.
