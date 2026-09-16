---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListCloudConnectors.html
---

# ListCloudConnectors
<a name="API_ListCloudConnectors"></a>

Returns a list of connectors filtered by its AWS Lambda Amazon Resource Name (ARN) and `type`.

## Request Syntax
<a name="API_ListCloudConnectors_RequestSyntax"></a>

```
GET /cloud-connectors?LambdaArn={{LambdaArn}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&Type={{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCloudConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LambdaArn](#API_ListCloudConnectors_RequestSyntax) **   <a name="managedintegrations-ListCloudConnectors-request-uri-LambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function to filter cloud connectors by.
Pattern: `(arn:aws:lambda:[0-9a-zA-Z-]+:[0-9]+:function:)?([a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?)`

 ** [MaxResults](#API_ListCloudConnectors_RequestSyntax) **   <a name="managedintegrations-ListCloudConnectors-request-uri-MaxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListCloudConnectors_RequestSyntax) **   <a name="managedintegrations-ListCloudConnectors-request-uri-NextToken"></a>
A token that can be used to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [Type](#API_ListCloudConnectors_RequestSyntax) **   <a name="managedintegrations-ListCloudConnectors-request-uri-Type"></a>
The type of cloud connectors to filter by when listing available connectors.
Valid Values: `LISTED | UNLISTED`

## Request Body
<a name="API_ListCloudConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCloudConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Description": "string",
         "EndpointConfig": {
            "lambda": {
               "arn": "string"
            }
         },
         "EndpointType": "string",
         "Id": "string",
         "Name": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCloudConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListCloudConnectors_ResponseSyntax) **   <a name="managedintegrations-ListCloudConnectors-response-Items"></a>
The list of connectors.
Type: Array of [ConnectorItem](API_ConnectorItem.md) objects

 ** [NextToken](#API_ListCloudConnectors_ResponseSyntax) **   <a name="managedintegrations-ListCloudConnectors-response-NextToken"></a>
A token that can be used to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListCloudConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListCloudConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListCloudConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListCloudConnectors)
