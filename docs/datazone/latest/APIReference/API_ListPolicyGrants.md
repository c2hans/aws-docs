---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListPolicyGrants.html
---

# ListPolicyGrants
<a name="API_ListPolicyGrants"></a>

Lists policy grants.

## Request Syntax
<a name="API_ListPolicyGrants_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/policies/managed/{{entityType}}/{{entityIdentifier}}/grants?maxResults={{maxResults}}&nextToken={{nextToken}}&policyType={{policyType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicyGrants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list policy grants.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-entityIdentifier"></a>
The ID of the entity for which you want to list policy grants.
Required: Yes

 ** [entityType](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-entityType"></a>
The type of entity for which you want to list policy grants.
Valid Values: `DOMAIN_UNIT | ENVIRONMENT_BLUEPRINT_CONFIGURATION | ENVIRONMENT_PROFILE | ASSET_TYPE`
Required: Yes

 ** [maxResults](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-maxResults"></a>
The maximum number of grants to return in a single call to `ListPolicyGrants`. When the number of grants to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListPolicyGrants` to list the next set of grants.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-nextToken"></a>
When the number of grants is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of grants, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListPolicyGrants` to list the next set of grants.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [policyType](#API_ListPolicyGrants_RequestSyntax) **   <a name="datazone-ListPolicyGrants-request-uri-policyType"></a>
The type of policy that you want to list.
Valid Values: `CREATE_DOMAIN_UNIT | OVERRIDE_DOMAIN_UNIT_OWNERS | ADD_TO_PROJECT_MEMBER_POOL | OVERRIDE_PROJECT_OWNERS | CREATE_GLOSSARY | CREATE_FORM_TYPE | CREATE_ASSET_TYPE | CREATE_PROJECT | CREATE_ENVIRONMENT_PROFILE | DELEGATE_CREATE_ENVIRONMENT_PROFILE | CREATE_ENVIRONMENT | CREATE_ENVIRONMENT_FROM_BLUEPRINT | CREATE_PROJECT_FROM_PROJECT_PROFILE | USE_ASSET_TYPE`
Required: Yes

## Request Body
<a name="API_ListPolicyGrants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyGrants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "grantList": [
      {
         "createdAt": number,
         "createdBy": "string",
         "detail": { ... },
         "grantId": "string",
         "principal": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPolicyGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [grantList](#API_ListPolicyGrants_ResponseSyntax) **   <a name="datazone-ListPolicyGrants-response-grantList"></a>
The results of this action - the listed grants.
Type: Array of [PolicyGrantMember](API_PolicyGrantMember.md) objects

 ** [nextToken](#API_ListPolicyGrants_ResponseSyntax) **   <a name="datazone-ListPolicyGrants-response-nextToken"></a>
When the number of grants is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of grants, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListPolicyGrants` to list the next set of grants.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListPolicyGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

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
<a name="API_ListPolicyGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListPolicyGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListPolicyGrants)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
