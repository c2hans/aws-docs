---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAssociatedResources.html
---

# ListAssociatedResources
<a name="API_app-registry_ListAssociatedResources"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Lists all of the resources that are associated with the specified application. Results are paginated.

**Note**
 If you share an application, and a consumer account associates a tag query to the application, all of the users who can access the application can also view the tag values in all accounts that are associated with it using this API.

## Request Syntax
<a name="API_app-registry_ListAssociatedResources_RequestSyntax"></a>

```
GET /applications/{{application}}/resources?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_ListAssociatedResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_ListAssociatedResources_RequestSyntax) **   <a name="servicecatalog-app-registry_ListAssociatedResources-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [maxResults](#API_app-registry_ListAssociatedResources_RequestSyntax) **   <a name="servicecatalog-app-registry_ListAssociatedResources-request-uri-maxResults"></a>
The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_app-registry_ListAssociatedResources_RequestSyntax) **   <a name="servicecatalog-app-registry_ListAssociatedResources-request-uri-nextToken"></a>
The token to use to get the next page of results after a previous API call.
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`

## Request Body
<a name="API_app-registry_ListAssociatedResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_ListAssociatedResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resources": [
      {
         "arn": "string",
         "name": "string",
         "options": [ "string" ],
         "resourceDetails": {
            "tagValue": "string"
         },
         "resourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_app-registry_ListAssociatedResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_app-registry_ListAssociatedResources_ResponseSyntax) **   <a name="servicecatalog-app-registry_ListAssociatedResources-response-nextToken"></a>
The token to use to get the next page of results after a previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`

 ** [resources](#API_app-registry_ListAssociatedResources_ResponseSyntax) **   <a name="servicecatalog-app-registry_ListAssociatedResources-response-resources"></a>
Information about the resources.
Type: Array of [ResourceInfo](API_app-registry_ResourceInfo.md) objects

## Errors
<a name="API_app-registry_ListAssociatedResources_Errors"></a>

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
<a name="API_app-registry_ListAssociatedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources)
