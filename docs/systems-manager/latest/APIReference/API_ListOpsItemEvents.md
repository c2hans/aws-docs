---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsItemEvents.html
---

# ListOpsItemEvents
<a name="API_ListOpsItemEvents"></a>

Returns a list of all OpsItem events in the current AWS Region and AWS account. You can limit the results to events associated with specific OpsItems by specifying a filter.

## Request Syntax
<a name="API_ListOpsItemEvents_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOpsItemEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListOpsItemEvents_RequestSyntax) **   <a name="systemsmanager-ListOpsItemEvents-request-Filters"></a>
One or more OpsItem filters. Use a filter to return a more specific list of results.
Type: Array of [OpsItemEventFilter](API_OpsItemEventFilter.md) objects
Required: No

 ** [MaxResults](#API_ListOpsItemEvents_RequestSyntax) **   <a name="systemsmanager-ListOpsItemEvents-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListOpsItemEvents_RequestSyntax) **   <a name="systemsmanager-ListOpsItemEvents-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListOpsItemEvents_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Summaries": [
      {
         "CreatedBy": {
            "Arn": "string"
         },
         "CreatedTime": number,
         "Detail": "string",
         "DetailType": "string",
         "EventId": "string",
         "OpsItemId": "string",
         "Source": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOpsItemEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOpsItemEvents_ResponseSyntax) **   <a name="systemsmanager-ListOpsItemEvents-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [Summaries](#API_ListOpsItemEvents_ResponseSyntax) **   <a name="systemsmanager-ListOpsItemEvents-response-Summaries"></a>
A list of event information for the specified OpsItems.
Type: Array of [OpsItemEventSummary](API_OpsItemEventSummary.md) objects

## Errors
<a name="API_ListOpsItemEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

 ** OpsItemLimitExceededException **
The request caused OpsItems to exceed one or more quotas.
HTTP Status Code: 400

 ** OpsItemNotFoundException **
The specified OpsItem ID doesn't exist. Verify the ID and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListOpsItemEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListOpsItemEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListOpsItemEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
