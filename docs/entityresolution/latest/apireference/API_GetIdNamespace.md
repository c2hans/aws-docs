---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdNamespace.html
---

# GetIdNamespace
<a name="API_GetIdNamespace"></a>

Returns the `IdNamespace` with a given name, if it exists.

## Request Syntax
<a name="API_GetIdNamespace_RequestSyntax"></a>

```
GET /idnamespaces/{{idNamespaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIdNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [idNamespaceName](#API_GetIdNamespace_RequestSyntax) **   <a name="API-GetIdNamespace-request-uri-idNamespaceName"></a>
The name of the ID namespace.
Pattern: `[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## Request Body
<a name="API_GetIdNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIdNamespace_ResponseSyntax"></a>

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
<a name="API_GetIdNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-createdAt"></a>
The timestamp of when the ID namespace was created.
Type: Timestamp

 ** [description](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-description"></a>
The description of the ID namespace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [idMappingWorkflowProperties](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-idMappingWorkflowProperties"></a>
Determines the properties of `IdMappingWorkflow` where this `IdNamespace` can be used as a `Source` or a `Target`.
Type: Array of [IdNamespaceIdMappingWorkflowProperties](API_IdNamespaceIdMappingWorkflowProperties.md) objects
Array Members: Fixed number of 1 item.

 ** [idNamespaceArn](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-idNamespaceArn"></a>
The Amazon Resource Name (ARN) of the ID namespace.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})`

 ** [idNamespaceName](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-idNamespaceName"></a>
The name of the ID namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

 ** [inputSourceConfig](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdNamespaceInputSource](API_IdNamespaceInputSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [roleArn](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access the resources defined in this `IdNamespace` on your behalf as part of a workflow run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [tags](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [type](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` to which all `sourceIds` will resolve to.
Type: String
Valid Values: `SOURCE | TARGET`

 ** [updatedAt](#API_GetIdNamespace_ResponseSyntax) **   <a name="API-GetIdNamespace-response-updatedAt"></a>
The timestamp of when the ID namespace was last updated.
Type: Timestamp

## Errors
<a name="API_GetIdNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_GetIdNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetIdNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetIdNamespace)
