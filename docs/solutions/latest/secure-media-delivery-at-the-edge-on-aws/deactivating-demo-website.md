---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/deactivating-demo-website.html
---

# Deactivating demo website
<a name="deactivating-demo-website"></a>

 **By redeploying CDK stack**

 If you deployed the solution through CDK, you can simply deactivate the demo website and its related components by modifying the configuration file with the parameters that determine what solution components are deployed.

1.  Navigate to the CDK project folder you used to configure and launch the solution in your account.

1.  Edit `solution.context.json` document and within **api** property change the **demo** value to `false` and save:

   ```
   {
    "main": {
    ...
    },
    "api": {
      "language": "nodejs",
      "demo": false
    }
    ...
   }
   ```

1.  Redeploy CDK stack.

   ```
   npx cdk deploy [stack_name]
   ```

 **By deactivating CloudFront distribution**

 If you deployed this solution using the CloudFormation template, the demo website will be automatically published with the assets stored in a dedicated S3 bucket delivered through CloudFront. You can shut down the website by simply deactivating the CloudFront distribution which is the only entry point for the website as the S3 bucket is private.

1.  In AWS Management Console, navigate to the CloudFront page.

1.  From the list of all the CloudFront distributions associated with your account, select the one that was created with the solution stack with the description that matches with **[Stack Name]-Demo website Secure Media Delivery,** and choose **Disable**.

1. After few minutes, the **status** of the distribution changes from `Enabled` to `Disabled` making it effectively unreachable.
