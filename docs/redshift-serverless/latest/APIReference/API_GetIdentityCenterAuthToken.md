---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetIdentityCenterAuthToken.html
---

# GetIdentityCenterAuthToken
<a name="API_GetIdentityCenterAuthToken"></a>

Returns an Identity Center authentication token for accessing Amazon Redshift Serverless workgroups.

The token provides secure access to data within the specified workgroups using Identity Center identity propagation. The token expires after a specified duration and must be refreshed for continued access.

The AWS Identity and Access Management (IAM) user or role that runs GetIdentityCenterAuthToken must have appropriate permissions to access the specified workgroups and Identity Center integration must be configured for the workgroups.

## Request Syntax
<a name="API_GetIdentityCenterAuthToken_RequestSyntax"></a>

```
{
   "workgroupNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetIdentityCenterAuthToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [workgroupNames](#API_GetIdentityCenterAuthToken_RequestSyntax) **   <a name="redshiftserverless-GetIdentityCenterAuthToken-request-workgroupNames"></a>
A list of workgroup names for which to generate the Identity Center authentication token.
Constraints:
+ Must contain between 1 and 20 workgroup names.
+ Each workgroup name must be a valid Amazon Redshift Serverless workgroup identifier.
+ All specified workgroups must have Identity Center integration enabled.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetIdentityCenterAuthToken_ResponseSyntax"></a>

```
{
   "expirationTime": "string",
   "token": "string"
}
```

## Response Elements
<a name="API_GetIdentityCenterAuthToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [expirationTime](#API_GetIdentityCenterAuthToken_ResponseSyntax) **   <a name="redshiftserverless-GetIdentityCenterAuthToken-response-expirationTime"></a>
The date and time when the Identity Center authentication token expires.
After this time, a new token must be requested for continued access.
Type: Timestamp

 ** [token](#API_GetIdentityCenterAuthToken_ResponseSyntax) **   <a name="redshiftserverless-GetIdentityCenterAuthToken-response-token"></a>
The Identity Center authentication token that can be used to access data in the specified workgroups.
This token contains the Identity Center identity information and is encrypted for secure transmission.
Type: String

## Errors
<a name="API_GetIdentityCenterAuthToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** DryRunException **
This exception is thrown when the request was successful, but dry run was enabled so no action was taken.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetIdentityCenterAuthToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetIdentityCenterAuthToken)
