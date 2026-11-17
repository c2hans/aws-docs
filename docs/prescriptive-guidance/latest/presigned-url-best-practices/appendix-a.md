---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/appendix-a.html
---

# Appendix A: How AWS services use presigned URLs
<a name="appendix-a"></a>

This appendix provides information about AWS services and features that use presigned URLs. This information serves two purposes:
+ To provide security engineers who implement controls with information about the possible impacts of those controls.
+ To create awareness of situations where this risk might be relevant for URL logging interactions.

**Important**
This appendix doesn't provide a complete list of AWS services or their usage of presigned URLs. It also doesn't cover custom or third-party solutions.

## Amazon S3 console
<a name="s3-console"></a>

**Principal:** Console user **Default expiration:** 5 minutes

**Disclaimer**: This section documents the current behavior of the Amazon S3 console.  AWS console behaviors are subject to change without notice.

The Amazon S3 console supports downloading and uploading objects. Downloads use a presigned URL that expires after 300 seconds (5 minutes).  The console generates the URL by sending a request to `https://<bucket-region>.console.aws.amazon.com/s3/batchOpsServlet-proxy`.

That request starts when you choose the download button. The console doesn't generate the URL in advance or send it to the client until you request the download.

Uploads are similar, except that the console sends two requests: `OPTIONS` as a preflight cross-origin resource sharing (CORS) check, and `PUT`. Both requests use the same signature.

The console signs requests with temporary credentials associated with the currently signed-in user. This guide doesn't cover how the console obtains those temporary credentials.

## Amazon S3 Object Lambda
<a name="s3-object-lambda"></a>

**Principal:** Access point caller **Default expiration:** 61 seconds

**Note**
As of November 7, 2025, Amazon S3 Object Lambda is available only to existing customers that are currently using the service and to select AWS Partner Network (APN) partners. For capabilities similar to S3 Object Lambda, see [Amazon S3 Object Lambda availability change](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html).

