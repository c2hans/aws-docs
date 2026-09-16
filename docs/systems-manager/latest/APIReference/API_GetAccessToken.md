---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetAccessToken.html
---

# GetAccessToken
<a name="API_GetAccessToken"></a>

Returns a credentials set to be used with just-in-time node access.

## Request Syntax
<a name="API_GetAccessToken_RequestSyntax"></a>

```
{
   "AccessRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAccessToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessRequestId](#API_GetAccessToken_RequestSyntax) **   <a name="systemsmanager-GetAccessToken-request-AccessRequestId"></a>
The ID of a just-in-time node access request.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetAccessToken_ResponseSyntax"></a>

```
{
   "AccessRequestStatus": "string",
   "Credentials": {
      "AccessKeyId": "string",
      "ExpirationTime": number,
      "SecretAccessKey": "string",
      "SessionToken": "string"
   }
}
```

## Response Elements
<a name="API_GetAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessRequestStatus](#API_GetAccessToken_ResponseSyntax) **   <a name="systemsmanager-GetAccessToken-response-AccessRequestStatus"></a>
The status of the access request.
Type: String
Valid Values: `Approved | Rejected | Revoked | Expired | Pending`

 ** [Credentials](#API_GetAccessToken_ResponseSyntax) **   <a name="systemsmanager-GetAccessToken-response-Credentials"></a>
The temporary security credentials which can be used to start just-in-time node access sessions.
Type: [Credentials](API_Credentials.md) object

## Errors
<a name="API_GetAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester doesn't have permissions to perform the requested operation.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request or operation couldn't be performed because the service is throttling requests.
 ** QuotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** ServiceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ValidationException **
The request isn't valid. Verify that you entered valid contents for the command and try again.
 ** ReasonCode **
The reason code for the invalid request.
HTTP Status Code: 400

## See Also
<a name="API_GetAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetAccessToken)
