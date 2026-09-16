---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html
---

# GetJobTagging
<a name="API_control_GetJobTagging"></a>

Returns the tags on an S3 Batch Operations job.

Permissions
To use the `GetJobTagging` operation, you must have permission to perform the `s3:GetJobTagging` action. For more information, see [Controlling access and labeling jobs using tags](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags) in the *Amazon S3 User Guide*.

Related actions include:
+  [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
+  [PutJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html)
+  [DeleteJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html)

## Request Syntax
<a name="API_control_GetJobTagging_RequestSyntax"></a>

```
GET /v20180820/jobs/{{id}}/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetJobTagging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_GetJobTagging_RequestSyntax) **   <a name="AmazonS3-control_GetJobTagging-request-uri-uri-JobId"></a>
The ID for the S3 Batch Operations job whose tags you want to retrieve.
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [x-amz-account-id](#API_control_GetJobTagging_RequestSyntax) **   <a name="AmazonS3-control_GetJobTagging-request-header-AccountId"></a>
The AWS account ID associated with the S3 Batch Operations job.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetJobTagging_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetJobTagging_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetJobTaggingResult>
   <Tags>
      <S3Tag>
         <Key>string</Key>
         <Value>string</Value>
      </S3Tag>
   </Tags>
</GetJobTaggingResult>
```

## Response Elements
<a name="API_control_GetJobTagging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetJobTaggingResult](#API_control_GetJobTagging_ResponseSyntax) **   <a name="AmazonS3-control_GetJobTagging-response-GetJobTaggingResult"></a>
Root level tag for the GetJobTaggingResult parameters.
Required: Yes

 ** [Tags](#API_control_GetJobTagging_ResponseSyntax) **   <a name="AmazonS3-control_GetJobTagging-response-Tags"></a>
The set of tags associated with the S3 Batch Operations job.
Type: Array of [S3Tag](API_control_S3Tag.md) data types

## Errors
<a name="API_control_GetJobTagging_Errors"></a>

 ** InternalServiceException **

HTTP Status Code: 500

 ** NotFoundException **

HTTP Status Code: 400

 ** TooManyRequestsException **

HTTP Status Code: 400

## See Also
<a name="API_control_GetJobTagging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetJobTagging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetJobTagging)