[Amazon S3 Object Lambda](https://aws.amazon.com/s3/features/object-lambda/) uses AWS Lambda functions to automatically process and transform data when your application retrieves it from Amazon S3. When S3 Object Lambda invokes a function, it provides the function with a presigned URL (`inputS3Url`) that the function can use to download the original object from the supporting access point.

These presigned URLs are signed for the [supporting Amazon S3 access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-security.html#olap-access-points-security), which is provided when you configure S3 Object Lambda. (This is not the same as the Object Lambda access point.) Instead of using a role that's bound to the Lambda function, the URL is signed by using the original caller's identity, and that user's permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these headers in the call to Amazon S3.

The presigned URL that's returned has an expiration time of 61 seconds (one second more than the maximum duration for an S3 Object Lambda function). The generated URL can be used only with the supporting access point. The caller of the S3 Object Lambda access point needs to have access to this access point. You can limit that access to the context of S3 Object Lambda by using the condition `"aws:CalledVia": ["s3-object-lambda.amazonaws.com"]`. When that condition is attached to a supporting access point or bucket, a user can't access the supporting access point or bucket directly.

With this approach, you don't need to grant the Lambda function access to your S3 bucket or access point. The role that's associated with the Lambda function needs permissions for **WriteGetObjectResponse**, but it doesn't need permissions for **GetObject**.

When S3 Object Lambda generates presigned URLs, it doesn't add network restrictions, so you can use a URL outside the Lambda function. However, any restrictions placed on the caller of S3 Object Lambda still apply. For example, if your Lambda function runs in an Amazon VPC and you restrict the caller to using a VPC endpoint, anyone who has the presigned URL must send it through that VPC endpoint. This restriction also applies to **SourceIp** and **VpcSourceIp**.

**Note**
To use an S3 Object Lambda function in a VPC, the VPC must have a route to public S3 endpoints to call **WriteGetObjectResponse**. This route doesn't remove VPC endpoint requirements for requests that retrieve data from the bucket.

## AWS Lambda Cross-Region CopyObject
<a name="lambda-cross-region-copy-object"></a>

**Principal: **AWS internal

**Default expiration: **3600 seconds

When you use the [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) or [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) API to copy across AWS Regions, Amazon S3 uses presigned URLs internally. You can call these APIs directly from SDKs or from the AWS CLI commands `aws s3api copy-object` and `aws s3api upload-part-copy`. Amazon S3 Replication doesn't use these APIs, but the AWS CLI `aws s3 cp` and `aws s3 sync` commands use them when the source and destination are S3 buckets. Various AWS SDKs also support them through `TransferManager` implementations.

## AWS Lambda GetFunction
<a name="lambda-get-function"></a>

**Principal:** AWS internal **Default expiration:** 10 minutes

AWS Lambda stores the user version in an S3 bucket that the Lambda team owns, before generating the assets deployed to Lambda containers. When you want to access the code for your function, call the [GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html) API. This API responds with `Code.Location`, which contains a presigned URL that's valid for 10 minutes (this expiration time is current behavior and not a published contract). If you don't want the code, you can use a combination of [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html), [GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConcurrency.html), and [ListTags](https://docs.aws.amazon.com/lambda/latest/dg/API_ListTags.html) to retrieve the other data that `GetFunction` returns.

Lambda signs the returned URL on behalf of the user, not with the credentials of the currently signed-in user. For this reason, condition keys (such as `aws:SourceIP`) that apply to the currently signed-in user or the user's temporary session credentials don't apply to the generated URL. This is true whether the condition keys apply to **GetFunction** only, or to all AWS API usage for the user or session.

The Lambda console also uses **GetFunction** and the presigned URL it returns. The console uses the temporary credentials associated with the currently signed-in user to call **GetFunction**. This document doesn't cover how the console obtains those temporary credentials.

## Amazon ECR
<a name="ecr"></a>

**Principal:** AWS internal **Default expiration:** 1 hour

[Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) (Amazon ECR) provides the [GetDownloadUrlForLayer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html) API, which returns a presigned URL that's valid for one hour and supports the download of a single layer from an Amazon ECR image. However, the Amazon ECR proxy uses this operation, and you generally don't use it to pull and push images.

## Amazon Redshift Spectrum
<a name="spectrum"></a>

**Principal: **Role passed to [CREATE EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html) through `IAM_ROLE` **Default expiration: **1 hour

Amazon Redshift Spectrum uses presigned URLs internally and [prohibits restrictions on the combination of the bucket and Amazon Redshift role that would limit presigned URLs](https://docs.aws.amazon.com/redshift/latest/mgmt/spectrum-enhanced-vpc.html#spectrum-enhanced-vpc-considerations-policies). You can use an `s3:signatureAge` value of 16 minutes, but very low values might cause queries to fail. The minimum value you can use depends on the timing and size of your query. A value that's lower than 16 minutes works for many scenarios, but you must test it. Restrict the role so that only Redshift Spectrum can use it. Redshift Spectrum doesn't disclose the URLs it generates, which mitigates the typical justification for lower expiration values.

## Amazon SageMaker AI Studio
<a name="sagemaker-studio"></a>

Amazon SageMaker AI Studio supports two API actions: [CreatePresignedDomainUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedDomainUrl.html) and [CreatePresignedNotebookInstanceUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html). However, these APIs aren't related to the Signature Version 4 presigned URL feature. These APIs create a URL that uses an `authToken` parameter, but they don't support any of the standard Signature Version 4 query parameters.

`authToken` is a different mechanism but has similarities to presigned URLs. It's sent as a query string parameter and supports an expiration time of 5 minutes.

SageMaker AI supports network restrictions. If you place a restriction on the `sagemaker:CreatePresignedDomainUrl` action, that action applies both to calling [CreatePresignedDomainUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedDomainUrl.html) and to using the generated URL. If you generate a URL from a valid network and then send it from an invalid network, the API call to generate the URL succeeds, but the request that sends the URL fails. The same is true of [CreatePresignedNotebookInstanceUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html) and the `sagemaker:CreatePresignedNotebookInstanceUrl` action.

For more information, see the [SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-access-ws.html).
