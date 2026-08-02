---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/endpoints.html
---

# Endpoints
<a name="endpoints"></a>

## URI
<a name="endpoints-url"></a>

`/2017-08-29/endpoints`

## HTTP methods
<a name="endpoints-http-methods"></a>

### POST
<a name="endpointspost"></a>

**Operation ID:** `DescribeEndpoints`

Send a request with an empty body to the regional API endpoint to get your account API endpoint. Note that DescribeEndpoints is no longer required. We recommend that you send your requests directly to the regional endpoint instead.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeEndpointsResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="endpointsoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="endpoints-schemas"></a>

### Request bodies
<a name="endpoints-request-examples"></a>

#### POST schema
<a name="endpoints-request-body-post-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer,
  "mode": enum
}
```

### Response bodies
<a name="endpoints-response-examples"></a>

#### DescribeEndpointsResponse schema
<a name="endpoints-response-body-describeendpointsresponse-example"></a>

```
{
  "endpoints": [
    {
      "url": "string"
    }
  ],
  "nextToken": "string"
}
```

#### ExceptionBody schema
<a name="endpoints-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="endpoints-properties"></a>

### DescribeEndpointsMode
<a name="endpoints-model-describeendpointsmode"></a>

Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET\_ONLY to return your endpoints if any exist, or an empty list if none exist.
+ `DEFAULT`
+ `GET_ONLY`

### DescribeEndpointsRequest
<a name="endpoints-model-describeendpointsrequest"></a>

Send a request with an empty body to the regional API endpoint to get your account API endpoint. Note that DescribeEndpoints is no longer required. We recommend that you send your requests directly to the regional endpoint instead.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxResults | integer<br />Format: int32 | False | Optional. Max number of endpoints, up to twenty, that will be returned at one time. |
| mode | [DescribeEndpointsMode](#endpoints-model-describeendpointsmode) | False | Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET\_ONLY to return your endpoints if any exist, or an empty list if none exist. |
| nextToken | string | False | Use this string, provided with the response to a previous request, to request the next batch of endpoints. |

### DescribeEndpointsResponse
<a name="endpoints-model-describeendpointsresponse"></a>

Successful describe endpoints requests will return your account API endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| endpoints | Array of type [Endpoint](#endpoints-model-endpoint) | False | List of endpoints |
| nextToken | string | False | Use this string to request the next batch of endpoints. |

### Endpoint
<a name="endpoints-model-endpoint"></a>

Describes an account-specific API endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| url | string | False | URL of endpoint |

### ExceptionBody
<a name="endpoints-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="endpoints-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeEndpoints
<a name="DescribeEndpoints-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/DescribeEndpoints)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/DescribeEndpoints)
