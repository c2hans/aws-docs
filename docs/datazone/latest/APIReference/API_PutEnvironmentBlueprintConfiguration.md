---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PutEnvironmentBlueprintConfiguration.html
---

# PutEnvironmentBlueprintConfiguration
<a name="API_PutEnvironmentBlueprintConfiguration"></a>

Writes the configuration for the specified environment blueprint in Amazon DataZone.

## Request Syntax
<a name="API_PutEnvironmentBlueprintConfiguration_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/environment-blueprint-configurations/{{environmentBlueprintIdentifier}} HTTP/1.1
Content-type: application/json

{
   "allowUserProvidedConfigurations": {{boolean}},
   "enabledRegions": [ "{{string}}" ],
   "environmentRolePermissionBoundary": "{{string}}",
   "globalParameters": {
      "{{string}}" : "{{string}}"
   },
   "manageAccessRoleArn": "{{string}}",
   "provisioningConfigurations": [
      { ... }
   ],
   "provisioningRoleArn": "{{string}}",
   "regionalParameters": {
      "{{string}}" : {
         "{{string}}" : "{{string}}"
      }
   },
   "resourceConfigurations": [
      {
         "description": "{{string}}",
         "name": "{{string}}",
         "parameters": {
            "{{string}}" : "{{string}}"
         },
         "region": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutEnvironmentBlueprintConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentBlueprintIdentifier](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-uri-environmentBlueprintIdentifier"></a>
The identifier of the environment blueprint.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_PutEnvironmentBlueprintConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowUserProvidedConfigurations](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-allowUserProvidedConfigurations"></a>
Specifies whether user-provided resource configurations are allowed for the environment blueprint.
Type: Boolean
Required: No

 ** [enabledRegions](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-enabledRegions"></a>
Specifies the enabled AWS Regions.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: Yes

 ** [environmentRolePermissionBoundary](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-environmentRolePermissionBoundary"></a>
The environment role permissions boundary.
Type: String
Pattern: `arn:aws[^:]*:iam::(aws|\d{12}):policy/[\w+=,.@-]*`
Required: No

 ** [globalParameters](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-globalParameters"></a>
Region-agnostic environment blueprint parameters.
Type: String to string map
Required: No

 ** [manageAccessRoleArn](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-manageAccessRoleArn"></a>
The ARN of the manage access role.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [provisioningConfigurations](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-provisioningConfigurations"></a>
The provisioning configuration of a blueprint.
Type: Array of [ProvisioningConfiguration](API_ProvisioningConfiguration.md) objects
Required: No

 ** [provisioningRoleArn](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-provisioningRoleArn"></a>
The ARN of the provisioning role.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [regionalParameters](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-regionalParameters"></a>
The regional parameters in the environment blueprint.
Type: String to string to string map map
Key Length Constraints: Minimum length of 4. Maximum length of 16.
Key Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: No

 ** [resourceConfigurations](#API_PutEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-request-resourceConfigurations"></a>
The resource configurations of the environment blueprint.
Type: Array of [PutResourceConfiguration](API_PutResourceConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_PutEnvironmentBlueprintConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowUserProvidedConfigurations": boolean,
   "createdAt": "string",
   "domainId": "string",
   "enabledRegions": [ "string" ],
   "environmentBlueprintId": "string",
   "environmentRolePermissionBoundary": "string",
   "manageAccessRoleArn": "string",
   "provisioningConfigurations": [
      { ... }
   ],
   "provisioningRoleArn": "string",
   "regionalParameters": {
      "string" : {
         "string" : "string"
      }
   },
   "resourceConfigurations": [
      {
         "description": "string",
         "identifier": "string",
         "name": "string",
         "parameters": {
            "string" : "string"
         },
         "region": "string"
      }
   ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_PutEnvironmentBlueprintConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowUserProvidedConfigurations](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-allowUserProvidedConfigurations"></a>
Specifies whether user-provided resource configurations are allowed for the environment blueprint.
Type: Boolean

 ** [createdAt](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-createdAt"></a>
The timestamp of when the environment blueprint was created.
Type: Timestamp

 ** [domainId](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-domainId"></a>
The identifier of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enabledRegions](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-enabledRegions"></a>
Specifies the enabled AWS Regions.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`

 ** [environmentBlueprintId](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-environmentBlueprintId"></a>
The identifier of the environment blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentRolePermissionBoundary](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-environmentRolePermissionBoundary"></a>
The environment role permissions boundary.
Type: String
Pattern: `arn:aws[^:]*:iam::(aws|\d{12}):policy/[\w+=,.@-]*`

 ** [manageAccessRoleArn](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-manageAccessRoleArn"></a>
The ARN of the manage access role.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [provisioningConfigurations](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-provisioningConfigurations"></a>
The provisioning configuration of a blueprint.
Type: Array of [ProvisioningConfiguration](API_ProvisioningConfiguration.md) objects

 ** [provisioningRoleArn](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-provisioningRoleArn"></a>
The ARN of the provisioning role.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [regionalParameters](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-regionalParameters"></a>
The regional parameters in the environment blueprint.
Type: String to string to string map map
Key Length Constraints: Minimum length of 4. Maximum length of 16.
Key Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`

 ** [resourceConfigurations](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-resourceConfigurations"></a>
The resource configurations of the environment blueprint.
Type: Array of [ResourceConfiguration](API_ResourceConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [updatedAt](#API_PutEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-PutEnvironmentBlueprintConfiguration-response-updatedAt"></a>
The timestamp of when the environment blueprint was updated.
Type: Timestamp

## Errors
<a name="API_PutEnvironmentBlueprintConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_PutEnvironmentBlueprintConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PutEnvironmentBlueprintConfiguration)
