---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/prepare-the-deployment.html
---

# Prepare the deployment
<a name="prepare-the-deployment"></a>

1. Clone the repository and change to its root directory.

   ```
   $ git clone https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations.git
   $ cd account-assessment-for-aws-organizations
   ```

1. Set the deployment values. Use a globally unique value for `DIST_OUTPUT_BUCKET`. Do not include the Region suffix in this value.

   ```
   $ export AWS_REGION=<REGION>
   $ export PROFILE_HUB=<HUB_PROFILE>
   $ export PROFILE_ORG_MGMT=<ORG_MGMT_PROFILE>
   $ export PROFILE_SPOKE=<SPOKE_PROFILE>
   $ export HUB_ACCOUNT_ID=<HUB_ACCOUNT_ID>
   $ export MANAGEMENT_ACCOUNT_ID=<MANAGEMENT_ACCOUNT_ID>
   $ export SPOKE_ACCOUNT_ID=<SPOKE_ACCOUNT_ID>
   $ export DIST_OUTPUT_BUCKET=<UNIQUE_BUCKET_BASE_NAME>
   $ export SOLUTION_ID=SO0217
   $ export SOLUTION_NAME="Account Assessment for AWS Organizations"
   $ export SOLUTION_TRADEMARKEDNAME=account-assessment-for-aws-organizations
   $ export SOLUTION_VERSION=<VERSION>
   $ export ASSET_BUCKET_NAME="${DIST_OUTPUT_BUCKET}-${AWS_REGION}"
   $ export DEPLOYMENT_NAMESPACE=<NAMESPACE>
   $ export USER_EMAIL=<EMAIL_ADDRESS>
   $ export ALLOW_LISTED_IP_RANGES=<COMMA_SEPARATED_CIDR_RANGES>
   $ export ORGANIZATION_ID=<ORGANIZATION_ID>
   ```

   Include the leading `v` in the guidance version, for example, `v1.1.0`. The deployment namespace must contain 3 to 10 lowercase letters, numbers, or hyphens. It cannot begin or end with a hyphen. Use the same value for all three stacks.

1. Create the Regional staging bucket in the Hub account.

   ```
   $ aws s3 mb "s3://${ASSET_BUCKET_NAME}" \
       --region "${AWS_REGION}" \
       --profile "${PROFILE_HUB}"
   ```

1. Build the Lambda package, web UI, and AWS CDK application.

   ```
   $ cd deployment
   $ chmod +x build-s3-dist.sh build-lambdas.sh
   $ ./build-s3-dist.sh \
       "${DIST_OUTPUT_BUCKET}" \
       "${SOLUTION_VERSION}"
   $ cd ..
   ```

1. Upload the web UI assets to the Regional staging bucket.

   ```
   $ aws s3 cp deployment/regional-s3-assets/webui/ \
       "s3://${ASSET_BUCKET_NAME}/${SOLUTION_TRADEMARKEDNAME}/${SOLUTION_VERSION}/webui/" \
       --recursive \
       --profile "${PROFILE_HUB}"
   ```

1. Install the AWS CDK application dependencies.

   ```
   $ cd source/infra
   $ npm ci
   ```

1. Bootstrap each target environment. You only need to bootstrap each account and Region once.

   ```
   $ npm run cdk -- bootstrap "aws://${HUB_ACCOUNT_ID}/${AWS_REGION}" \
       --profile "${PROFILE_HUB}"
   $ npm run cdk -- bootstrap "aws://${MANAGEMENT_ACCOUNT_ID}/${AWS_REGION}" \
       --profile "${PROFILE_ORG_MGMT}"
   $ npm run cdk -- bootstrap "aws://${SPOKE_ACCOUNT_ID}/${AWS_REGION}" \
       --profile "${PROFILE_SPOKE}"
   ```

If you deploy the Spoke stack to multiple accounts, bootstrap each account before deploying the stack.
