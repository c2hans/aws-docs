---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/step-1-build-deployment-assets.html
---

# Step 1: Build deployment assets
<a name="step-1-build-deployment-assets"></a>

Follow step-by-step instructions to build deployment assets.

1.  Create an S3 bucket with the bucket appended with the region in which the deployment is to be made. example, if the deployment is to be made in **us-east-1** create a bucket name as `[BUCKET_NAME]-us-east-1`.

1.  Clone the git repo

   ```
    git clone <repo-url>
   ```

1.  Prepare build file

   ```
    cd <rootDir>/deployment
   chmod +x ./build-s3-dist.sh
   ```

1.  Build and package deployment assets, replace `[S3_BUCKET]` with name of bucket created in previous step, replace `[VERSION_ID]` with current version of sample code ( 1.1.3 as of July, 2025 )

   ```
    ./build-s3-dist.sh [S3_BUCKET] centralized-network-inspection [VERSION_ID]
   ```

1.  Copy assets from `./deployment/regional-s3-assets/*` to s3 bucket `s3://[S3_BUCKET]-[REGION]/centralized-network-inspection/[VERSION_ID]/`

1.  Copy assets from `./deployment/regional-s3-assets/*` to s3 bucket `s3://[S3_BUCKET]-[REGION]/centralized-network-inspection/latest/`

1.  use the file `./deployment/global-s3-assets/centralized-network-inspection-on-aws.template` to create CloudFormation stack in next step.
