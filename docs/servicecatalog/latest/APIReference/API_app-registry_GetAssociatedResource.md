---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetAssociatedResource.html
---

# GetAssociatedResource
<a name="API_app-registry_GetAssociatedResource"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Gets the resource associated with the application.

## Request Syntax
<a name="API_app-registry_GetAssociatedResource_RequestSyntax"></a>

```
GET /applications/{{application}}/resources/{{resourceType}}/{{resource}}?maxResults={{maxResults}}&nextToken={{nextToken}}&resourceTagStatus={{resourceTagStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_GetAssociatedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [maxResults](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-maxResults"></a>
 The maximum number of results to return. If the parameter is omitted, it defaults to 25. The value is optional.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-nextToken"></a>
 A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`

 ** [resource](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-resource"></a>
The name or ID of the resource associated with the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [resourceTagStatus](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-resourceTagStatus"></a>
 States whether an application tag is applied, not applied, in the process of being applied, or skipped.
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SUCCESS | FAILED | IN_PROGRESS | SKIPPED`

 ** [resourceType](#API_app-registry_GetAssociatedResource_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-request-uri-resourceType"></a>
The type of resource associated with the application.
Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`
Required: Yes

## Request Body
<a name="API_app-registry_GetAssociatedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_GetAssociatedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationTagResult": {
      "applicationTagStatus": "string",
      "errorMessage": "string",
      "nextToken": "string",
      "resources": [
         {
            "errorMessage": "string",
            "resourceArn": "string",
            "resourceType": "string",
            "status": "string"
         }
      ]
   },
   "options": [ "string" ],
   "resource": {
      "arn": "string",
      "associationTime": "string",
      "integrations": {
         "resourceGroup": {
            "arn": "string",
            "errorMessage": "string",
            "state": "string"
         }
      },
      "name": "string"
   }
}
```

## Response Elements
<a name="API_app-registry_GetAssociatedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationTagResult](#API_app-registry_GetAssociatedResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-response-applicationTagResult"></a>
 The result of the application that's tag applied to a resource.
Type: [ApplicationTagResult](API_app-registry_ApplicationTagResult.md) object

 ** [options](#API_app-registry_GetAssociatedResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-response-options"></a>
 Determines whether an application tag is applied or skipped.
Type: Array of strings
Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

 ** [resource](#API_app-registry_GetAssociatedResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAssociatedResource-response-resource"></a>
The resource associated with the application.
Type: [Resource](API_app-registry_Resource.md) object

## Errors
<a name="API_app-registry_GetAssociatedResource_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_GetAssociatedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/GetAssociatedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
