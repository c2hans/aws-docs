---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceView.html
---

# GetServiceView
<a name="API_GetServiceView"></a>

Retrieves details about a specific Resource Explorer service view. This operation returns the configuration and properties of the specified view.

## Request Syntax
<a name="API_GetServiceView_RequestSyntax"></a>

```
POST /GetServiceView HTTP/1.1
Content-type: application/json

{
   "ServiceViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetServiceView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetServiceView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ServiceViewArn](#API_GetServiceView_RequestSyntax) **   <a name="resourceexplorer-GetServiceView-request-ServiceViewArn"></a>
The Amazon Resource Name (ARN) of the service view to retrieve details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_GetServiceView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "View": {
      "Filters": {
         "FilterString": "string"
      },
      "IncludedProperties": [
         {
            "Name": "string"
         }
      ],
      "ScopeType": "string",
      "ServiceViewArn": "string",
      "StreamingAccessForService": "string"
   }
}
```

## Response Elements
<a name="API_GetServiceView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_GetServiceView_ResponseSyntax) **   <a name="resourceexplorer-GetServiceView-response-View"></a>
A `ServiceView` object that contains the details and configuration of the requested service view.
Type: [ServiceView](API_ServiceView.md) object

## Errors
<a name="API_GetServiceView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_GetServiceView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetServiceView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetServiceView)
