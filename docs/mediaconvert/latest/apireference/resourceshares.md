---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/resourceshares.html
---

# ResourceShares
<a name="resourceshares"></a>

## URI
<a name="resourceshares-url"></a>

`/2017-08-29/resourceShares`

## HTTP methods
<a name="resourceshares-http-methods"></a>

### POST
<a name="resourcesharespost"></a>

**Operation ID:** `CreateResourceShare`

Create a new resource share request for MediaConvert resources with Support.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | CreateResourceShareResponse | 202 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="resourcesharesoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="resourceshares-schemas"></a>

### Request bodies
<a name="resourceshares-request-examples"></a>

#### POST schema
<a name="resourceshares-request-body-post-example"></a>

```
{
  "jobId": "string",
  "supportCaseId": "string"
}
```

### Response bodies
<a name="resourceshares-response-examples"></a>

#### CreateResourceShareResponse schema
<a name="resourceshares-response-body-createresourceshareresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="resourceshares-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="resourceshares-properties"></a>

### CreateResourceShareRequest
<a name="resourceshares-model-createresourcesharerequest"></a>

The request to share MediaConvert resources with Support.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobId | string | True | Specify MediaConvert Job ID or ARN to share |
| supportCaseId | string | True | Support case identifier |

### CreateResourceShareResponse
<a name="resourceshares-model-createresourceshareresponse"></a>

Successfully accepted the request to share MediaConvert resources.

### ExceptionBody
<a name="resourceshares-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="resourceshares-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateResourceShare
<a name="CreateResourceShare-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/CreateResourceShare)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/CreateResourceShare)
