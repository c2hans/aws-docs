---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html
---

# BatchGetCollection
<a name="API_BatchGetCollection"></a>

Returns attributes for one or more collections, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

## Request Syntax
<a name="API_BatchGetCollection_RequestSyntax"></a>

```
{
   "ids": [ "{{string}}" ],
   "names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetCollection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ids](#API_BatchGetCollection_RequestSyntax) **   <a name="opensearchserverless-BatchGetCollection-request-ids"></a>
A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the [ListCollections](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html) API.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** [names](#API_BatchGetCollection_RequestSyntax) **   <a name="opensearchserverless-BatchGetCollection-request-names"></a>
A list of collection names. You can't provide names and IDs in the same request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

## Response Syntax
<a name="API_BatchGetCollection_ResponseSyntax"></a>

```
{
   "collectionDetails": [
      {
         "arn": "string",
         "collectionEndpoint": "string",
         "collectionGroupName": "string",
         "createdDate": number,
         "dashboardEndpoint": "string",
         "deletionProtection": "string",
         "description": "string",
         "failureCode": "string",
         "failureMessage": "string",
         "fipsEndpoints": {
            "collectionEndpoint": "string",
            "dashboardEndpoint": "string"
         },
         "id": "string",
         "kmsKeyArn": "string",
         "lastModifiedDate": number,
         "name": "string",
         "standbyReplicas": "string",
         "status": "string",
         "type": "string",
         "vectorOptions": {
            "ServerlessVectorAcceleration": "string"
         }
      }
   ],
   "collectionErrorDetails": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "id": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionDetails](#API_BatchGetCollection_ResponseSyntax) **   <a name="opensearchserverless-BatchGetCollection-response-collectionDetails"></a>
Details about each collection.
Type: Array of [CollectionDetail](API_CollectionDetail.md) objects

 ** [collectionErrorDetails](#API_BatchGetCollection_ResponseSyntax) **   <a name="opensearchserverless-BatchGetCollection-response-collectionErrorDetails"></a>
Error information for the request.
Type: Array of [CollectionErrorDetail](API_CollectionErrorDetail.md) objects

## Errors
<a name="API_BatchGetCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetCollection_Examples"></a>

### Retrieve attributes from multiple collections
<a name="API_BatchGetCollection_Example_1"></a>

The following example requests attributes from two different collections.

#### Sample Request
<a name="API_BatchGetCollection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: aoss.<region>.<domain>
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: OpenSearchServerless.BatchGetCollection

{
  "ids": ["1iu5usc4adj5", "1iu5usc4rame"]
}
```

#### Sample Response
<a name="API_BatchGetCollection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "collectionDetails": [
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc",
            "collectionEndpoint": "https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com",
            "createdDate": 1655422947204,
            "lastModifiedDate": 1655422947204,
            "dashboardEndpoint": "https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com/_dashboards",
            "fipsEndpoints": {
                "collectionEndpoint": "https://07tjusf2h91cunochc.us-east-1.aoss-fips.amazonaws.com",
                "dashboardEndpoint": "https://07tjusf2h91cunochc.us-east-1.aoss-fips.amazonaws.com/_dashboards"
            },
            "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "type": "TIMESERIES",
            "description": "Log data",
            "id": "07tjusf2h91cunochc",
            "name": "my-collection",
            "status": "ACTIVE"
        },
        {
            "id": "178ukvtg3i82dvopdid",
            "name": "another-collection",
            "status": "CREATING",
            "type": "TIMESERIES",
            "description": "",
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/178ukvtg3i82dvopdid",
            "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "createdDate": 1667446262828,
            "lastModifiedDate": 1667446300769,
            "collectionEndpoint": "https://178ukvtg3i82dvopdid.us-east-1.aoss.amazonaws.com",
            "dashboardEndpoint": "https://178ukvtg3i82dvopdid.us-east-1.aoss.amazonaws.com/_dashboards"
        }
    ],
    "collectionErrorDetails": []
}
```

## See Also
<a name="API_BatchGetCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/BatchGetCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/BatchGetCollection)
