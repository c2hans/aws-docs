---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetEnvironmentBlueprintConfiguration.html
---

# GetEnvironmentBlueprintConfiguration
<a name="API_GetEnvironmentBlueprintConfiguration"></a>

Gets the blueprint configuration in Amazon DataZone.

## Request Syntax
<a name="API_GetEnvironmentBlueprintConfiguration_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environment-blueprint-configurations/{{environmentBlueprintIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironmentBlueprintConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where this blueprint exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentBlueprintIdentifier](#API_GetEnvironmentBlueprintConfiguration_RequestSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-request-uri-environmentBlueprintIdentifier"></a>
He ID of the blueprint.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetEnvironmentBlueprintConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironmentBlueprintConfiguration_ResponseSyntax"></a>

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
<a name="API_GetEnvironmentBlueprintConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowUserProvidedConfigurations](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-allowUserProvidedConfigurations"></a>
Specifies whether user-provided resource configurations are allowed for the environment blueprint.
Type: Boolean

 ** [createdAt](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-createdAt"></a>
The timestamp of when this blueprint was created.
Type: Timestamp

 ** [domainId](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-domainId"></a>
The ID of the Amazon DataZone domain where this blueprint exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enabledRegions](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-enabledRegions"></a>
The AWS regions in which this blueprint is enabled.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`

 ** [environmentBlueprintId](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-environmentBlueprintId"></a>
The ID of the blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentRolePermissionBoundary](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-environmentRolePermissionBoundary"></a>
The environment role permissions boundary.
Type: String
Pattern: `arn:aws[^:]*:iam::(aws|\d{12}):policy/[\w+=,.@-]*`

 ** [manageAccessRoleArn](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-manageAccessRoleArn"></a>
The ARN of the manage access role with which this blueprint is created.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [provisioningConfigurations](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-provisioningConfigurations"></a>
The provisioning configuration of a blueprint.
Type: Array of [ProvisioningConfiguration](API_ProvisioningConfiguration.md) objects

 ** [provisioningRoleArn](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-provisioningRoleArn"></a>
The ARN of the provisioning role with which this blueprint is created.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [regionalParameters](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-regionalParameters"></a>
The regional parameters of the blueprint.
Type: String to string to string map map
Key Length Constraints: Minimum length of 4. Maximum length of 16.
Key Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`

 ** [resourceConfigurations](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-resourceConfigurations"></a>
The resource configurations of the environment blueprint.
Type: Array of [ResourceConfiguration](API_ResourceConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [updatedAt](#API_GetEnvironmentBlueprintConfiguration_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprintConfiguration-response-updatedAt"></a>
The timestamp of when this blueprint was upated.
Type: Timestamp

## Errors
<a name="API_GetEnvironmentBlueprintConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetEnvironmentBlueprintConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetEnvironmentBlueprintConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
