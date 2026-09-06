---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfigurationManager.html
---

# GetConfigurationManager
<a name="API_GetConfigurationManager"></a>

Returns a configuration manager.

## Request Syntax
<a name="API_GetConfigurationManager_RequestSyntax"></a>

```
GET /configurationManager/{{ManagerArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfigurationManager_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ManagerArn](#API_GetConfigurationManager_RequestSyntax) **   <a name="quicksetup-GetConfigurationManager-request-uri-ManagerArn"></a>
The ARN of the configuration manager.
Length Constraints: Minimum length of 1.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: Yes

## Request Body
<a name="API_GetConfigurationManager_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfigurationManager_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationDefinitions": [
      {
         "Id": "string",
         "LocalDeploymentAdministrationRoleArn": "string",
         "LocalDeploymentExecutionRoleName": "string",
         "Parameters": {
            "string" : "string"
         },
         "Type": "string",
         "TypeVersion": "string"
      }
   ],
   "CreatedAt": "string",
   "Description": "string",
   "LastModifiedAt": "string",
   "ManagerArn": "string",
   "Name": "string",
   "StatusSummaries": [
      {
         "LastUpdatedAt": "string",
         "Status": "string",
         "StatusDetails": {
            "string" : "string"
         },
         "StatusMessage": "string",
         "StatusType": "string"
      }
   ],
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetConfigurationManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationDefinitions](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-ConfigurationDefinitions"></a>
The configuration definitions association with the configuration manager.
Type: Array of [ConfigurationDefinition](API_ConfigurationDefinition.md) objects

 ** [CreatedAt](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-CreatedAt"></a>
The datetime stamp when the configuration manager was created.
Type: Timestamp

 ** [Description](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-Description"></a>
The description of the configuration manager.
Type: String

 ** [LastModifiedAt](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-LastModifiedAt"></a>
The datetime stamp when the configuration manager was last updated.
Type: Timestamp

 ** [ManagerArn](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-ManagerArn"></a>
The ARN of the configuration manager.
Type: String

 ** [Name](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-Name"></a>
The name of the configuration manager.
Type: String

 ** [StatusSummaries](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-StatusSummaries"></a>
A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.
Type: Array of [StatusSummary](API_StatusSummary.md) objects

 ** [Tags](#API_GetConfigurationManager_ResponseSyntax) **   <a name="quicksetup-GetConfigurationManager-response-Tags"></a>
Key-value pairs of metadata to assign to the configuration manager.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]+`

## Errors
<a name="API_GetConfigurationManager_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found. Check the ID or name and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_GetConfigurationManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/GetConfigurationManager)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/GetConfigurationManager)
