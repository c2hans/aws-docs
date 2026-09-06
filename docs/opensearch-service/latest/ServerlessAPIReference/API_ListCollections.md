---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html
---

# ListCollections
<a name="API_ListCollections"></a>

Lists all OpenSearch Serverless collections. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

**Note**
Make sure to include an empty request body {} if you don't include any collection filters in the request.

## Request Syntax
<a name="API_ListCollections_RequestSyntax"></a>

```
{
   "collectionFilters": {
      "collectionGroupName": "{{string}}",
      "name": "{{string}}",
      "status": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCollections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionFilters](#API_ListCollections_RequestSyntax) **   <a name="opensearchserverless-ListCollections-request-collectionFilters"></a>
 A list of filter names and values that you can use for requests.
Type: [CollectionFilters](API_CollectionFilters.md) object
Required: No

 ** [maxResults](#API_ListCollections_RequestSyntax) **   <a name="opensearchserverless-ListCollections-request-maxResults"></a>
The maximum number of results to return. Default is 20. You can use `nextToken` to get the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCollections_RequestSyntax) **   <a name="opensearchserverless-ListCollections-request-nextToken"></a>
If your initial `ListCollections` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListCollections` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_ListCollections_ResponseSyntax"></a>

```
{
   "collectionSummaries": [
      {
         "arn": "string",
         "collectionGroupName": "string",
         "id": "string",
         "kmsKeyArn": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCollections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionSummaries](#API_ListCollections_ResponseSyntax) **   <a name="opensearchserverless-ListCollections-response-collectionSummaries"></a>
Details about each collection.
Type: Array of [CollectionSummary](API_CollectionSummary.md) objects

 ** [nextToken](#API_ListCollections_ResponseSyntax) **   <a name="opensearchserverless-ListCollections-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListCollections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## Examples
<a name="API_ListCollections_Examples"></a>

### Retrieve all collections
<a name="API_ListCollections_Example_1"></a>

The following example lists all collections.

#### Sample Request
<a name="API_ListCollections_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: aoss.<region>.<domain>
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: OpenSearchServerless.ListCollections
{}
```

#### Sample Response
<a name="API_ListCollections_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "collectionSummaries": [
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc",
            "id": "07tjusf2h91cunochc",
            "name": "collection-1",
            "status": "ACTIVE"
        },
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/63hf8klid6904sfcvb",
            "id": "63hf8klid6904sfcvb",
            "name": "collection-2",
            "status": "FAILED"
        },
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/lo0p4fgjs6fbc87ads",
            "id": "lo0p4fgjs6fbc87ads",
            "name": "collection-3",
            "status": "ACTIVE"
        },
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/12hd79jbckl6dh4d89",
            "id": "12hd79jbckl6dh4d89",
            "name": "collection-4",
            "status": "DELETING"
        },
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/17dg8kiybd96dvnd8s",
            "id": "17dg8kiybd96dvnd8s",
            "name": "collection-5",
            "status": "CREATING"
        }
    ],
    "nextToken": "MWl1NXVzYzQ0b25q"
}
```

### Retrieve a subset of collections
<a name="API_ListCollections_Example_2"></a>

The following example lists collections with a status of `ACTIVE`.

#### Sample Request
<a name="API_ListCollections_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: aoss.<region>.<domain>
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: OpenSearchServerless.ListCollections
{
   "collectionFilters": {
      "status": "ACTIVE"
   }
}
```

#### Sample Response
<a name="API_ListCollections_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "collectionSummaries": [
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc",
            "id": "07tjusf2h91cunochc",
            "name": "collection-1",
            "status": "ACTIVE"
        },
        {
            "arn": "arn:aws:aoss:us-east-1:123456789012:collection/lo0p4fgjs6fbc87ads",
            "id": "lo0p4fgjs6fbc87ads",
            "name": "collection-3",
            "status": "ACTIVE"
        }
    ],
    "nextToken": "MWl1NXVzYzQ0b25q"
}
```

## See Also
<a name="API_ListCollections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListCollections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListCollections)
