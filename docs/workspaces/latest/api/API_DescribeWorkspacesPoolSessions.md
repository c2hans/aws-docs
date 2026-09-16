---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesPoolSessions.html
---

# DescribeWorkspacesPoolSessions
<a name="API_DescribeWorkspacesPoolSessions"></a>

**Note**
End of support notice: On December 31, 2027, AWS will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html).

Retrieves a list that describes the streaming sessions for a specified pool.

## Request Syntax
<a name="API_DescribeWorkspacesPoolSessions_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "PoolId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspacesPoolSessions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribeWorkspacesPoolSessions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-request-Limit"></a>
The maximum size of each page of results. The default value is 20 and the maximum value is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeWorkspacesPoolSessions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PoolId](#API_DescribeWorkspacesPoolSessions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-request-PoolId"></a>
The identifier of the pool.
Type: String
Pattern: `^wspool-[0-9a-z]{9}$`
Required: Yes

 ** [UserId](#API_DescribeWorkspacesPoolSessions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-request-UserId"></a>
The identifier of the user.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_DescribeWorkspacesPoolSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Sessions": [
      {
         "AuthenticationType": "string",
         "ConnectionState": "string",
         "ExpirationTime": number,
         "InstanceId": "string",
         "NetworkAccessConfiguration": {
            "EniId": "string",
            "EniPrivateIpAddress": "string"
         },
         "PoolId": "string",
         "SessionId": "string",
         "StartTime": number,
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeWorkspacesPoolSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeWorkspacesPoolSessions_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-response-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Sessions](#API_DescribeWorkspacesPoolSessions_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspacesPoolSessions-response-Sessions"></a>
Describes the pool sessions.
Type: Array of [WorkspacesPoolSession](API_WorkspacesPoolSession.md) objects

## Errors
<a name="API_DescribeWorkspacesPoolSessions_Errors"></a>

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
<a name="API_DescribeWorkspacesPoolSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspacesPoolSessions)
