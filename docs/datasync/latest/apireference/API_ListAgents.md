---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ListAgents.html
---

# ListAgents
<a name="API_ListAgents"></a>

Returns a list of AWS DataSync agents that belong to an AWS account in the AWS Region specified in the request.

With pagination, you can reduce the number of agents returned in a response. If you get a truncated list of agents in a response, the response contains a marker that you can specify in your next request to fetch the next page of agents.

 `ListAgents` is eventually consistent. This means the result of running the operation might not reflect that you just created or deleted an agent. For example, if you create an agent with [CreateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html) and then immediately run `ListAgents`, that agent might not show up in the list right away. In situations like this, you can always confirm whether an agent has been created (or deleted) by using [DescribeAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html).

## Request Syntax
<a name="API_ListAgents_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAgents_RequestSyntax) **   <a name="DataSync-ListAgents-request-MaxResults"></a>
Specifies the maximum number of DataSync agents to list in a response. By default, a response shows a maximum of 100 agents.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAgents_RequestSyntax) **   <a name="DataSync-ListAgents-request-NextToken"></a>
Specifies an opaque string that indicates the position to begin the next list of results in the response.
Type: String
Length Constraints: Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

## Response Syntax
<a name="API_ListAgents_ResponseSyntax"></a>

```
{
   "Agents": [
      {
         "AgentArn": "string",
         "Name": "string",
         "Platform": {
            "Version": "string"
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Agents](#API_ListAgents_ResponseSyntax) **   <a name="DataSync-ListAgents-response-Agents"></a>
A list of DataSync agents in your AWS account in the AWS Region specified in the request. The list is ordered by the agents' Amazon Resource Names (ARNs).
Type: Array of [AgentListEntry](API_AgentListEntry.md) objects

 ** [NextToken](#API_ListAgents_ResponseSyntax) **   <a name="DataSync-ListAgents-response-NextToken"></a>
The opaque string that indicates the position to begin the next list of results in the response.
Type: String
Length Constraints: Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListAgents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_ListAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/ListAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/ListAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ListAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/ListAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ListAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/ListAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/ListAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/ListAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/ListAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ListAgents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
