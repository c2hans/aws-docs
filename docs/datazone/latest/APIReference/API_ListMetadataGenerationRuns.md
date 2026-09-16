---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListMetadataGenerationRuns.html
---

# ListMetadataGenerationRuns
<a name="API_ListMetadataGenerationRuns"></a>

Lists all metadata generation runs.

Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.

Prerequisites:
+ Valid domain identifier.
+ User must have access to metadata generation runs in the domain.

## Request Syntax
<a name="API_ListMetadataGenerationRuns_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/metadata-generation-runs?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}}&targetIdentifier={{targetIdentifier}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMetadataGenerationRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where you want to list metadata generation runs.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-maxResults"></a>
The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-nextToken"></a>
When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [status](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-status"></a>
The status of the metadata generation runs.
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELED | SUCCEEDED | FAILED | PARTIALLY_SUCCEEDED`

 ** [targetIdentifier](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-targetIdentifier"></a>
The target ID for which you want to list metadata generation runs.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [type](#API_ListMetadataGenerationRuns_RequestSyntax) **   <a name="datazone-ListMetadataGenerationRuns-request-uri-type"></a>
The type of the metadata generation runs.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

## Request Body
<a name="API_ListMetadataGenerationRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMetadataGenerationRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
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
         "types": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMetadataGenerationRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListMetadataGenerationRuns_ResponseSyntax) **   <a name="datazone-ListMetadataGenerationRuns-response-items"></a>
The results of the ListMetadataGenerationRuns action.
Type: Array of [MetadataGenerationRunItem](API_MetadataGenerationRunItem.md) objects

 ** [nextToken](#API_ListMetadataGenerationRuns_ResponseSyntax) **   <a name="datazone-ListMetadataGenerationRuns-response-nextToken"></a>
When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListMetadataGenerationRuns_Errors"></a>

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
<a name="API_ListMetadataGenerationRuns_Examples"></a>

### Example
<a name="API_ListMetadataGenerationRuns_Example_1"></a>

This example illustrates one usage of ListMetadataGenerationRuns.

#### Sample Request
<a name="API_ListMetadataGenerationRuns_Example_1_Request"></a>

```
aws datazone list-metadata-generation-runs --domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_ListMetadataGenerationRuns_Example_1_Response"></a>

```
{
    "items": [{
            "createdAt": 1752642939.631,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "mgr3tlpxo4mg5q",
            "owningProjectId": "prj7nx82mkl",
            "status": "SUCCEEDED",
            "target": {
                "identifier": "ast7k9mpq2xvn4",
                "revision": "1",
                "type": "ASSET"
            },
            "types": ["BUSINESS_DESCRIPTIONS"]
        },
        {
            "createdAt": 1752643907.566,
            "createdBy": "usr7nx82mkl",
            "domainId": "dzd_53ielnpxktdilj",
            "id": "mgr487vbdcqwn8",
            "owningProjectId": "prj7nx82mkl",
            "status": "SUCCEEDED",
            "target": {
                "identifier": "ast7k9mpq2xvn4",
                "revision": "4",
                "type": "ASSET"
            },
            "types": ["BUSINESS_DESCRIPTIONS"]
        },
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
    ]
}
```

### Example
<a name="API_ListMetadataGenerationRuns_Example_2"></a>

Failuse case - missing parameter:

#### Sample Request
<a name="API_ListMetadataGenerationRuns_Example_2_Request"></a>

```
aws datazone list-metadata-generation-runs
```

#### Sample Response
<a name="API_ListMetadataGenerationRuns_Example_2_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier
```

### Example
<a name="API_ListMetadataGenerationRuns_Example_3"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_ListMetadataGenerationRuns_Example_3_Request"></a>

```
aws datazone list-metadata-generation-runs --domain-identifier "invalid_domain"
```

#### Sample Response
<a name="API_ListMetadataGenerationRuns_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the ListMetadataGenerationRuns operation: 1 validation error detected: Value at 'domainIdentifier' failed to satisfy constraint: Member must satisfy regular expression pattern: dzd[-_][a-zA-Z0-9_-]{1,36}
```

### Example
<a name="API_ListMetadataGenerationRuns_Example_4"></a>

ListMetadataGenerationRuns with multiple filters:

#### Sample Request
<a name="API_ListMetadataGenerationRuns_Example_4_Request"></a>

```
aws datazone get-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--type "BUSINESS_NAMES"
--status "SUCCEEDED"
--target-identifier "cy61vbvez4nuw7"
```

#### Sample Response
<a name="API_ListMetadataGenerationRuns_Example_4_Response"></a>

```
{
  "items": [
    {
      "createdAt": 1.762021397763E9,
      "createdBy": "",
      "domainId": "dzd_53ielnpxktdilj",
      "id": "bcbuj2s3uooylj",
      "owningProjectId": "4dc7fa5wzsdup3",
      "status": "SUCCEEDED",
      "target": {
        "identifier": "cy61vbvez4nuw7",
        "revision": "12",
        "type": "ASSET"
      },
      "type": "BUSINESS_NAMES",
      "types": [
        "BUSINESS_NAMES"
      ]
    }
  ]
}
```

## See Also
<a name="API_ListMetadataGenerationRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListMetadataGenerationRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListMetadataGenerationRuns)
