---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListTrafficDistributionGroups.html
---

# ListTrafficDistributionGroups
<a name="API_ListTrafficDistributionGroups"></a>

Lists traffic distribution groups.

## Request Syntax
<a name="API_ListTrafficDistributionGroups_RequestSyntax"></a>

```
GET /traffic-distribution-groups?instanceId={{InstanceId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrafficDistributionGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListTrafficDistributionGroups_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroups-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:instance/)?[a-zA-Z0-9_-]+$`

 ** [MaxResults](#API_ListTrafficDistributionGroups_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroups-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListTrafficDistributionGroups_RequestSyntax) **   <a name="connect-ListTrafficDistributionGroups-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListTrafficDistributionGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrafficDistributionGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TrafficDistributionGroupSummaryList": [
      {
         "Arn": "string",
         "Id": "string",
         "InstanceArn": "string",
         "IsDefault": boolean,
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrafficDistributionGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrafficDistributionGroups_ResponseSyntax) **   <a name="connect-ListTrafficDistributionGroups-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [TrafficDistributionGroupSummaryList](#API_ListTrafficDistributionGroups_ResponseSyntax) **   <a name="connect-ListTrafficDistributionGroups-response-TrafficDistributionGroupSummaryList"></a>
A list of traffic distribution groups.
Type: Array of [TrafficDistributionGroupSummary](API_TrafficDistributionGroupSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_ListTrafficDistributionGroups_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListTrafficDistributionGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListTrafficDistributionGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListTrafficDistributionGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
