---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListEnvironmentBlueprintConfigurations.html
---

# ListEnvironmentBlueprintConfigurations
<a name="API_ListEnvironmentBlueprintConfigurations"></a>

Lists blueprint configurations for a Amazon DataZone environment.

## Request Syntax
<a name="API_ListEnvironmentBlueprintConfigurations_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environment-blueprint-configurations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironmentBlueprintConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListEnvironmentBlueprintConfigurations_RequestSyntax) **   <a name="datazone-ListEnvironmentBlueprintConfigurations-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListEnvironmentBlueprintConfigurations_RequestSyntax) **   <a name="datazone-ListEnvironmentBlueprintConfigurations-request-uri-maxResults"></a>
The maximum number of blueprint configurations to return in a single call to `ListEnvironmentBlueprintConfigurations`. When the number of configurations to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListEnvironmentBlueprintConfigurations` to list the next set of configurations.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListEnvironmentBlueprintConfigurations_RequestSyntax) **   <a name="datazone-ListEnvironmentBlueprintConfigurations-request-uri-nextToken"></a>
When the number of blueprint configurations is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of configurations, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentBlueprintConfigurations` to list the next set of configurations.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListEnvironmentBlueprintConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironmentBlueprintConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentBlueprintConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListEnvironmentBlueprintConfigurations_ResponseSyntax) **   <a name="datazone-ListEnvironmentBlueprintConfigurations-response-items"></a>
The results of the `ListEnvironmentBlueprintConfigurations` action.
Type: Array of [EnvironmentBlueprintConfigurationItem](API_EnvironmentBlueprintConfigurationItem.md) objects

 ** [nextToken](#API_ListEnvironmentBlueprintConfigurations_ResponseSyntax) **   <a name="datazone-ListEnvironmentBlueprintConfigurations-response-nextToken"></a>
When the number of blueprint configurations is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of configurations, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentBlueprintConfigurations` to list the next set of configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListEnvironmentBlueprintConfigurations_Errors"></a>

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
<a name="API_ListEnvironmentBlueprintConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListEnvironmentBlueprintConfigurations)
