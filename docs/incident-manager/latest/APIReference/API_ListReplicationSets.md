---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListReplicationSets.html
---

# ListReplicationSets
<a name="API_ListReplicationSets"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists details about the replication set configured in your account.

## Request Syntax
<a name="API_ListReplicationSets_RequestSyntax"></a>

```
POST /listReplicationSets HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListReplicationSets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListReplicationSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListReplicationSets_RequestSyntax) **   <a name="IncidentManager-ListReplicationSets-request-maxResults"></a>
The maximum number of results per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListReplicationSets_RequestSyntax) **   <a name="IncidentManager-ListReplicationSets-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListReplicationSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "replicationSetArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListReplicationSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReplicationSets_ResponseSyntax) **   <a name="IncidentManager-ListReplicationSets-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [replicationSetArns](#API_ListReplicationSets_ResponseSyntax) **   <a name="IncidentManager-ListReplicationSets-response-replicationSetArns"></a>
The Amazon Resource Name (ARN) of the list replication set.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

## Errors
<a name="API_ListReplicationSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListReplicationSets_Examples"></a>

### Example
<a name="API_ListReplicationSets_Example_1"></a>

This example illustrates one usage of ListReplicationSets.

#### Sample Request
<a name="API_ListReplicationSets_Example_1_Request"></a>

```
POST /listReplicationSets HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-replication-sets
X-Amz-Date: 20210810T223055Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_ListReplicationSets_Example_1_Response"></a>

```
{
	"nextToken":null,
	"replicationSetArns":
		[
			"arn:aws:ssm-incidents::111122223333:replication-set/40bd98f0-4110-2dee-b35e-b87006f9e172"
		]
}
```

## See Also
<a name="API_ListReplicationSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListReplicationSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListReplicationSets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
