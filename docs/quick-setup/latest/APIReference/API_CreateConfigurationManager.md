---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_CreateConfigurationManager.html
---

# CreateConfigurationManager
<a name="API_CreateConfigurationManager"></a>

Creates a Quick Setup configuration manager resource. This object is a collection of desired state configurations for multiple configuration definitions and summaries describing the deployments of those definitions.

## Request Syntax
<a name="API_CreateConfigurationManager_RequestSyntax"></a>

```
POST /configurationManager HTTP/1.1
Content-type: application/json

{
   "ConfigurationDefinitions": [
      {
         "LocalDeploymentAdministrationRoleArn": "{{string}}",
         "LocalDeploymentExecutionRoleName": "{{string}}",
         "Parameters": {
            "{{string}}" : "{{string}}"
         },
         "Type": "{{string}}",
         "TypeVersion": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfigurationManager_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfigurationManager_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationDefinitions](#API_CreateConfigurationManager_RequestSyntax) **   <a name="quicksetup-CreateConfigurationManager-request-ConfigurationDefinitions"></a>
The definition of the Quick Setup configuration that the configuration manager deploys.
Type: Array of [ConfigurationDefinitionInput](API_ConfigurationDefinitionInput.md) objects
Required: Yes

 ** [Description](#API_CreateConfigurationManager_RequestSyntax) **   <a name="quicksetup-CreateConfigurationManager-request-Description"></a>
A description of the configuration manager.
Type: String
Pattern: `.{0,512}`
Required: No

 ** [Name](#API_CreateConfigurationManager_RequestSyntax) **   <a name="quicksetup-CreateConfigurationManager-request-Name"></a>
A name for the configuration manager.
Type: String
Pattern: `[ A-Za-z0-9._-]{0,120}`
Required: No

 ** [Tags](#API_CreateConfigurationManager_RequestSyntax) **   <a name="quicksetup-CreateConfigurationManager-request-Tags"></a>
Key-value pairs of metadata to assign to the configuration manager.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Required: No

## Response Syntax
<a name="API_CreateConfigurationManager_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ManagerArn": "string"
}
```

## Response Elements
<a name="API_CreateConfigurationManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagerArn](#API_CreateConfigurationManager_ResponseSyntax) **   <a name="quicksetup-CreateConfigurationManager-response-ManagerArn"></a>
The ARN for the newly created configuration manager.
Type: String

## Errors
<a name="API_CreateConfigurationManager_Errors"></a>

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

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_CreateConfigurationManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/CreateConfigurationManager)
