---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdNamespace.html
---

# CreateIdNamespace
<a name="API_CreateIdNamespace"></a>

Creates an ID namespace object which will help customers provide metadata explaining their dataset and how to use it. Each ID namespace must have a unique name. To modify an existing ID namespace, use the UpdateIdNamespace API.

## Request Syntax
<a name="API_CreateIdNamespace_RequestSyntax"></a>

```
POST /idnamespaces HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "idMappingWorkflowProperties": [
      {
         "idMappingType": "{{string}}",
         "providerProperties": {
            "providerConfiguration": {{JSON value}},
            "providerServiceArn": "{{string}}"
         },
         "ruleBasedProperties": {
            "attributeMatchingModel": "{{string}}",
            "recordMatchingModels": [ "{{string}}" ],
            "ruleDefinitionTypes": [ "{{string}}" ],
            "rules": [
               {
                  "matchingKeys": [ "{{string}}" ],
                  "ruleName": "{{string}}"
               }
            ]
         }
      }
   ],
   "idNamespaceName": "{{string}}",
   "inputSourceConfig": [
      {
         "inputSourceARN": "{{string}}",
         "schemaName": "{{string}}"
      }
   ],
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIdNamespace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIdNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-description"></a>
The description of the ID namespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [idMappingWorkflowProperties](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-idMappingWorkflowProperties"></a>
Determines the properties of `IdMappingWorflow` where this `IdNamespace` can be used as a `Source` or a `Target`.
Type: Array of [IdNamespaceIdMappingWorkflowProperties](API_IdNamespaceIdMappingWorkflowProperties.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [idNamespaceName](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-idNamespaceName"></a>
The name of the ID namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** [inputSourceConfig](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdNamespaceInputSource](API_IdNamespaceInputSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [roleArn](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access the resources defined in this `IdNamespace` on your behalf as part of the workflow run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [tags](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [type](#API_CreateIdNamespace_RequestSyntax) **   <a name="API-CreateIdNamespace-request-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` to which all `sourceIds` will resolve to.
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

## Response Syntax
<a name="API_CreateIdNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "idMappingWorkflowProperties": [
      {
         "idMappingType": "string",
         "providerProperties": {
            "providerConfiguration": JSON value,
            "providerServiceArn": "string"
         },
         "ruleBasedProperties": {
            "attributeMatchingModel": "string",
            "recordMatchingModels": [ "string" ],
            "ruleDefinitionTypes": [ "string" ],
            "rules": [
               {
                  "matchingKeys": [ "string" ],
                  "ruleName": "string"
               }
            ]
         }
      }
   ],
   "idNamespaceArn": "string",
   "idNamespaceName": "string",
   "inputSourceConfig": [
      {
         "inputSourceARN": "string",
         "schemaName": "string"
      }
   ],
   "roleArn": "string",
   "tags": {
      "string" : "string"
   },
   "type": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_CreateIdNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-createdAt"></a>
The timestamp of when the ID namespace was created.
Type: Timestamp

 ** [description](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-description"></a>
The description of the ID namespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [idMappingWorkflowProperties](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-idMappingWorkflowProperties"></a>
Determines the properties of `IdMappingWorkflow` where this `IdNamespace` can be used as a `Source` or a `Target`.
Type: Array of [IdNamespaceIdMappingWorkflowProperties](API_IdNamespaceIdMappingWorkflowProperties.md) objects
Array Members: Fixed number of 1 item.

 ** [idNamespaceArn](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-idNamespaceArn"></a>
The Amazon Resource Name (ARN) of the ID namespace.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})`

 ** [idNamespaceName](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-idNamespaceName"></a>
The name of the ID namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

 ** [inputSourceConfig](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdNamespaceInputSource](API_IdNamespaceInputSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [roleArn](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access the resources defined in `inputSourceConfig` on your behalf as part of the workflow run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [tags](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [type](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` to which all `sourceIds` will resolve to.
Type: String
Valid Values: `SOURCE | TARGET`

 ** [updatedAt](#API_CreateIdNamespace_ResponseSyntax) **   <a name="API-CreateIdNamespace-response-updatedAt"></a>
The timestamp of when the ID namespace was last updated.
Type: Timestamp

## Errors
<a name="API_CreateIdNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_CreateIdNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/CreateIdNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/CreateIdNamespace)
