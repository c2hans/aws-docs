---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ListMemberships.html
---

# ListMemberships
<a name="API_ListMemberships"></a>

Returns a paginated list of membership summaries for the specified agent space within an application.

## Request Syntax
<a name="API_ListMemberships_RequestSyntax"></a>

```
POST /ListMemberships HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "applicationId": "{{string}}",
   "maxResults": {{number}},
   "memberType": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMemberships_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMemberships_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_ListMemberships_RequestSyntax) **   <a name="securityagent-ListMemberships-request-agentSpaceId"></a>
The unique identifier of the agent space to list memberships for.
Type: String
Required: Yes

 ** [applicationId](#API_ListMemberships_RequestSyntax) **   <a name="securityagent-ListMemberships-request-applicationId"></a>
The unique identifier of the application that contains the agent space.
Type: String
Required: Yes

 ** [maxResults](#API_ListMemberships_RequestSyntax) **   <a name="securityagent-ListMemberships-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [memberType](#API_ListMemberships_RequestSyntax) **   <a name="securityagent-ListMemberships-request-memberType"></a>
Filter memberships by member type.
Type: String
Valid Values: `USER | ALL`
Required: No

 ** [nextToken](#API_ListMemberships_RequestSyntax) **   <a name="securityagent-ListMemberships-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListMemberships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "membershipSummaries": [
      {
         "agentSpaceId": "string",
         "applicationId": "string",
         "config": { ... },
         "createdAt": "string",
         "createdBy": "string",
         "membershipId": "string",
         "memberType": "string",
         "metadata": { ... },
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemberships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [membershipSummaries](#API_ListMemberships_ResponseSyntax) **   <a name="securityagent-ListMemberships-response-membershipSummaries"></a>
The list of membership summaries.
Type: Array of [MembershipSummary](API_MembershipSummary.md) objects

 ** [nextToken](#API_ListMemberships_ResponseSyntax) **   <a name="securityagent-ListMemberships-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.
Type: String

## Errors
<a name="API_ListMemberships_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListMemberships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/ListMemberships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ListMemberships)
