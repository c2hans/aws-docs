---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/step-1-launch-the-hub-stack.html
---

# Step 1: Deploy the Hub stack
<a name="step-1-launch-the-hub-stack"></a>

Deploy the Hub stack to the member account that you selected as the Hub account.

1. Review the changes that AWS CDK deploys.

   ```
   $ npm run cdk -- diff account-assessment-for-aws-organizations-hub \
       --profile "${PROFILE_HUB}" \
       --no-change-set
   ```

1. Deploy the stack.

   ```
   $ npm run deploy -- \
       --parameters DeploymentNamespace="${DEPLOYMENT_NAMESPACE}" \
       --parameters UserEmail="${USER_EMAIL}" \
       --parameters AllowListedIPRanges="${ALLOW_LISTED_IP_RANGES}" \
       --parameters OrganizationID="${ORGANIZATION_ID}" \
       --parameters ManagementAccountId="${MANAGEMENT_ACCOUNT_ID}" \
       --profile "${PROFILE_HUB}"
   ```

1. Review the IAM changes when prompted, and confirm the deployment.

1. Wait for the stack to reach `CREATE_COMPLETE` or `UPDATE_COMPLETE`.

The default DynamoDB item lifetime is 90 days, and the default Amazon Cognito multi-factor authentication setting is `OPTIONAL`. To override these values, add the `DynamoTimeToLive` or `MultiFactorAuthentication` parameter when you run the deploy command.

**Custom-resource Lambda functions**
In addition to its primary Lambda functions, this guidance includes custom-resource Lambda functions that configure the Amazon Cognito domain and deploy the web UI. These functions run when the Hub stack is created, updated, or deleted. Do not delete them because they manage associated resources.
