---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/lambda-parameters.html
---

# Lambda architecture template parameters
<a name="lambda-parameters"></a>

\+

|  **Parameter**  |  **Default**  |  **Description**  |
| --- | --- | --- |
|  **CORS Enabled**  | No | Choose whether to activate CORS. For information about this parameter, refer to . |
|  **CORS Origin**  |  `*`  | This value is returned by the API in the **Access-Control-Allow-Origin** header. An asterisk value supports any origin. We recommend specifying a specific origin (Ex: http://example.domain) to restrict cross-site access to your API.<br /> **Note:** This value is ignored if **CORS\_ENABLED** is set to `No`. |
|  **Source Buckets**  | <Requires input> | Specifies the S3 bucket (or buckets) in your account that contain(s) the images that you manipulate. To specify multiple buckets, separate them by commas. |
|  **Enable S3 Object Lambda (Deprecated)**  |  `No`  | This option has been deprecated. Amazon S3 Object Lambda will no longer be open to new customers starting on November 7, 2025. If you were not an existing user of S3 Object Lambda before November 7, 2025, select 'No'. For more information, please visit https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html.<br />Determines which component to use to use as the CloudFront distribution origin. No uses API gateway, Yes uses an S3 Object Lambda Access Point, which supports images larger than the existing 6 MB size limit. Only the origin in use will be created by the template. |
|  **Deploy Demo UI**  | Yes | The demo UI that deploys to the `Demo` S3 bucket. For more information refer to [Use the demo UI](use-the-demo-ui.md). |
|  **Log Retention Period**  | 180 | Specifies the number of days to retain Lambda log data in CloudWatch logs. |
|  **Enable Signature**  | No | Choose whether to activate the image URL signature feature. For information about this feature, refer to . |
|  **SecretsManager Secret**  |  *<Optional input>*  | Define the Secrets Manager secret name that contains the secret key for the image URL signature.<br /> **Note:** This value is ignored if the **Enable Signature** parameter is set to `No`. |
|  **SecretsManager Key**  |  *<Optional input>*  | Define the Secrets Manager secret key that contains the secret value to create the image URL signature.<br /> **Note:** This value is ignored if the **Enable Signature** parameter is set to `No`. |
|  **Enable Default Fallback Image**  | No | Choose whether to activate the default fallback image feature. For information about this feature, refer to . |
|  **Fallback Image S3 Bucket**  |  *<Optional input>*  | Specify the S3 bucket which contains the default fallback image.<br /> **Note:** This value is ignored if the **Enable Default Fallback Image** parameter is set to `No`. |
|  **Fallback Image S3 Key**  |  *<Optional input>*  | Specify the default fallback image S3 object key, including prefix. See [Creating object key names](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) for more information.<br /> **Note:** This value is ignored if the **Enable Default Fallback Image** parameter is set to `No`. |
|  **AutoWebP**  |  `No`  | Choose whether to automatically convert responses to the [WebP](https://developers.google.com/speed/webp) image formats if the Accept request header allows it. |
|  **Origin Shield Region**  |  `Disabled`  | The Region to set up the Origin Shield caching layer for the CloudFront distribution. May result in a better cache hit ratio, as well as lower latency on repeat requests in new regions. For more information on choosing an Origin Shield region, see the [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html). |
|  **CloudFront PriceClass**  | PriceClass\_All | The CloudFront price class to use. For more information, refer to [Choosing the price class for a CloudFront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html) in the *Amazon CloudFront Developer Guide*. |
|  **Use Existing CloudFront Distribution**  |  `No`  | Choose whether to deploy the solution in a way that it can be attached to an existing CloudFront distribution. If `No` is selected, a CloudFront distribution will be created for you. If you have selected `Yes`, manual action will need to be performed to finish the attachment, refer to [Attaching an Existing CloudFront distribution](attaching-existing-distribution.md) for more information. |
|  **Existing CloudFront Distribution ID**  |  `<Optional Input>`  | The Distribution ID for the existing CloudFront distribution being attached to. This field is required if Use Existing CloudFront Distribution is set to Yes, and will be used to set up IAM permissions, metrics, and CloudFormation template outputs.<br /> **Note:** This value is ignored if **Use Existing CloudFront Distribution** is set to `No`. |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.
