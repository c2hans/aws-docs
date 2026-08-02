---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/log-in-to-workload-discovery-on-aws.html
---

# Log in to Workload Discovery on AWS
<a name="log-in-to-workload-discovery-on-aws"></a>

After the solution successfully deploys, determine the URL for the [Amazon CloudFront distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html) that serves the solution’s web UI.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose **View nested** to display the nested stacks that make up the deployment. Depending on your preferences, nested stacks might already be displayed.

1. Select the main Workload Discovery on AWS stack.

1. Select the **Outputs** tab and choose the URL in the **Value** column associated with the **WebUiUrl** key.

1. On the **Sign in to** screen, enter the sign-in credentials that you received via email. Then take the following actions:

   1. Follow the prompts to change your password.

   1. Use the verification code sent to your email to complete account recovery.
