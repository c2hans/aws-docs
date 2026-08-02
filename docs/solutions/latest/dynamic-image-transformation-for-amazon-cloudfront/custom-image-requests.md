---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/custom-image-requests.html
---

# Custom image requests
<a name="custom-image-requests"></a>

**Note**
As of recent releases of Dynamic Image Transformation for Amazon CloudFront, editing the environment variables directly is not supported for the AutoWebP (v7.0.0), SourceBuckets (v6.2.6), OriginShieldRegion(v7.0.0) and EnableS3ObjectLambda(v7.0.0) template parameters, instead, follow the instructions in [Updating template parameters](updating-template-parameters.md).

You can customize most settings for this solution by editing and updating the environment variables associated with the image handler Lambda function. You can find the image handler function in the AWS Management Console using one of the following methods:

 **Using the AWS Lambda console:**

1. Sign in to the [AWS Lambda console](https://console.aws.amazon.com/lambda).

1. Select **Functions**. The image handler function is listed with the following naming convention: `[.replaceable]<StackName>`-ImageHandlerFunction-`[.replaceable]<UniqueID>`.

 **Using the AWS CloudFormation console:**

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose the **Resources** tab. The image handler function is listed with a **Logical ID** of `ImageHandlerFunction`.

After opening the Lambda function, go to the **Environment variables** section. Use the following key-value pairs to customize the solutions settings.

 **Note:** The solution uses the  to determine these initial key values, except for **REWRITE\_MATCH\_PATTERN** and **REWRITE\_SUBSTITUTION**.

| Variable Key | Value Type | Description |
| --- | --- | --- |
|  **AUTO\_WEPB**  |  `Yes/No`  | Choose whether to automatically accept webp image formats. |
|  **CORS\_ENABLED**  |  `Yes/No`  | Indicates whether to return an **Access-Control-Allow-Origin** header with the image handler API response. |
|  **CORS\_ORIGIN**  |  `String`  | This value is returned by the API in the **Access-Control-Allow-Origin** header. An asterisk value supports any origin. We recommend specifying a specific origin (Ex: `https://example.domain`) to restrict cross-site access to your API.<br /> **Note:** This value is ignored if **CORS\_ENABLED** is set to `No`. |
|  **ENABLE\_DEFAULT\_FALLBACK\_IMAGE**  |  `Yes/No`  | Choose whether to return the default fallback image when errors occur. |
|  **DEFAULT\_FALLBACK\_IMAGE\_BUCKET**  |  `String`  | Specifies the S3 bucket which contains the default fallback image.<br /> **Note:** This value is ignored if the **ENABLE\_DEFAULT\_FALLBACK\_IMAGE** parameter is set to `No`. |
|  **DEFAULT\_FALLBACK\_IMAGE\_KEY**  |  `String`  | Defines the default fallback image S3 object key, including the prefix.<br /> **Note:** This value is ignored if the **ENABLE\_DEFAULT\_FALLBACK\_IMAGE** parameter is set to `No`. |
|  **ENABLE\_SIGNATURE**  |  `Yes/No`  | Choose whether to use the image URL signature. |
|  **REWRITE\_MATCH\_PATTERN**  |  `Regex`  | By default, this parameter is empty. If you overwrite this default value, use a JavaScript-compatible regular expression for matching custom image requests using the rewrite function. This value should match the JavaScript compatible regular expression. For example, `/(filters-)/gm`. |
|  **REWRITE\_SUBSTITUTION**  |  `String`  | By default, this parameter is empty. If you overwrite this default value, use a substitution string for custom image requests using the rewrite function. For example, `filters:`. |
|  **SECRETS\_MANAGER**  |  `String`  | Defines the Secrets Manager secret that contains the secret key for the image URL signature.<br /> **Note:** This value is ignored if `[.replaceable]ENABLE_SIGNATURE` is set to `No`. |
|  **SECRET\_KEY**  |  `String`  | Defines the Secrets Manager secret key that contains the secret value to create the image URL signature.<br /> **Note:** This value is ignored if **ENABLE\_SIGNATURE** is set to `No`. |
|  **SOURCE\_BUCKETS**  |  `String`  | The S3 bucket (or buckets) in your account that contain(s) the original images. If you’re providing multiple buckets, separate them by commas. |
