---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectClientAddIns.html
---

# DescribeConnectClientAddIns
<a name="API_DescribeConnectClientAddIns"></a>

Retrieves a list of Connect Customer client add-ins that have been created.

## Request Syntax
<a name="API_DescribeConnectClientAddIns_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectClientAddIns_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeConnectClientAddIns_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectClientAddIns-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeConnectClientAddIns_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectClientAddIns-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ResourceId](#API_DescribeConnectClientAddIns_RequestSyntax) **   <a name="WorkSpaces-DescribeConnectClientAddIns-request-ResourceId"></a>
The directory identifier for which the client add-in is configured.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

## Response Syntax
<a name="API_DescribeConnectClientAddIns_ResponseSyntax"></a>

```
{
   "AddIns": [
      {
         "AddInId": "string",
         "Name": "string",
         "ResourceId": "string",
         "URL": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConnectClientAddIns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddIns](#API_DescribeConnectClientAddIns_ResponseSyntax) **   <a name="WorkSpaces-DescribeConnectClientAddIns-response-AddIns"></a>
Information about client add-ins.
Type: Array of [ConnectClientAddIn](API_ConnectClientAddIn.md) objects

 ** [NextToken](#API_DescribeConnectClientAddIns_ResponseSyntax) **   <a name="WorkSpaces-DescribeConnectClientAddIns-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeConnectClientAddIns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConnectClientAddIns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeConnectClientAddIns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeConnectClientAddIns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
