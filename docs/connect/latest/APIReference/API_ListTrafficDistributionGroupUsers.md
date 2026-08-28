---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListTrafficDistributionGroupUsers.html
---

# ListTrafficDistributionGroupUsers
<a name="API_ListTrafficDistributionGroupUsers"></a>

Lists traffic distribution group users.

## Request Syntax
<a name="API_ListTrafficDistributionGroupUsers_RequestSyntax"></a>

```
GET /traffic-distribution-group/{{TrafficDistributionGroupId}}/user?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrafficDistributionGroupUsers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListTrafficDistributionGroupUsers_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroupUsers-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListTrafficDistributionGroupUsers_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroupUsers-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [TrafficDistributionGroupId](#API_ListTrafficDistributionGroupUsers_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroupUsers-request-uri-TrafficDistributionGroupId"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_ListTrafficDistributionGroupUsers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrafficDistributionGroupUsers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TrafficDistributionGroupUserSummaryList": [
      {
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrafficDistributionGroupUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrafficDistributionGroupUsers_ResponseSyntax) **   <a name="connect-ListTrafficDistributionGroupUsers-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [TrafficDistributionGroupUserSummaryList](#API_ListTrafficDistributionGroupUsers_ResponseSyntax) **   <a name="connect-ListTrafficDistributionGroupUsers-response-TrafficDistributionGroupUserSummaryList"></a>
A list of traffic distribution group users.
Type: Array of [TrafficDistributionGroupUserSummary](API_TrafficDistributionGroupUserSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_ListTrafficDistributionGroupUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_ListTrafficDistributionGroupUsers_Examples"></a>

### Example
<a name="API_ListTrafficDistributionGroupUsers_Example_1"></a>

The following example lists traffic distribution group users.

#### Sample Request
<a name="API_ListTrafficDistributionGroupUsers_Example_1_Request"></a>

```
GET connect.[region].amazonaws.com/traffic-distribution-group/[traffic_distribution_group_id]/user
```

#### Sample Response
<a name="API_ListTrafficDistributionGroupUsers_Example_1_Response"></a>

```
{
   "TrafficDistributionGroupUserSummaryList": [
      {
         "UserId": "[user_id]"
      }
   ]
}
```

## See Also
<a name="API_ListTrafficDistributionGroupUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListTrafficDistributionGroupUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListTrafficDistributionGroupUsers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
