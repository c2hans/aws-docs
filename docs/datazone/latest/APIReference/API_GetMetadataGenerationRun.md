---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetMetadataGenerationRun.html
---

# GetMetadataGenerationRun
<a name="API_GetMetadataGenerationRun"></a>

Gets a metadata generation run in Amazon DataZone.

Prerequisites:
+ Valid domain and run identifier.
+ The metadata generation run must exist.
+ User must have read access to the metadata run.

## Request Syntax
<a name="API_GetMetadataGenerationRun_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/metadata-generation-runs/{{identifier}}?type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMetadataGenerationRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetMetadataGenerationRun_RequestSyntax) **   <a name="datazone-GetMetadataGenerationRun-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain the metadata generation run of which you want to get.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetMetadataGenerationRun_RequestSyntax) **   <a name="datazone-GetMetadataGenerationRun-request-uri-identifier"></a>
The identifier of the metadata generation run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [type](#API_GetMetadataGenerationRun_RequestSyntax) **   <a name="datazone-GetMetadataGenerationRun-request-uri-type"></a>
The type of the metadata generation run.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

## Request Body
<a name="API_GetMetadataGenerationRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMetadataGenerationRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "id": "string",
   "owningProjectId": "string",
   "status": "string",
   "target": {
      "identifier": "string",
      "revision": "string",
      "type": "string"
   },
   "type": "string",
   "types": [ "string" ],
   "typeStats": [
      {
         "errorMessage": "string",
         "status": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMetadataGenerationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-createdAt"></a>
The timestamp of when the metadata generation run was start.
Type: Timestamp

 ** [createdBy](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-createdBy"></a>
The Amazon DataZone user who started the metadata generation run.
Type: String

 ** [domainId](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-domainId"></a>
The ID of the Amazon DataZone domain the metadata generation run of which you want to get.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-id"></a>
The ID of the metadata generation run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-owningProjectId"></a>
The ID of the project that owns the assets for which you're running metadata generation.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-status"></a>
The status of the metadata generation run.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELED | SUCCEEDED | FAILED | PARTIALLY_SUCCEEDED`

 ** [target](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-target"></a>
The asset for which you're generating metadata.
Type: [MetadataGenerationRunTarget](API_MetadataGenerationRunTarget.md) object

 ** [type](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-type"></a>
 *This parameter has been deprecated.*
The type of metadata generation run.
Type: String
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

 ** [types](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-types"></a>
The types of the metadata generation run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

 ** [typeStats](#API_GetMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-GetMetadataGenerationRun-response-typeStats"></a>
The type stats included in the metadata generation run output details.
Type: Array of [MetadataGenerationRunTypeStat](API_MetadataGenerationRunTypeStat.md) objects

## Errors
<a name="API_GetMetadataGenerationRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetMetadataGenerationRun_Examples"></a>

### Example
<a name="API_GetMetadataGenerationRun_Example_1"></a>

This example illustrates one usage of GetMetadataGenerationRun.

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_1_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr5g0fy285m1q"
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_1_Response"></a>

```
{
    "createdAt": 1752644436.666,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "id": "mgr5g0fy285m1q",
    "owningProjectId": "prj7nx82mkl",
    "status": "CANCELED",
    "target": {
        "identifier": "ast6br2md6v9h",
        "revision": "1",
        "type": "ASSET"
    },
    "types": ["BUSINESS_DESCRIPTIONS"]
}
```

### Example
<a name="API_GetMetadataGenerationRun_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_2_Request"></a>

```
aws datazone get-metadata-generation-run
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_2_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier, —identifier
```

### Example
<a name="API_GetMetadataGenerationRun_Example_3"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_3_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr_nonexistent"
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetMetadataGenerationRun operation: Requested prediction cannot be found in domain
```

### Example
<a name="API_GetMetadataGenerationRun_Example_4"></a>

Failure case - validation error:

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_4_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "wrongdomain" \
--identifier "mgr5g0fy285m1q"
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_4_Response"></a>

```
An error occurred (ValidationException) when calling the GetMetadataGenerationRun operation: 1 validation error detected: Value at 'domainIdentifier' failed to satisfy constraint: Member must satisfy regular expression pattern: dzd[-_][a-zA-Z0-9_-]{1,36}
```

### Example
<a name="API_GetMetadataGenerationRun_Example_5"></a>

Failure case - service quota exceeded:

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_5_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "wrongdomain" \
--identifier "mgr5g0fy285m1q"
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_5_Response"></a>

```
{
    "createdAt": 1.762972585509E9,
    "createdBy": "SYSTEM",
    "domainId": "dzd_6rexlvjnu84cbr",
    "id": "4sn866f04fzl47",
    "owningProjectId": "4dc7fa5wzsdup3",
    "status": "FAILED",
    "target": {
        "identifier": "duaeacyg76xovb",
        "revision": "23",
        "type": "ASSET"
    },
    "typeStats": [{
        "errorMessage": "business name generation has reached monthly quota",
        "status": "FAILED",
        "type": "BUSINESS_NAMES"
    }],
    "types": [
        "BUSINESS_NAMES"
    ]
}
```

### Example
<a name="API_GetMetadataGenerationRun_Example_6"></a>

GetMetadataGenerationRun with specific type:

#### Sample Request
<a name="API_GetMetadataGenerationRun_Example_6_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr5g0fy285m1q"
--type "BUSINESS_NAMES"
```

#### Sample Response
<a name="API_GetMetadataGenerationRun_Example_6_Response"></a>

```
{
  "createdAt": 1.762021397763E9,
  "createdBy": "",
  "domainId": "dzd_53ielnpxktdilj",
  "id": "mgr5g0fy285m1q",
  "owningProjectId": "4dc7fa5wzsdup3",
  "status": "SUCCEEDED",
  "target": {
    "identifier": "cy61vbvez4nuw7",
    "revision": "12",
    "type": "ASSET"
  },
  "type": "BUSINESS_NAMES",
  "typeStats": [
    {
      "status": "SUCCEEDED",
      "type": "BUSINESS_NAMES"
    }
  ],
  "types": [
    "BUSINESS_NAMES"
  ]
}
```

## See Also
<a name="API_GetMetadataGenerationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetMetadataGenerationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetMetadataGenerationRun)
