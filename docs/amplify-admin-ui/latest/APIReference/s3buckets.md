---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/s3buckets.html
---

# S3Buckets
<a name="s3buckets"></a>

List the Amazon S3 buckets in your AWS account.

## URI
<a name="s3buckets-url"></a>

`/prod/s3Buckets`

## HTTP methods
<a name="s3buckets-http-methods"></a>

### POST
<a name="s3bucketspost"></a>

**Operation ID:** `ListS3Buckets`

The list of S3 buckets in your account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListS3BucketsRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="s3bucketsoptions"></a>

Enables CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="s3buckets-schemas"></a>

### Request bodies
<a name="s3buckets-request-examples"></a>

#### POST schema
<a name="s3buckets-request-body-post-example"></a>

```
{
  "nextToken": "string"
}
```

### Response bodies
<a name="s3buckets-response-examples"></a>

#### ListS3BucketsRespObj schema
<a name="s3buckets-response-body-lists3bucketsrespobj-example"></a>

```
{
  "nextToken": "string",
  "buckets": [
    {
      "name": "string",
      "creationDate": "string"
    }
  ]
}
```

#### BadRequestException schema
<a name="s3buckets-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="s3buckets-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="s3buckets-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="s3buckets-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="s3buckets-properties"></a>

### BadRequestException
<a name="s3buckets-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="s3buckets-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="s3buckets-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### ListS3BucketsReqObj
<a name="s3buckets-model-lists3bucketsreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Reserved for future use. |

### ListS3BucketsRespObj
<a name="s3buckets-model-lists3bucketsrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| buckets | Array of type [S3BucketInfo](#s3buckets-model-s3bucketinfo) | True | The list of S3 buckets. |
| nextToken | string | False | Reserved for future use. |

### NotFoundException
<a name="s3buckets-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### S3BucketInfo
<a name="s3buckets-model-s3bucketinfo"></a>

Describes the metadata of the S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationDate | string | False | The creation date of the S3 bucket. |
| name | string | False | The name of the S3 bucket. |

## See also
<a name="s3buckets-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListS3Buckets
<a name="ListS3Buckets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/ListS3Buckets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/ListS3Buckets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
