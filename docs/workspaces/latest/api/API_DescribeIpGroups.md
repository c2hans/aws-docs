---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeIpGroups.html
---

# DescribeIpGroups
<a name="API_DescribeIpGroups"></a>

Describes one or more of your IP access control groups.

## Request Syntax
<a name="API_DescribeIpGroups_RequestSyntax"></a>

```
{
   "GroupIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIpGroups_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [GroupIds](#API_DescribeIpGroups_RequestSyntax) **   <a name="WorkSpaces-DescribeIpGroups-request-GroupIds"></a>
The identifiers of one or more IP access control groups.
Type: Array of strings
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: No

 ** [MaxResults](#API_DescribeIpGroups_RequestSyntax) **   <a name="WorkSpaces-DescribeIpGroups-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeIpGroups_RequestSyntax) **   <a name="WorkSpaces-DescribeIpGroups-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeIpGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Result": [
      {
         "groupDesc": "string",
         "groupId": "string",
         "groupName": "string",
         "userRules": [
            {
               "ipRule": "string",
               "ruleDesc": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeIpGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeIpGroups_ResponseSyntax) **   <a name="WorkSpaces-DescribeIpGroups-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Result](#API_DescribeIpGroups_ResponseSyntax) **   <a name="WorkSpaces-DescribeIpGroups-response-Result"></a>
Information about the IP access control groups.
Type: Array of [WorkspacesIpGroup](API_WorkspacesIpGroup.md) objects

## Errors
<a name="API_DescribeIpGroups_Errors"></a>

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
<a name="API_DescribeIpGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeIpGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeIpGroups)
