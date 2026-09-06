---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-2/ug/S3-buckets-prereqs.html
---

# Amazon S3 bucket prerequisites for isolated VPC deployments
<a name="S3-buckets-prereqs"></a>

If you're deploying Research and Engineering Studio in an isolated VPC, follow these steps to update the lambda configuration parameters after you deploy RES in your AWS account.

1. Log into the Lambda Console of the AWS account where Research and Engineering Studio is deployed.

1. Find and navigate to the Lambda function named `{{<RES-EnvironmentName>}}-vdc-custom-credential-broker-lambda`.

1. Select the **Configuration** tab of the function.
![isolated VPC environment variable](http://docs.aws.amazon.com/res/archive/release-minus-2/ug/images/Isolated-VPC-Env-Variable.png)

1. On the left hand side, choose **Environment variables** to view that section.

1. Choose **Edit** and add the following new environment variable to the function:
   + Key: `AWS_STS_REGIONAL_ENDPOINTS`
   + Value: `regional`

1. Choose **Save**.
