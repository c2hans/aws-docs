---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_StopApplication.html
---

# StopApplication
<a name="API_StopApplication"></a>

Request is an operation to stop an application.

Parameter `ApplicationId` is required. Parameters `StopConnectedEntity` and `IncludeEc2InstanceShutdown` are optional.

## Request Syntax
<a name="API_StopApplication_RequestSyntax"></a>

```
POST /stop-application HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "IncludeEc2InstanceShutdown": {{boolean}},
   "StopConnectedEntity": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_StopApplication_RequestSyntax) **   <a name="ssmsap-StopApplication-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [IncludeEc2InstanceShutdown](#API_StopApplication_RequestSyntax) **   <a name="ssmsap-StopApplication-request-IncludeEc2InstanceShutdown"></a>
Boolean. If included and if set to `True`, the StopApplication operation will shut down the associated Amazon EC2 instance in addition to the application.
Type: Boolean
Required: No

 ** [StopConnectedEntity](#API_StopApplication_RequestSyntax) **   <a name="ssmsap-StopApplication-request-StopConnectedEntity"></a>
Specify the `ConnectedEntityType`. Accepted type is `DBMS`.
If this parameter is included, the connected DBMS (Database Management System) will be stopped.
Type: String
Valid Values: `DBMS`
Required: No

## Response Syntax
<a name="API_StopApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_StopApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_StopApplication_ResponseSyntax) **   <a name="ssmsap-StopApplication-response-OperationId"></a>
The ID of the operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`

## Errors
<a name="API_StopApplication_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/StopApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/StopApplication)
