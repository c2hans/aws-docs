---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetMLConfiguration.html
---

# GetMLConfiguration
<a name="API_GetMLConfiguration"></a>

Returns information about a specific ML configuration.

## Request Syntax
<a name="API_GetMLConfiguration_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/ml-configurations HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMLConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_GetMLConfiguration_RequestSyntax) **   <a name="API-GetMLConfiguration-request-uri-membershipIdentifier"></a>
The membership ID of the member that owns the ML configuration you want to return information about.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetMLConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMLConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createTime": "string",
   "defaultOutputLocation": {
      "destination": {
         "s3Destination": {
            "s3Uri": "string"
         }
      },
      "roleArn": "string"
   },
   "membershipIdentifier": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetMLConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createTime](#API_GetMLConfiguration_ResponseSyntax) **   <a name="API-GetMLConfiguration-response-createTime"></a>
The time at which the ML configuration was created.
Type: Timestamp

 ** [defaultOutputLocation](#API_GetMLConfiguration_ResponseSyntax) **   <a name="API-GetMLConfiguration-response-defaultOutputLocation"></a>
The Amazon S3 location where ML model output is stored.
Type: [MLOutputConfiguration](API_MLOutputConfiguration.md) object

 ** [membershipIdentifier](#API_GetMLConfiguration_ResponseSyntax) **   <a name="API-GetMLConfiguration-response-membershipIdentifier"></a>
The membership ID of the member that owns the ML configuration you requested.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [updateTime](#API_GetMLConfiguration_ResponseSyntax) **   <a name="API-GetMLConfiguration-response-updateTime"></a>
The most recent time at which the ML configuration was updated.
Type: Timestamp

## Errors
<a name="API_GetMLConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetMLConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetMLConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetMLConfiguration)
