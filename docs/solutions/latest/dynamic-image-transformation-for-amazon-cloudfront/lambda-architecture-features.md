---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/lambda-architecture-features.html
---

# Lambda architecture features
<a name="lambda-architecture-features"></a>

 **Demo UI**

This solution optionally deploys a demo UI into your account to demonstrate the basic features of the solution. You can use the UI to interact directly with your new image handler API endpoint, using image files that already exist in your account.

This solution’s template contains a Deploy Demo UI parameter that’s activated (set to Yes) by default. If activated, this option deploys an additional Amazon S3 bucket and associated CloudFront distribution into your account.

 **Smart cropping**

You can use this image request option to crop images using the facial recognition capabilities of Amazon Rekognition. To generate a cropped image, a Lambda function sends requests to Amazon Rekognition to identify faces in images and calculate crop areas.

**Note**
Amazon Rekognition supports only JPEG and PNG file formats for smart cropping. When using the Amazon Rekognition features with an image that isn’t JPEG or PNG, the solution automatically converts the image to PNG for use with Amazon Rekognition, then converts it back to the original format.

 **Content moderation**

You can use this image request option to detect and blur inappropriate images. To detect an inappropriate image, a Lambda function sends requests to Amazon Rekognition to identify inappropriate content.

**Note**
Amazon Rekognition supports only JPEG and PNG file formats for content moderation. When using the Amazon Rekognition features with an image that isn’t JPEG or PNG, the solution automatically converts the image to PNG for use with Amazon Rekognition, then converts it back to the original format.

<a name="cross-origin-resource-sharing"></a> **Cross-origin resource sharing**

This solution’s template contains two parameters that activate Cross-origin resource sharing (CORS) for your image handler API: CorsEnabledParameter and CorsOriginParameter. CORS defines how client web applications loaded in one domain can interact with resources in a different domain. You can activate CORS for your image handler API to make requests to your image handler API from outside the domain space of the API.

For example, if you have a public web application hosted on either a custom domain or a cloud domain outside of AWS, you can activate CORS to fetch original or modified images from the image handler API.

**Note**
If you want to change your CORS configuration after deployment, you can activate or deactivate CORS by editing the CORS\_ENABLED (Yes/No) and CORS\_ORIGIN environment variables of the Lambda image handler function. See Using AWS Lambda environment variables in the AWS Lambda Developer Guide for more information.

<a name="image-url-signature"></a> **Image URL signature**

This solution’s template contains three parameters that are required for the image URL signature functionality: EnableSignatureParameter, SecretsManagerSecretParameter, and SecretsManagerKeyParameter. To activate this feature:
+ Set the EnableSignatureParameter parameter to Yes
+ Set the SecretsManagerSecretParameter and SecretsManagerKeyParameter parameters to a valid secret and key that you originally created in Secrets Manager

**Important**
You are responsible for creating the Secrets Manager secret and key. For more information about Secrets Manager secret creation, refer to [Create and manage secrets with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in the AWS Secrets Manager User Guide.

When you activate this feature, the image handler AWS Lambda function checks for a valid signature in the image request. If the signature doesn’t match, the solution returns an error message. When activating the image URL signature, you must provide the signature query string to your URL. For example, you can create the signature using the following Node.js code:

**Note**
If you are using query parameter based edits, the query parameters must be sorted prior to signature generation.

```
const secret = '<YOUR_SECRET_VALUE_IN_SECRETS_MANAGER>';
const path = '/<YOUR_PATH>'; // Add the first '/' to path.
const query_params = '?<YOUR_QUERY_PARAMS>'
const sorted_query_params = query_params.slice(1).split("&").sort().join("&")
const signature = crypto.createHmac('sha256', secret).update(path+(sorted_query_params ? `?${sorted_query_params}` : '')).digest('hex');
```

You can request your image using the image URL signature:

```
https://<distributionName>.cloudfront.net/<YOUR_PATH>?query_param2=val2&query_param_1=val1&signature=<YOUR_SIGNATURE>
```

**Note**
If you update your existing solution deployment and activate the image URL signature, the updated stack will no longer be compatible with the existing URLs. You must update your application to provide the correct signature query string to your URLs. To update the solution stack, refer to Update the solution.

**Note**
If you plan to use the Expires query parameter alongside signed requests, ensure you include the expiration when creating your signature. For more information, refer to Include request expiration.

<a name="default-fallback-image"></a> **Default fallback image**

This solution provides a default fallback image feature that returns the specified fallback image when errors occur during processing, rather than a JSON object error message. This solution’s template contains three parameters that are required for the default fallback image feature: EnableDefaultFallbackImageParameter, FallbackImageS3BucketParameter, and FallbackImageS3KeyParameters.

By default, this feature is deactivated. To activate this feature:
+ Set the EnableDefaultFallbackImageParameter parameter to Yes
+ Set the FallbackImageS3BucketParameter and FallbackImageS3KeyParameter parameters to a valid S3 bucket and object key

**Note**
Before activating this feature, if you use an S3 bucket policy in the fallback image S3 bucket, you must edit the bucket policy to allow the CustomResourceFunction and ImageHandlerFunction AWS Lambda functions to get the default fallback image object. For more information, see Adding a bucket policy by using the Amazon S3 console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
