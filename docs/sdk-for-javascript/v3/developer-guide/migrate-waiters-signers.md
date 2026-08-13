---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-waiters-signers.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Waiters and signers
<a name="migrate-waiters-signers"></a>

This page describes the usage of waiters and signers in the AWS SDK for JavaScript v3.

## Waiters
<a name="waiters"></a>

 In v2, all waiters are bound to the service client class, and you need to specify in waiter's input which designed state the client will be waiting for. For example, you need to call [`waitFor("bucketExists")`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#bucketExists-waiter) to wait for a newly created bucket to be ready.

 In v3, you don't need to import waiters if your application doesn't need one. Moreover, you can import only the waiter you need to wait for the particular desired state you want. Thus, you can reduce your bundle size and improve performance. Here is an example of waiting for bucket to be ready after creation:

```
import { S3Client, CreateBucketCommand, waitUntilBucketExists } from "@aws-sdk/client-s3"; // ES6 import
// const { S3Client, CreateBucketCommand, waitUntilBucketExists } = require("@aws-sdk/client-s3"); // CommonJS import

const Bucket = "{{BUCKET_NAME}}";
const client = new S3Client({ region: "{{REGION}}" });
const command = new CreateBucketCommand({ Bucket });

await client.send(command);
await waitUntilBucketExists({ client, maxWaitTime: 60 }, { Bucket });
```

 You can find everything of how to configure the waiters in the [blog post of waiters in the AWS SDK for JavaScript v3](https://aws.amazon.com/blogs/developer/waiters-in-modular-aws-sdk-for-javascript/).

## Amazon CloudFront Signer
<a name="cloudfront-signer"></a>

 In v2, you can sign the request to access restricted Amazon CloudFront distributions with [`AWS.CloudFront.Signer`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CloudFront/Signer.html).

 In v3, you have the same utilities provided in the [`@aws-sdk/cloudfront-signer`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_cloudfront_signer.html) package.

## Amazon RDS Signer
<a name="rds-signer"></a>

 In v2, you can generate the auth token to an Amazon RDS database using [`AWS.RDS.Signer`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/RDS/Signer.html).

 In v3, the similar utility class is available in [` @aws-sdk/rds-signer`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_rds_signer.html) package.

## Amazon Polly Signer
<a name="polly-signer"></a>

 In v2, you can generate a signed URL to the speech synthesized by Amazon Polly service with [` AWS.Polly.Presigner`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Polly/Presigner.html).

 In v3, the similar utility function is available in [` @aws-sdk/polly-request-presigner`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_polly_request_presigner.html) package.
