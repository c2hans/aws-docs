---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/step-3-launch-the-spoke-stack.html
---

# Step 3: Deploy the Spoke stack
<a name="step-3-launch-the-spoke-stack"></a>

Deploy the Spoke stack to every account that the guidance assesses, including the Hub account if you want to assess it.

1. Review the changes that AWS CDK deploys.

   ```
   $ npm run cdk -- diff account-assessment-for-aws-organizations-spoke \
       --profile "${PROFILE_SPOKE}" \
       --no-change-set
   ```

1. Deploy the stack.

   ```
   $ npm run deploySpoke -- \
       --parameters DeploymentNamespace="${DEPLOYMENT_NAMESPACE}" \
       --parameters HubAccountId="${HUB_ACCOUNT_ID}" \
       --profile "${PROFILE_SPOKE}"
   ```

1. Review the IAM changes when prompted, and confirm the deployment.

1. Wait for the stack to reach `CREATE_COMPLETE` or `UPDATE_COMPLETE`.

Repeat these steps with the AWS CLI profile for each Spoke account.

To assess the Hub account, repeat the Spoke deployment with `PROFILE_SPOKE` set to the Hub account profile.
