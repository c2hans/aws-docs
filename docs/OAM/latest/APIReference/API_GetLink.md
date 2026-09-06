---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetLink.html
---

# GetLink
<a name="API_GetLink"></a>

Returns complete information about one link.

To use this operation, provide the link ARN. To retrieve a list of link ARNs, use [ListLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html).

## Request Syntax
<a name="API_GetLink_RequestSyntax"></a>

```
POST /GetLink HTTP/1.1
Content-type: application/json

{
   "Identifier": "{{string}}",
   "IncludeTags": {{boolean}}
}
```

## URI Request Parameters
<a name="API_GetLink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetLink_RequestSyntax) **   <a name="OAM-GetLink-request-Identifier"></a>
The ARN of the link to retrieve information for.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

 ** [IncludeTags](#API_GetLink_RequestSyntax) **   <a name="OAM-GetLink-request-IncludeTags"></a>
Set `IncludeTags` to `true` to receive tags in the response, or `false` to exclude them.
The default value is `true`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetLink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "Label": "string",
   "LabelTemplate": "string",
   "LinkConfiguration": {
      "LogGroupConfiguration": {
         "Filter": "string"
      },
      "MetricConfiguration": {
         "Filter": "string"
      }
   },
   "ResourceTypes": [ "string" ],
   "SinkArn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-Arn"></a>
The ARN of the link.
Type: String

 ** [Id](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-Id"></a>
The random ID string that AWS generated as part of the link ARN.
Type: String

 ** [Label](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-Label"></a>
The label that you assigned to this link, with the variables resolved to their actual values.
Type: String

 ** [LabelTemplate](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-LabelTemplate"></a>
The exact label template that was specified when the link was created, with the template variables not resolved.
Type: String

 ** [LinkConfiguration](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-LinkConfiguration"></a>
This structure includes filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.
Type: [LinkConfiguration](API_LinkConfiguration.md) object

 ** [ResourceTypes](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-ResourceTypes"></a>
The resource types supported by this link.
Type: Array of strings

 ** [SinkArn](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-SinkArn"></a>
The ARN of the sink that is used for this link.
Type: String

 ** [Tags](#API_GetLink_ResponseSyntax) **   <a name="OAM-GetLink-response-Tags"></a>
The tags assigned to the link.
Type: String to string map

## Errors
<a name="API_GetLink_Errors"></a>

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
<a name="API_GetLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/GetLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/GetLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/GetLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/GetLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/GetLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/GetLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/GetLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/GetLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/GetLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/GetLink)
