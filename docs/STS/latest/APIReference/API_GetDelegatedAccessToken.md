---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetDelegatedAccessToken.html
---

# GetDelegatedAccessToken
<a name="API_GetDelegatedAccessToken"></a>

Exchanges a trade-in token for temporary AWS credentials with the permissions associated with the assumed principal. This operation allows you to obtain credentials for a specific principal based on a trade-in token, enabling delegation of access to AWS resources.

## Request Parameters
<a name="API_GetDelegatedAccessToken_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TradeInToken **
The token to exchange for temporary AWS credentials. This token must be valid and unexpired at the time of the request.
Type: String
Required: Yes

## Response Elements
<a name="API_GetDelegatedAccessToken_ResponseElements"></a>

The following elements are returned by the service.

 ** AssumedPrincipal **
The Amazon Resource Name (ARN) of the principal that was assumed when obtaining the delegated access token. This ARN identifies the IAM entity whose permissions are granted by the temporary credentials.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`

 ** Credentials **
 AWS credentials for API authentication.
Type: [Credentials](API_Credentials.md) object

 ** PackedPolicySize **
The percentage of the maximum policy size that is used by the session policy. The policy size is calculated as the sum of all the session policies and permission boundaries attached to the session. If the packed size exceeds 100%, the request fails.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_GetDelegatedAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExpiredTradeInToken **
The trade-in token provided in the request has expired and can no longer be exchanged for credentials. Request a new token and retry the operation.
HTTP Status Code: 400

 ** PackedPolicyTooLarge **
The request was rejected because the total packed size of the session policies and session tags combined was too large. An AWS conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) in the *IAM User Guide*.
You could receive this error even though you meet other defined session policy and session tag limits. For more information, see [IAM and AWS STS Entity Character Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length) in the *IAM User Guide*.
HTTP Status Code: 400

## See Also
<a name="API_GetDelegatedAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/GetDelegatedAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/GetDelegatedAccessToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Token Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query STS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
