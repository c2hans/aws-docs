---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListFirewallDomainLists.html
---

# ListFirewallDomainLists
<a name="API_route53globalresolver_ListFirewallDomainLists"></a>

Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_ListFirewallDomainLists_RequestSyntax"></a>

```
GET /firewall-domain-lists?global_resolver_id={{globalResolverId}}&max_results={{maxResults}}&next_token={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_ListFirewallDomainLists_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalResolverId](#API_route53globalresolver_ListFirewallDomainLists_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListFirewallDomainLists-request-uri-globalResolverId"></a>
The ID of the Global Resolver that contains the DNS view the domain lists are associated to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [maxResults](#API_route53globalresolver_ListFirewallDomainLists_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListFirewallDomainLists-request-uri-maxResults"></a>
The maximum number of results to retrieve in a single call.

 ** [nextToken](#API_route53globalresolver_ListFirewallDomainLists_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListFirewallDomainLists-request-uri-nextToken"></a>
A pagination token used for large sets of results that can't be returned in a single response.

## Request Body
<a name="API_route53globalresolver_ListFirewallDomainLists_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_ListFirewallDomainLists_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "firewallDomainLists": [
      {
         "arn": "string",
         "createdAt": "string",
         "description": "string",
         "globalResolverId": "string",
         "id": "string",
         "name": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_ListFirewallDomainLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [firewallDomainLists](#API_route53globalresolver_ListFirewallDomainLists_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListFirewallDomainLists-response-firewallDomainLists"></a>
List of the DNS Firewall domain lists.
Type: Array of [FirewallDomainListsItem](API_route53globalresolver_FirewallDomainListsItem.md) objects

 ** [nextToken](#API_route53globalresolver_ListFirewallDomainLists_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListFirewallDomainLists-response-nextToken"></a>
A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.
Type: String

## Errors
<a name="API_route53globalresolver_ListFirewallDomainLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify the resource ID and try again.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Wait a moment and try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are invalid. Check the parameter values and try again.
 ** fieldList **
The list of fields that aren't valid.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_route53globalresolver_ListFirewallDomainLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/ListFirewallDomainLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/ListFirewallDomainLists)
