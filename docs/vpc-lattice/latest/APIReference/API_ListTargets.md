---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListTargets.html
---

# ListTargets
<a name="API_ListTargets"></a>

Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target.

## Request Syntax
<a name="API_ListTargets_RequestSyntax"></a>

```
POST /targetgroups/{{targetGroupIdentifier}}/listtargets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "targets": [
      {
         "id": "{{string}}",
         "port": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_ListTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTargets_RequestSyntax) **   <a name="vpclattice-ListTargets-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTargets_RequestSyntax) **   <a name="vpclattice-ListTargets-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [targetGroupIdentifier](#API_ListTargets_RequestSyntax) **   <a name="vpclattice-ListTargets-request-uri-targetGroupIdentifier"></a>
The ID or ARN of the target group.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_ListTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targets](#API_ListTargets_RequestSyntax) **   <a name="vpclattice-ListTargets-request-targets"></a>
The targets.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_ListTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "id": "string",
         "port": number,
         "reasonCode": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListTargets_ResponseSyntax) **   <a name="vpclattice-ListTargets-response-items"></a>
Information about the targets.
Type: Array of [TargetSummary](API_TargetSummary.md) objects

 ** [nextToken](#API_ListTargets_ResponseSyntax) **   <a name="vpclattice-ListTargets-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_ListTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
