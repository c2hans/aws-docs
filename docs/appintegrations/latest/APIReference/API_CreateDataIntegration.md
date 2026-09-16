---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html
---

# CreateDataIntegration
<a name="API_connect-app-integrations_CreateDataIntegration"></a>

Creates and persists a DataIntegration resource.

**Note**
You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the `CreateDataIntegration` API.

## Request Syntax
<a name="API_connect-app-integrations_CreateDataIntegration_RequestSyntax"></a>

```
POST /dataIntegrations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "FileConfiguration": {
      "Filters": {
         "{{string}}" : [ "{{string}}" ]
      },
      "Folders": [ "{{string}}" ]
   },
   "KmsKey": "{{string}}",
   "Name": "{{string}}",
   "ObjectConfiguration": {
      "{{string}}" : {
         "{{string}}" : [ "{{string}}" ]
      }
   },
   "ScheduleConfig": {
      "FirstExecutionFrom": "{{string}}",
      "Object": "{{string}}",
      "ScheduleExpression": "{{string}}"
   },
   "SourceURI": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_CreateDataIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-app-integrations_CreateDataIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [Description](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-Description"></a>
A description of the DataIntegration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** [FileConfiguration](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-FileConfiguration"></a>
The configuration for what files should be pulled from the source.
Type: [FileConfiguration](API_connect-app-integrations_FileConfiguration.md) object
Required: No

 ** [KmsKey](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-KmsKey"></a>
The KMS key ARN for the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

 ** [Name](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-Name"></a>
The name of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

 ** [ObjectConfiguration](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-ObjectConfiguration"></a>
The configuration for what data should be pulled from the source.
Type: String to string to array of strings map map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

 ** [ScheduleConfig](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-ScheduleConfig"></a>
The name of the data and how often it should be pulled from the source.
Type: [ScheduleConfiguration](API_connect-app-integrations_ScheduleConfiguration.md) object
Required: No

 ** [SourceURI](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-SourceURI"></a>
The URI of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
Required: No

 ** [Tags](#API_connect-app-integrations_CreateDataIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-app-integrations_CreateDataIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ClientToken": "string",
   "Description": "string",
   "FileConfiguration": {
      "Filters": {
         "string" : [ "string" ]
      },
      "Folders": [ "string" ]
   },
   "Id": "string",
   "KmsKey": "string",
   "Name": "string",
   "ObjectConfiguration": {
      "string" : {
         "string" : [ "string" ]
      }
   },
   "ScheduleConfiguration": {
      "FirstExecutionFrom": "string",
      "Object": "string",
      "ScheduleExpression": "string"
   },
   "SourceURI": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-app-integrations_CreateDataIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-Arn"></a>
The Amazon Resource Name (ARN)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [ClientToken](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`

 ** [Description](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-Description"></a>
A description of the DataIntegration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`

 ** [FileConfiguration](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-FileConfiguration"></a>
The configuration for what files should be pulled from the source.
Type: [FileConfiguration](API_connect-app-integrations_FileConfiguration.md) object

 ** [Id](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-Id"></a>
A unique identifier.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [KmsKey](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-KmsKey"></a>
The KMS key ARN for the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`

 ** [Name](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-Name"></a>
The name of the DataIntegration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`

 ** [ObjectConfiguration](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-ObjectConfiguration"></a>
The configuration for what data should be pulled from the source.
Type: String to string to array of strings map map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `.*\S.*`
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`

 ** [ScheduleConfiguration](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-ScheduleConfiguration"></a>
The name of the data and how often it should be pulled from the source.
Type: [ScheduleConfiguration](API_connect-app-integrations_ScheduleConfiguration.md) object

 ** [SourceURI](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-SourceURI"></a>
The URI of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`

 ** [Tags](#API_connect-app-integrations_CreateDataIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateDataIntegration-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-app-integrations_CreateDataIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceQuotaExceededException **
The allowed quota for the resource has been exceeded.
HTTP Status Code: 429

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_CreateDataIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/CreateDataIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/CreateDataIntegration)
