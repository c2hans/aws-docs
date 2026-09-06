---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfiguration.html
---

# GetConfiguration
<a name="API_GetConfiguration"></a>

Returns details about the specified configuration.

## Request Syntax
<a name="API_GetConfiguration_RequestSyntax"></a>

```
GET /getConfiguration/{{ConfigurationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationId](#API_GetConfiguration_RequestSyntax) **   <a name="quicksetup-GetConfiguration-request-uri-ConfigurationId"></a>
A service generated identifier for the configuration.
Pattern: `[a-zA-Z0-9-_/:]{1,100}`
Required: Yes

## Request Body
<a name="API_GetConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Account": "string",
   "ConfigurationDefinitionId": "string",
   "CreatedAt": "string",
   "Id": "string",
   "LastModifiedAt": "string",
   "ManagerArn": "string",
   "Parameters": {
      "string" : "string"
   },
   "Region": "string",
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
   "Type": "string",
   "TypeVersion": "string"
}
```

## Response Elements
<a name="API_GetConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Account](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-Account"></a>
The ID of the AWS account where the configuration was deployed.
Type: String

 ** [ConfigurationDefinitionId](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-ConfigurationDefinitionId"></a>
The ID of the configuration definition.
Type: String

 ** [CreatedAt](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-CreatedAt"></a>
The datetime stamp when the configuration manager was created.
Type: Timestamp

 ** [Id](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-Id"></a>
A service generated identifier for the configuration.
Type: String

 ** [LastModifiedAt](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-LastModifiedAt"></a>
The datetime stamp when the configuration manager was last updated.
Type: Timestamp

 ** [ManagerArn](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-ManagerArn"></a>
The ARN of the configuration manager.
Type: String

 ** [Parameters](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-Parameters"></a>
The parameters for the configuration definition type.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9+=@_\/\s-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 40960.

 ** [Region](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-Region"></a>
The AWS Region where the configuration was deployed.
Type: String

 ** [StatusSummaries](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-StatusSummaries"></a>
A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.
Type: Array of [StatusSummary](API_StatusSummary.md) objects

 ** [Type](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-Type"></a>
The type of the Quick Setup configuration.
Type: String

 ** [TypeVersion](#API_GetConfiguration_ResponseSyntax) **   <a name="quicksetup-GetConfiguration-response-TypeVersion"></a>
The version of the Quick Setup type used.
Type: String

## Errors
<a name="API_GetConfiguration_Errors"></a>

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
<a name="API_GetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/GetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/GetConfiguration)
