---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/step-2-launch-the-orgmanagement-stack.html
---

# Step 2: Deploy the Org-Management stack
<a name="step-2-launch-the-orgmanagement-stack"></a>

Deploy the Org-Management stack to the AWS Organizations management account.

1. Review the changes that AWS CDK deploys.

   ```
   $ npm run cdk -- diff account-assessment-for-aws-organizations-org-management \
       --profile "${PROFILE_ORG_MGMT}" \
       --no-change-set
   ```

1. Deploy the stack.

   ```
   $ npm run deployOrgMgmt -- \
       --parameters DeploymentNamespace="${DEPLOYMENT_NAMESPACE}" \
       --parameters HubAccountId="${HUB_ACCOUNT_ID}" \
       --profile "${PROFILE_ORG_MGMT}"
   ```

1. Review the IAM changes when prompted, and confirm the deployment.

1. Wait for the stack to reach `CREATE_COMPLETE` or `UPDATE_COMPLETE`.
