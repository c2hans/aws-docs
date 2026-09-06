---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/source-code-location.html
---

# Source code location
<a name="source-code-location"></a>

In a default Landing Zone Accelerator on AWS deployment, CodePipeline retrieves the source code from the [solution’s GitHub repository](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main). You may want to instead store the source code in Amazon S3 to use only Amazon-provided products. This solution supports this operating model by uploading the LZA source code to an existing S3 bucket before deploying the solution.

Follow these instructions to implement this pattern:

1. Create an S3 bucket with [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) enabled. This bucket should be created in the same AWS account and region you plan to deploy the Landing Zone Accelerator on AWS solution.

1. Clone or download the latest release of the Landing Zone Accelerator on AWS [source code](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/source).

1. Navigate to the landing-zone-accelerator-on-aws folder:

   ```
   cd landing-zone-accelerator-on-aws
   ```

1. Compress all files and folders inside the landing-zone-accelerator-on-aws folder into a versioned zip archive file and upload it to your S3 bucket:

   ```
   SOURCE_CODE_BUCKET_NAME=YOUR_BUCKET_NAME
   LZA_VERSION=v1.14.2
   zip -q -T -r ../$LZA_VERSION.zip .  # quiet, test integrity, recursive
   aws s3 cp ../$LZA_VERSION.zip s3://$SOURCE_CODE_BUCKET_NAME/release/$LZA_VERSION.zip
   ```
**Note**
Replace `v1.14.2` with the actual LZA version you are deploying. The zip file must contain all the contents inside the landing-zone-accelerator-on-aws folder or the build will fail.

1. Install dependencies and build the source code:

   ```
   yarn install && yarn build
   ```

1. Navigate to the installer folder:

   ```
   cd packages/\@aws-accelerator/installer/
   ```

1. Synthesize the installer template by running:

   ```
   cdk synth --context use-s3-source=true
   ```

**Note**
If your S3 bucket is encrypted with KMS (S3-KMS), you must pass the KMS key ID when synthesizing the template:

```
cdk synth --context use-s3-source=true --context
s3-source-kms-key-arn=arn:aws:kms:us-east-1:000000000000:key/aaaaaaaa-1111-bbbb-2222-cccccc333333
```

1. Retrieve the synthesize template named `AWSAccelerator- InstallerStack.template.json` from the cdk.out directory.

1. Use this template to create the `AWSAccelerator-Installer` CloudFormation stack in the account and region the S3 bucket was created in.

1. The deployment now follows the same process as the [standard deployment process](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deployment-overview.html) with the addition of the following parameters:
   +  **RepositoryBucketName** - The name of the S3 bucket used to contain the source code.
   +  **RepositoryBucketObject** - The S3 object key of the source code uploaded in Step 5.
   +  **RepositoryBucketKmsKeyArn** - (OPTIONAL) The ARN of the KMS key used to encrypt the S3 bucket.
