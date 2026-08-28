---
source_url: https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-errors.html
---

# AWS Service Catalog deployment errors
<a name="launch-wizard-sap-service-catalog-errors"></a>

For AWS Service Catalog deployments completed prior to February 7, 2022, perform the following steps to remove the `AmazonLambdaRolePolicyForLaunchWizardSAP` policy from the `AmazonLambdaRoleForLaunchWizard` role, and add a new inline policy. Deployments completed after February 7, 2022 do not require you to perform these steps.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles** from the left navigation pane.

1. Search for the `AmazonLambdaRoleForLaunchWizard`. Select the policy to view the attached permissions.

1. Check whether the `AmazonLambdaRolePolicyForLaunchWizardSAP` policy is attached to this role. If it is attached, remove the policy by selecting the check box next to it, and choose **Remove**.

1. Add the following inline policy by choosing **Add permissions**>**Create inline policy**, and entering the policy in the **JSON** tab of the **Create policy** wizard.

------
#### [ JSON ]

****

   ```
   {
     "Version":"2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "ssm:GetParameter"
         ],
         "Resource": "arn:aws:ssm:*::parameter/LaunchWizard*"
       },
       {
         "Effect": "Allow",
         "Action": [
           "ssm:GetDocument",
           "ssm:sendCommand"
         ],
         "Resource": "arn:aws:ssm:*::document/AWS-RunShellScript"
       },
       {
         "Effect": "Allow",
         "Action": [
           "ssm:SendCommand"
         ],
         "Resource": [
         "arn:aws:ec2:*:{{111122223333}}:instance/*"
         ],
         "Condition": {
           "StringLike": {
             "ssm:resourceTag/LaunchWizardApplicationType": "*"
           }
         }
       }
     ]
   }
   ```

------

1. Choose **Review policy**, enter a name for the policy, and choose **Create policy**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
