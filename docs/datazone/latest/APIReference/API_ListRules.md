---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListRules.html
---

# ListRules
<a name="API_ListRules"></a>

Lists existing rules. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.

## Request Syntax
<a name="API_ListRules_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/list-rules/{{targetType}}/{{targetIdentifier}}?assetTypes={{assetTypes}}&dataProduct={{dataProduct}}&includeCascaded={{includeCascaded}}&maxResults={{maxResults}}&nextToken={{nextToken}}&projectIds={{projectIds}}&ruleAction={{action}}&ruleType={{ruleType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [action](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-action"></a>
The action of the rule.
Valid Values: `CREATE_LISTING_CHANGE_SET | CREATE_SUBSCRIPTION_REQUEST`

 ** [assetTypes](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-assetTypes"></a>
The asset types of the rule.
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`

 ** [dataProduct](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-dataProduct"></a>
The data product of the rule.

 ** [domainIdentifier](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-domainIdentifier"></a>
The ID of the domain in which the rules are to be listed.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [includeCascaded](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-includeCascaded"></a>
Specifies whether to include cascading rules in the results.

 ** [maxResults](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-maxResults"></a>
The maximum number of rules to return in a single call to `ListRules`. When the number of rules to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListRules` to list the next set of rules.
Valid Range: Minimum value of 25. Maximum value of 50.

 ** [nextToken](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-nextToken"></a>
When the number of rules is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of rules, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListRules` to list the next set of rules.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIds](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-projectIds"></a>
The IDs of projects in which rules are to be listed.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [ruleType](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-ruleType"></a>
The type of the rule.
Valid Values: `METADATA_FORM_ENFORCEMENT | GLOSSARY_TERM_ENFORCEMENT`

 ** [targetIdentifier](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-targetIdentifier"></a>
The target ID of the rule.
Required: Yes

 ** [targetType](#API_ListRules_RequestSyntax) **   <a name="datazone-ListRules-request-uri-targetType"></a>
The target type of the rule.
Valid Values: `DOMAIN_UNIT`
Required: Yes

## Request Body
<a name="API_ListRules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "action": "string",
         "identifier": "string",
         "lastUpdatedBy": "string",
         "name": "string",
         "revision": "string",
         "ruleType": "string",
         "scope": {
            "assetType": {
               "selectionMode": "string",
               "specificAssetTypes": [ "string" ]
            },
            "dataProduct": boolean,
            "project": {
               "selectionMode": "string",
               "specificProjects": [ "string" ]
            }
         },
         "target": { ... },
         "targetType": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListRules_ResponseSyntax) **   <a name="datazone-ListRules-response-items"></a>
The results of the `ListRules` action.
Type: Array of [RuleSummary](API_RuleSummary.md) objects

 ** [nextToken](#API_ListRules_ResponseSyntax) **   <a name="datazone-ListRules-response-nextToken"></a>
When the number of rules is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of rules, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListRules` to list the next set of rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListRules_Errors"></a>

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
<a name="API_ListRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListRules)
