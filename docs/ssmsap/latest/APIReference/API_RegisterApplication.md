---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_RegisterApplication.html
---

# RegisterApplication
<a name="API_RegisterApplication"></a>

Register an SAP application with AWS Systems Manager for SAP. You must meet the following requirements before registering.

The SAP application you want to register with AWS Systems Manager for SAP is running on Amazon EC2.

AWS Systems Manager Agent must be setup on an Amazon EC2 instance along with the required IAM permissions.

Amazon EC2 instance(s) must have access to the secrets created in AWS Secrets Manager to manage SAP applications and components.

## Request Syntax
<a name="API_RegisterApplication_RequestSyntax"></a>

```
POST /register-application HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "ApplicationType": "{{string}}",
   "ComponentsInfo": [
      {
         "ComponentType": "{{string}}",
         "Ec2InstanceId": "{{string}}",
         "Sid": "{{string}}"
      }
   ],
   "Credentials": [
      {
         "CredentialType": "{{string}}",
         "DatabaseName": "{{string}}",
         "SecretId": "{{string}}"
      }
   ],
   "DatabaseArn": "{{string}}",
   "Instances": [ "{{string}}" ],
   "SapInstanceNumber": "{{string}}",
   "Sid": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_RegisterApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [ApplicationType](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-ApplicationType"></a>
The type of the application.
Type: String
Valid Values: `HANA | SAP_ABAP`
Required: Yes

 ** [ComponentsInfo](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-ComponentsInfo"></a>
This is an optional parameter for component details to which the SAP ABAP application is attached, such as Web Dispatcher.
This is an array of ApplicationComponent objects. You may input 0 to 5 items.
Type: Array of [ComponentInfo](API_ComponentInfo.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [Credentials](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-Credentials"></a>
The credentials of the SAP application.
Type: Array of [ApplicationCredential](API_ApplicationCredential.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [DatabaseArn](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-DatabaseArn"></a>
The Amazon Resource Name of the SAP HANA database.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** [Instances](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-Instances"></a>
The Amazon EC2 instances on which your SAP application is running.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `i-[\w\d]{8}$|^i-[\w\d]{17}`
Required: Yes

 ** [SapInstanceNumber](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-SapInstanceNumber"></a>
The SAP instance number of the application.
Type: String
Pattern: `[0-9]{2}`
Required: No

 ** [Sid](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-Sid"></a>
The System ID of the application.
Type: String
Pattern: `[A-Z][A-Z0-9]{2}`
Required: No

 ** [Tags](#API_RegisterApplication_RequestSyntax) **   <a name="ssmsap-RegisterApplication-request-Tags"></a>
The tags to be attached to the SAP application.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_RegisterApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Application": {
      "AppRegistryArn": "string",
      "Arn": "string",
      "AssociatedApplicationArns": [ "string" ],
      "Components": [ "string" ],
      "DiscoveryStatus": "string",
      "Id": "string",
      "LastUpdated": number,
      "Status": "string",
      "StatusMessage": "string",
      "Type": "string"
   },
   "OperationId": "string"
}
```

## Response Elements
<a name="API_RegisterApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Application](#API_RegisterApplication_ResponseSyntax) **   <a name="ssmsap-RegisterApplication-response-Application"></a>
The application registered with AWS Systems Manager for SAP.
Type: [Application](API_Application.md) object

 ** [OperationId](#API_RegisterApplication_ResponseSyntax) **   <a name="ssmsap-RegisterApplication-response-OperationId"></a>
The ID of the operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`

## Errors
<a name="API_RegisterApplication_Errors"></a>

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
<a name="API_RegisterApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/RegisterApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/RegisterApplication)
