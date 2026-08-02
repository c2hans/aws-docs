---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_UpdateApplicationSettings.html
---

# UpdateApplicationSettings
<a name="API_UpdateApplicationSettings"></a>

Updates the settings of an application registered with AWS Systems Manager for SAP.

## Request Syntax
<a name="API_UpdateApplicationSettings_RequestSyntax"></a>

```
POST /update-application-settings HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "Backint": {
      "BackintMode": "{{string}}",
      "EnsureNoBackupInProcess": {{boolean}}
   },
   "CredentialsToAddOrUpdate": [
      {
         "CredentialType": "{{string}}",
         "DatabaseName": "{{string}}",
         "SecretId": "{{string}}"
      }
   ],
   "CredentialsToRemove": [
      {
         "CredentialType": "{{string}}",
         "DatabaseName": "{{string}}",
         "SecretId": "{{string}}"
      }
   ],
   "DatabaseArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApplicationSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateApplicationSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_UpdateApplicationSettings_RequestSyntax) **   <a name="ssmsap-UpdateApplicationSettings-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [Backint](#API_UpdateApplicationSettings_RequestSyntax) **   <a name="ssmsap-UpdateApplicationSettings-request-Backint"></a>
Installation of AWS Backint Agent for SAP HANA.
Type: [BackintConfig](API_BackintConfig.md) object
Required: No

 ** [CredentialsToAddOrUpdate](#API_UpdateApplicationSettings_RequestSyntax) **   <a name="ssmsap-UpdateApplicationSettings-request-CredentialsToAddOrUpdate"></a>
The credentials to be added or updated.
Type: Array of [ApplicationCredential](API_ApplicationCredential.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [CredentialsToRemove](#API_UpdateApplicationSettings_RequestSyntax) **   <a name="ssmsap-UpdateApplicationSettings-request-CredentialsToRemove"></a>
The credentials to be removed.
Type: Array of [ApplicationCredential](API_ApplicationCredential.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [DatabaseArn](#API_UpdateApplicationSettings_RequestSyntax) **   <a name="ssmsap-UpdateApplicationSettings-request-DatabaseArn"></a>
The Amazon Resource Name of the SAP HANA database that replaces the current SAP HANA connection with the SAP\_ABAP application.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

## Response Syntax
<a name="API_UpdateApplicationSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string",
   "OperationIds": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateApplicationSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_UpdateApplicationSettings_ResponseSyntax) **   <a name="ssmsap-UpdateApplicationSettings-response-Message"></a>
The update message.
Type: String

 ** [OperationIds](#API_UpdateApplicationSettings_ResponseSyntax) **   <a name="ssmsap-UpdateApplicationSettings-response-OperationIds"></a>
The IDs of the operations.
Type: Array of strings
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`

## Errors
<a name="API_UpdateApplicationSettings_Errors"></a>

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
<a name="API_UpdateApplicationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/UpdateApplicationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/UpdateApplicationSettings)
