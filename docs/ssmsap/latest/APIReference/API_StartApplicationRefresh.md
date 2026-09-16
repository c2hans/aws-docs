---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StartApplicationRefresh.html
---

# StartApplicationRefresh
<a name="API_StartApplicationRefresh"></a>

Refreshes a registered application.

## Request Syntax
<a name="API_StartApplicationRefresh_RequestSyntax"></a>

```
POST /start-application-refresh HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartApplicationRefresh_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartApplicationRefresh_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_StartApplicationRefresh_RequestSyntax) **   <a name="ssmsap-StartApplicationRefresh-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

## Response Syntax
<a name="API_StartApplicationRefresh_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_StartApplicationRefresh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_StartApplicationRefresh_ResponseSyntax) **   <a name="ssmsap-StartApplicationRefresh-response-OperationId"></a>
The ID of the operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`

## Errors
<a name="API_StartApplicationRefresh_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflict has occurred.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** UnauthorizedException **
The request is not authorized.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartApplicationRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/StartApplicationRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/StartApplicationRefresh)
