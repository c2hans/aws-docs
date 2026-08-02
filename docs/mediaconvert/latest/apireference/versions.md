---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/versions.html
---

# Versions
<a name="versions"></a>

## URI
<a name="versions-url"></a>

`/2017-08-29/versions`

## HTTP methods
<a name="versions-http-methods"></a>

### GET
<a name="versionsget"></a>

**Operation ID:** `ListVersions`

Retrieve a JSON array of all available Job engine versions and the date they expire.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListVersionsResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="versionsoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="versions-schemas"></a>

### Request bodies
<a name="versions-request-examples"></a>

#### GET schema
<a name="versions-request-body-get-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer
}
```

### Response bodies
<a name="versions-response-examples"></a>

#### ListVersionsResponse schema
<a name="versions-response-body-listversionsresponse-example"></a>

```
{
  "versions": [
    {
      "version": "string",
      "expirationDate": "string"
    }
  ],
  "nextToken": "string"
}
```

#### ExceptionBody schema
<a name="versions-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="versions-properties"></a>

### ExceptionBody
<a name="versions-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### JobEngineVersion
<a name="versions-model-jobengineversion"></a>

Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions are in a YYYY-MM-DD format.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| expirationDate | string<br />Format: date-time | False | The date that this Job engine version expires. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested. |
| version | string | False | Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions represent periodically grouped MediaConvert releases with new features, updates, improvements, and fixes. Job engine versions are in a YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support. |

### ListVersionsRequest
<a name="versions-model-listversionsrequest"></a>

Retrieve a JSON array of all available Job engine versions and the date they expire. Job engine versions are in YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxResults | integer<br />Format: int32<br />Minimum: 1<br />Maximum: 20 | False | Optional. Number of valid Job engine versions, up to twenty, that will be returned at one time. |
| nextToken | string | False | Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions. |

### ListVersionsResponse
<a name="versions-model-listversionsresponse"></a>

Successful list versions requests will return a JSON for available Job engine versions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions. |
| versions | Array of type [JobEngineVersion](#versions-model-jobengineversion) | False | Retrieve a JSON array of all available Job engine versions and the date they expire. |

## See also
<a name="versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListVersions
<a name="ListVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/ListVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/ListVersions)
