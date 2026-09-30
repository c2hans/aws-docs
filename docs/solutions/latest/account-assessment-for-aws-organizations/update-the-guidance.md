---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/update-the-guidance.html
---

# Update the guidance
<a name="update-the-guidance"></a>

## Update AWS CDK deployments
<a name="update-aws-cdk-deployments"></a>

Use the AWS CDK application in the [GitHub repository](https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations) to update the guidance.

1. Back up any guidance data that you must retain.

1. In your local repository, fetch the release that you want to deploy.

   ```
   $ git fetch --tags
   $ git checkout <VERSION>
   ```

1. Reapply any source-code customizations, including the anonymized operational metrics opt-out setting, to the new version.

1. Set the same Region, AWS CLI profiles, deployment namespace, staging bucket name, and stack parameters that you used for the existing deployment. Set `SOLUTION_VERSION` to the version that you checked out.

1. From the `deployment` directory, rebuild the application.

   ```
   $ ./build-s3-dist.sh \
       "${DIST_OUTPUT_BUCKET}" \
       "${SOLUTION_VERSION}"
   ```

1. Upload the rebuilt assets to the versioned path in the existing Regional staging bucket.

   ```
   $ aws s3 cp regional-s3-assets/webui/ \
       "s3://${ASSET_BUCKET_NAME}/${SOLUTION_TRADEMARKEDNAME}/${SOLUTION_VERSION}/webui/" \
       --recursive \
       --profile "${PROFILE_HUB}"
   ```

1. Change to the `source/infra` directory (`cd ../source/infra`) and run `npm ci`.

1. Run `cdk diff` for the Hub, Org-Management, and Spoke stacks. Review the proposed resource and IAM changes before continuing.

1. Follow the deployment instructions to update the [Hub stack](step-1-launch-the-hub-stack.md), the [Org-Management stack](step-2-launch-the-orgmanagement-stack.md), and each [Spoke stack](step-3-launch-the-spoke-stack.md).

1. Wait for each stack to reach `UPDATE_COMPLETE`.

You do not need to bootstrap an account and Region again unless the AWS CDK bootstrap resources are missing or the new release requires a newer bootstrap version. For the initial environment setup and variable definitions, see [Prepare the deployment](prepare-the-deployment.md).

## Update from version 1.0.x
<a name="update-from-version-1-0"></a>

From version v1.1.0 on, we improved the generation of the Cognito UserPool name and the AppRegistry application name to make it less likely that your deployment fails due to a name conflict. As these changes are not backwards compatible, it is not possible to update the v1.0.x Hub stack to v1.1.x in place.

If you have v1.0.x installed in your account, and you want to start using v1.1.x, take the following steps:
+ Delete the AWS CDK stacks of your v1.0.x installation.
+ Before deleting the UserPool, check if there are any users (except from the default user created at deployment time) that you need to re-create in the new UserPool. Note their email addresses if needed.
+ Delete the UserPool, S3 buckets and DynamoDB tables of your v1.0.x installation. As your scan data are stale, you do not need to migrate any data to the new guidance version. You will be able to run a fresh scan after installing the new guidance version. See [uninstall instructions](uninstall-the-guidance.md) for details.
+ Choose a new deployment namespace and install v1.1.x freshly in your accounts, following the [deployment instructions](deploy-the-guidance.md#deployment-process-overview) in this guide.
