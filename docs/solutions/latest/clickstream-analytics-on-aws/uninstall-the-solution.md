---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/uninstall-the-solution.html
---

# Uninstall the guidance
<a name="uninstall-the-solution"></a>

 You will encounter an IAM role missing error if you delete Clickstream Analytics on AWS main stack before you delete the stacks created for Clickstream projects. Clickstream Analytics on AWS console launches additional CloudFormation stacks for the Clickstream pipelines. We recommend you delete projects before uninstalling the guidance.

## Step 1. Delete projects
<a name="step-1.-delete-projects"></a>

1.  Go to the Clickstream Analytics on AWS console.

1.  In the left sidebar, choose **Projects**.

1.  Select the project to be deleted.

1.  Choose the **Delete** button in the upper right corner.

1.  Repeat steps 3 and 4 to delete all your projects.

## Step 2. Delete Clickstream Analytics on AWS stack
<a name="step-2.-delete-clickstream-analytics-on-aws-stack"></a>

1.  Go to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Find the CloudFormation stack of the guidance.

1.  Delete the CloudFormation Stack of the guidance.

1.  (Optional) Delete the S3 bucket created by the guidance.

   1.  Choose the CloudFormation stack of the guidance, and select the **Resources** tab.

   1.  In the search bar, enter DataBucket. It shows all resources with the name DataBucket created by the guidance. You can find the resource type **AWS::S3::Bucket**, and the **Physical ID** field is the S3 bucket name.

   1.  Go to the S3 console, and find the S3 bucket with the bucket name. **Empty** and **Delete** the S3 bucket.
