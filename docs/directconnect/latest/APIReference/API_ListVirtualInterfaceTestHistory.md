---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html
---

# ListVirtualInterfaceTestHistory
<a name="API_ListVirtualInterfaceTestHistory"></a>

Lists the virtual interface failover test history.

## Request Syntax
<a name="API_ListVirtualInterfaceTestHistory_RequestSyntax"></a>

```
{
   "bgpPeers": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}",
   "testId": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVirtualInterfaceTestHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bgpPeers](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-bgpPeers"></a>
The BGP peers that were placed in the DOWN state during the virtual interface failover test.
Type: Array of strings
Required: No

 ** [maxResults](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

 ** [status](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-status"></a>
The status of the virtual interface failover test.
Type: String
Required: No

 ** [testId](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-testId"></a>
The ID of the virtual interface failover test.
Type: String
Required: No

 ** [virtualInterfaceId](#API_ListVirtualInterfaceTestHistory_RequestSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-request-virtualInterfaceId"></a>
The ID of the virtual interface that was tested.
Type: String
Required: No

## Response Syntax
<a name="API_ListVirtualInterfaceTestHistory_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "virtualInterfaceTestHistory": [
      {
         "bgpPeers": [ "string" ],
         "endTime": number,
         "ownerAccount": "string",
         "startTime": number,
         "status": "string",
         "testDurationInMinutes": number,
         "testId": "string",
         "virtualInterfaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVirtualInterfaceTestHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVirtualInterfaceTestHistory_ResponseSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [virtualInterfaceTestHistory](#API_ListVirtualInterfaceTestHistory_ResponseSyntax) **   <a name="DX-ListVirtualInterfaceTestHistory-response-virtualInterfaceTestHistory"></a>
The ID of the tested virtual interface.
Type: Array of [VirtualInterfaceTestHistory](API_VirtualInterfaceTestHistory.md) objects

## Errors
<a name="API_ListVirtualInterfaceTestHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_ListVirtualInterfaceTestHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ListVirtualInterfaceTestHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
