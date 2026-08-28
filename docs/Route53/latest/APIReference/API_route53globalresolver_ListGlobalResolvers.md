---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ListGlobalResolvers.html
---

# ListGlobalResolvers
<a name="API_route53globalresolver_ListGlobalResolvers"></a>

Lists all Route 53 Global Resolver instances in your account with pagination support.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_ListGlobalResolvers_RequestSyntax"></a>

```
GET /global-resolver?max_results={{maxResults}}&next_token={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_ListGlobalResolvers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_route53globalresolver_ListGlobalResolvers_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListGlobalResolvers-request-uri-maxResults"></a>
The maximum number of Route 53 Global Resolver instances to return in the response. Valid range is 1-100.

 ** [nextToken](#API_route53globalresolver_ListGlobalResolvers_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListGlobalResolvers-request-uri-nextToken"></a>
The token for the next page of results. This value is returned in the response if there are more results to retrieve.

## Request Body
<a name="API_route53globalresolver_ListGlobalResolvers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_ListGlobalResolvers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "globalResolvers": [
      {
         "arn": "string",
         "clientToken": "string",
         "createdAt": "string",
         "description": "string",
         "dnsName": "string",
         "id": "string",
         "ipAddressType": "string",
         "ipv4Addresses": [ "string" ],
         "ipv6Addresses": [ "string" ],
         "name": "string",
         "observabilityRegion": "string",
         "regions": [ "string" ],
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_ListGlobalResolvers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [globalResolvers](#API_route53globalresolver_ListGlobalResolvers_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListGlobalResolvers-response-globalResolvers"></a>
Paginated list of Global Resolvers.
Type: Array of [GlobalResolversItem](API_route53globalresolver_GlobalResolversItem.md) objects

 ** [nextToken](#API_route53globalresolver_ListGlobalResolvers_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_ListGlobalResolvers-response-nextToken"></a>
A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.
Type: String

## Errors
<a name="API_route53globalresolver_ListGlobalResolvers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

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
<a name="API_route53globalresolver_ListGlobalResolvers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/ListGlobalResolvers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/ListGlobalResolvers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
