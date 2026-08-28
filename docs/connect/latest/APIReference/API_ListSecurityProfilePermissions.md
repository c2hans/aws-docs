---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListSecurityProfilePermissions.html
---

# ListSecurityProfilePermissions
<a name="API_ListSecurityProfilePermissions"></a>

Lists the permissions granted to a security profile.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Request Syntax
<a name="API_ListSecurityProfilePermissions_RequestSyntax"></a>

```
GET /security-profiles-permissions/{{InstanceId}}/{{SecurityProfileId}}?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSecurityProfilePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListSecurityProfilePermissions_RequestSyntax) **   <a name="connect-ListSecurityProfilePermissions-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListSecurityProfilePermissions_RequestSyntax) **   <a name="connect-ListSecurityProfilePermissions-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListSecurityProfilePermissions_RequestSyntax) **   <a name="connect-ListSecurityProfilePermissions-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [SecurityProfileId](#API_ListSecurityProfilePermissions_RequestSyntax) **   <a name="connect-ListSecurityProfilePermissions-request-uri-SecurityProfileId"></a>
The identifier for the security profle.
Required: Yes

## Request Body
<a name="API_ListSecurityProfilePermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSecurityProfilePermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastModifiedRegion": "string",
   "LastModifiedTime": number,
   "NextToken": "string",
   "Permissions": [ "string" ]
}
```

## Response Elements
<a name="API_ListSecurityProfilePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastModifiedRegion](#API_ListSecurityProfilePermissions_ResponseSyntax) **   <a name="connect-ListSecurityProfilePermissions-response-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_ListSecurityProfilePermissions_ResponseSyntax) **   <a name="connect-ListSecurityProfilePermissions-response-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp

 ** [NextToken](#API_ListSecurityProfilePermissions_ResponseSyntax) **   <a name="connect-ListSecurityProfilePermissions-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [Permissions](#API_ListSecurityProfilePermissions_ResponseSyntax) **   <a name="connect-ListSecurityProfilePermissions-response-Permissions"></a>
The permissions granted to the security profile. For a complete list of valid permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).
Type: Array of strings
Array Members: Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_ListSecurityProfilePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

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

## See Also
<a name="API_ListSecurityProfilePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListSecurityProfilePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListSecurityProfilePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
