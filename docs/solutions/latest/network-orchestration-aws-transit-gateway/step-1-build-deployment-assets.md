---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-1-build-deployment-assets.html
---

# Step 1: Build deployment assets
<a name="step-1-build-deployment-assets"></a>

Before you launch the stacks, build the CloudFormation templates and Lambda source code from the source code repository. Then stage the Lambda assets in an Amazon S3 bucket in your account. Perform these steps once, from a machine that has the AWS CLI, Git, Node.js, and Poetry installed.

**Note**
The repository’s `deployment/` templates aren’t ready to deploy as-is. These build steps prepare them. For the full explanation, see [AWS CloudFormation templates](aws-cloudformation-templates.md).

1. Create an S3 bucket in the AWS Region where you plan to deploy. The bucket name must end with the Region name. For example, to deploy in the US East (N. Virginia) Region (`us-east-1`), create a bucket named ` {{my-bucket}}-us-east-1`. The build appends `-{{<region>}} ` to the base name you provide in the next steps.
**Note**
If you deploy spoke stacks into more than one AWS Region, create a source bucket in each of those Regions. Each stack loads its assets from `<BUCKET_BASE_NAME>-<region>` in the Region where you deploy it. That bucket must exist in the Region, with the built assets uploaded.

1. Clone the Guidance source code repository:

   ```
   git clone https://github.com/aws-solutions-library-samples/network-orchestration-for-aws-transit-gateway.git
   ```

1. Change to the `deployment` directory and make the build script executable:

   ```
   cd network-orchestration-for-aws-transit-gateway/deployment
   chmod +x ./build-s3-dist.sh
   ```

1. Run the build script. It requires four arguments:

   ```
   ./build-s3-dist.sh <BUCKET_BASE_NAME> network-orchestration-for-aws-transit-gateway <VERSION> <BUCKET_BASE_NAME>
   ```

<table>
<thead>
  <tr><th>Argument</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <code>&lt;BUCKET_BASE_NAME&gt;</code> (first)</td><td>The base name of the bucket you created, <b>without</b> the <code>-&lt;region&gt;</code> suffix. The build stages the Lambda source code under this bucket.</td></tr>
  <tr><td> <code>network-orchestration-for-aws-transit-gateway</code> (second)</td><td>The Guidance name. Enter this value exactly as shown.</td></tr>
  <tr><td> <code>&lt;VERSION&gt;</code> (third)</td><td>The version to build. Use the latest release tag from the repository’s <a href="https://github.com/aws-solutions-library-samples/network-orchestration-for-aws-transit-gateway/releases">Releases</a> page (for example, <code>v3.3.26</code>).</td></tr>
  <tr><td> <code>&lt;BUCKET_BASE_NAME&gt;</code> (fourth)</td><td>The template output bucket. Use the same bucket base name as the first argument.</td></tr>
</tbody>
</table>

**Note**
Use the same bucket base name for the first and fourth arguments. This deployment uses only the source (regional) bucket — it hosts the Lambda code. Upload the CloudFormation templates directly in the CloudFormation console in the following steps.

   For example:

   ```
   ./build-s3-dist.sh notg-guidance network-orchestration-for-aws-transit-gateway v3.3.28 notg-guidance
   ```

1. Upload the generated Lambda source assets to your bucket, using the same version value you passed to the build script:

   ```
   aws s3 cp ./regional-s3-assets/ s3://<BUCKET_BASE_NAME>-<region>/network-orchestration-for-aws-transit-gateway/<VERSION>/ --recursive
   ```

   For example:

   ```
   aws s3 cp ./regional-s3-assets/ s3://notg-guidance-us-east-1/network-orchestration-for-aws-transit-gateway/v3.3.28/ --recursive
   ```

   The `regional-s3-assets/` directory includes the Lambda code, the web console, and the AWS AppSync GraphQL assets. During deployment, the hub stack’s ConsoleDeploy custom resource copies the console and GraphQL assets from this same bucket.

1. Grant every account that you deploy this Guidance into (the hub account, each spoke account, and — if you use AWS Organizations — the management account) read access to the staged source code. Attach the following bucket policy to your S3 bucket. Replace the placeholders with your bucket name, Region, and the account IDs you deploy into.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowNetworkOrchestrationAccountsToReadSourceCode",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::<HUB_ACCOUNT_ID>:root",
                       "arn:aws:iam::<SPOKE_ACCOUNT_ID>:root",
                       "arn:aws:iam::<ORG_MANAGEMENT_ACCOUNT_ID>:root"
                   ]
               },
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::<BUCKET_BASE_NAME>-<region>/network-orchestration-for-aws-transit-gateway/*"
           }
       ]
   }
   ```
**Note**
List every account that you deploy a hub, spoke, or organization-role stack into. Because the policy grants access only to named accounts (not to everyone), you can keep Amazon S3 Block Public Access enabled on the bucket. If you deploy into many accounts in an organization, you can scope access with the `aws:PrincipalOrgID` condition key instead. If you do, review your S3 Block Public Access settings. AWS might treat a policy that uses a wildcard principal as public.

1. The build also generates the four CloudFormation templates in the `./global-s3-assets/` directory:
   +  `network-orchestration-hub.template`
   +  `network-orchestration-spoke.template`
   +  `network-orchestration-organization-role.template`
   +  `network-orchestration-hub-service-linked-roles.template`

     You upload these template files directly in the CloudFormation console in the following steps.
