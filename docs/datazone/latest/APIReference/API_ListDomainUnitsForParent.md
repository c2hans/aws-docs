---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDomainUnitsForParent.html
---

# ListDomainUnitsForParent
<a name="API_ListDomainUnitsForParent"></a>

Lists child domain units for the specified parent domain unit.

## Request Syntax
<a name="API_ListDomainUnitsForParent_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/domain-units?maxResults={{maxResults}}&nextToken={{nextToken}}&parentDomainUnitIdentifier={{parentDomainUnitIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainUnitsForParent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListDomainUnitsForParent_RequestSyntax) **   <a name="datazone-ListDomainUnitsForParent-request-uri-domainIdentifier"></a>
The ID of the domain in which you want to list domain units for a parent domain unit.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListDomainUnitsForParent_RequestSyntax) **   <a name="datazone-ListDomainUnitsForParent-request-uri-maxResults"></a>
The maximum number of domain units to return in a single call to ListDomainUnitsForParent. When the number of domain units to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListDomainUnitsForParent_RequestSyntax) **   <a name="datazone-ListDomainUnitsForParent-request-uri-nextToken"></a>
When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [parentDomainUnitIdentifier](#API_ListDomainUnitsForParent_RequestSyntax) **   <a name="datazone-ListDomainUnitsForParent-request-uri-parentDomainUnitIdentifier"></a>
The ID of the parent domain unit.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: Yes

## Request Body
<a name="API_ListDomainUnitsForParent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainUnitsForParent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDomainUnitsForParent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDomainUnitsForParent_ResponseSyntax) **   <a name="datazone-ListDomainUnitsForParent-response-items"></a>
The results returned by this action.
Type: Array of [DomainUnitSummary](API_DomainUnitSummary.md) objects

 ** [nextToken](#API_ListDomainUnitsForParent_ResponseSyntax) **   <a name="datazone-ListDomainUnitsForParent-response-nextToken"></a>
When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDomainUnitsForParent_Errors"></a>

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
<a name="API_ListDomainUnitsForParent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDomainUnitsForParent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDomainUnitsForParent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
