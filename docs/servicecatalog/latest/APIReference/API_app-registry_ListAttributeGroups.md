---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAttributeGroups.html
---

# ListAttributeGroups
<a name="API_app-registry_ListAttributeGroups"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Lists all attribute groups which you have access to. Results are paginated.

## Request Syntax
<a name="API_app-registry_ListAttributeGroups_RequestSyntax"></a>

```
GET /attribute-groups?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_ListAttributeGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_app-registry_ListAttributeGroups_RequestSyntax) **   <a name="servicecatalog-app-registry_ListAttributeGroups-request-uri-maxResults"></a>
The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_app-registry_ListAttributeGroups_RequestSyntax) **   <a name="servicecatalog-app-registry_ListAttributeGroups-request-uri-nextToken"></a>
The token to use to get the next page of results after a previous API call.
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`

## Request Body
<a name="API_app-registry_ListAttributeGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_ListAttributeGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributeGroups": [
      {
         "arn": "string",
         "createdBy": "string",
         "creationTime": "string",
         "description": "string",
         "id": "string",
         "lastUpdateTime": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_app-registry_ListAttributeGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributeGroups](#API_app-registry_ListAttributeGroups_ResponseSyntax) **   <a name="servicecatalog-app-registry_ListAttributeGroups-response-attributeGroups"></a>
This list of attribute groups.
Type: Array of [AttributeGroupSummary](API_app-registry_AttributeGroupSummary.md) objects

 ** [nextToken](#API_app-registry_ListAttributeGroups_ResponseSyntax) **   <a name="servicecatalog-app-registry_ListAttributeGroups-response-nextToken"></a>
The token to use to get the next page of results after a previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_app-registry_ListAttributeGroups_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_ListAttributeGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/ListAttributeGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAttributeGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
