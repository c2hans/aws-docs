---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSink.html
---

# GetSink
<a name="API_GetSink"></a>

Returns complete information about one monitoring account sink.

To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html).

## Request Syntax
<a name="API_GetSink_RequestSyntax"></a>

```
POST /GetSink HTTP/1.1
Content-type: application/json

{
   "Identifier": "{{string}}",
   "IncludeTags": {{boolean}}
}
```

## URI Request Parameters
<a name="API_GetSink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetSink_RequestSyntax) **   <a name="OAM-GetSink-request-Identifier"></a>
The ARN of the sink to retrieve information for.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

 ** [IncludeTags](#API_GetSink_RequestSyntax) **   <a name="OAM-GetSink-request-IncludeTags"></a>
Set `IncludeTags` to `true` to receive tags in the response, or `false` to exclude them.
The default value is `true`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetSink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "Name": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetSink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetSink_ResponseSyntax) **   <a name="OAM-GetSink-response-Arn"></a>
The ARN of the sink.
Type: String

 ** [Id](#API_GetSink_ResponseSyntax) **   <a name="OAM-GetSink-response-Id"></a>
The random ID string that AWS generated as part of the sink ARN.
Type: String

 ** [Name](#API_GetSink_ResponseSyntax) **   <a name="OAM-GetSink-response-Name"></a>
The name of the sink.
Type: String

 ** [Tags](#API_GetSink_ResponseSyntax) **   <a name="OAM-GetSink-response-Tags"></a>
The tags assigned to the sink.
Type: String to string map

## Errors
<a name="API_GetSink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## See Also
<a name="API_GetSink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/GetSink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/GetSink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/GetSink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/GetSink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/GetSink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/GetSink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/GetSink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/GetSink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/GetSink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/GetSink)
