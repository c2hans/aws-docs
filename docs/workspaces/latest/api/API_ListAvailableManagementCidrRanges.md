---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html
---

# ListAvailableManagementCidrRanges
<a name="API_ListAvailableManagementCidrRanges"></a>

Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable Bring Your Own License (BYOL).

This operation can be run only by AWS accounts that are enabled for BYOL. If your account isn't enabled for BYOL, you'll receive an `AccessDeniedException` error.

The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.

## Request Syntax
<a name="API_ListAvailableManagementCidrRanges_RequestSyntax"></a>

```
{
   "ManagementCidrRangeConstraint": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailableManagementCidrRanges_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ManagementCidrRangeConstraint](#API_ListAvailableManagementCidrRanges_RequestSyntax) **   <a name="WorkSpaces-ListAvailableManagementCidrRanges-request-ManagementCidrRangeConstraint"></a>
The IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).
Type: String
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$`
Required: Yes

 ** [MaxResults](#API_ListAvailableManagementCidrRanges_RequestSyntax) **   <a name="WorkSpaces-ListAvailableManagementCidrRanges-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [NextToken](#API_ListAvailableManagementCidrRanges_RequestSyntax) **   <a name="WorkSpaces-ListAvailableManagementCidrRanges-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListAvailableManagementCidrRanges_ResponseSyntax"></a>

```
{
   "ManagementCidrRanges": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailableManagementCidrRanges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagementCidrRanges](#API_ListAvailableManagementCidrRanges_ResponseSyntax) **   <a name="WorkSpaces-ListAvailableManagementCidrRanges-response-ManagementCidrRanges"></a>
The list of available IP address ranges, specified as IPv4 CIDR blocks.
Type: Array of strings
Pattern: `(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.0\.0)(\/(16$))$`

 ** [NextToken](#API_ListAvailableManagementCidrRanges_ResponseSyntax) **   <a name="WorkSpaces-ListAvailableManagementCidrRanges-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAvailableManagementCidrRanges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_ListAvailableManagementCidrRanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ListAvailableManagementCidrRanges)
