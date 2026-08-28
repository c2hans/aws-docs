---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListTargetGroups.html
---

# ListTargetGroups
<a name="API_ListTargetGroups"></a>

Lists your target groups. You can narrow your search by using the filters below in your request.

## Request Syntax
<a name="API_ListTargetGroups_RequestSyntax"></a>

```
GET /targetgroups?maxResults={{maxResults}}&nextToken={{nextToken}}&targetGroupType={{targetGroupType}}&vpcIdentifier={{vpcIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTargetGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTargetGroups_RequestSyntax) **   <a name="vpclattice-ListTargetGroups-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListTargetGroups_RequestSyntax) **   <a name="vpclattice-ListTargetGroups-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [targetGroupType](#API_ListTargetGroups_RequestSyntax) **   <a name="vpclattice-ListTargetGroups-request-uri-targetGroupType"></a>
The target group type.
Valid Values: `IP | LAMBDA | INSTANCE | ALB`

 ** [vpcIdentifier](#API_ListTargetGroups_RequestSyntax) **   <a name="vpclattice-ListTargetGroups-request-uri-vpcIdentifier"></a>
The ID or ARN of the VPC.
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Request Body
<a name="API_ListTargetGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTargetGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "id": "string",
         "ipAddressType": "string",
         "lambdaEventStructureVersion": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "port": number,
         "protocol": "string",
         "serviceArns": [ "string" ],
         "status": "string",
         "type": "string",
         "vpcIdentifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTargetGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListTargetGroups_ResponseSyntax) **   <a name="vpclattice-ListTargetGroups-response-items"></a>
Information about the target groups.
Type: Array of [TargetGroupSummary](API_TargetGroupSummary.md) objects

 ** [nextToken](#API_ListTargetGroups_ResponseSyntax) **   <a name="vpclattice-ListTargetGroups-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListTargetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

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
<a name="API_ListTargetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListTargetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListTargetGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
