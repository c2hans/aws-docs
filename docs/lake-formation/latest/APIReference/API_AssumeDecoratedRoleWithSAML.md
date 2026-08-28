---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.html
---

# AssumeDecoratedRoleWithSAML
<a name="API_AssumeDecoratedRoleWithSAML"></a>

Allows a caller to assume an IAM role decorated as the SAML user specified in the SAML assertion included in the request. This decoration allows Lake Formation to enforce access policies against the SAML users and groups. This API operation requires SAML federation setup in the caller’s account as it can only be called with valid SAML assertions. Lake Formation does not scope down the permission of the assumed role. All permissions attached to the role via the SAML federation setup will be included in the role session.

 This decorated role is expected to access data in Amazon S3 by getting temporary access from Lake Formation which is authorized via the virtual API `GetDataAccess`. Therefore, all SAML roles that can be assumed via `AssumeDecoratedRoleWithSAML` must at a minimum include `lakeformation:GetDataAccess` in their role policies. A typical IAM policy attached to such a role would include the following actions:
+ glue:\*Database\*
+ glue:\*Table\*
+ glue:\*Partition\*
+ glue:\*UserDefinedFunction\*
+ lakeformation:GetDataAccess

## Request Syntax
<a name="API_AssumeDecoratedRoleWithSAML_RequestSyntax"></a>

```
POST /AssumeDecoratedRoleWithSAML HTTP/1.1
Content-type: application/json

{
   "DurationSeconds": {{number}},
   "PrincipalArn": "{{string}}",
   "RoleArn": "{{string}}",
   "SAMLAssertion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssumeDecoratedRoleWithSAML_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssumeDecoratedRoleWithSAML_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DurationSeconds](#API_AssumeDecoratedRoleWithSAML_RequestSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-request-DurationSeconds"></a>
The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** [PrincipalArn](#API_AssumeDecoratedRoleWithSAML_RequestSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-request-PrincipalArn"></a>
The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.
Type: String
Pattern: `arn:aws:iam::[0-9]*:saml-provider/.*`
Required: Yes

 ** [RoleArn](#API_AssumeDecoratedRoleWithSAML_RequestSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-request-RoleArn"></a>
The role that represents an IAM principal whose scope down policy allows it to call credential vending APIs such as `GetTemporaryTableCredentials`. The caller must also have iam:PassRole permission on this role.
Type: String
Pattern: `arn:aws:iam::[0-9]*:role/.*`
Required: Yes

 ** [SAMLAssertion](#API_AssumeDecoratedRoleWithSAML_RequestSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-request-SAMLAssertion"></a>
A SAML assertion consisting of an assertion statement for the user who needs temporary credentials. This must match the SAML assertion that was issued to IAM. This must be Base64 encoded.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 100000.
Required: Yes

## Response Syntax
<a name="API_AssumeDecoratedRoleWithSAML_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessKeyId": "string",
   "Expiration": number,
   "SecretAccessKey": "string",
   "SessionToken": "string"
}
```

## Response Elements
<a name="API_AssumeDecoratedRoleWithSAML_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessKeyId](#API_AssumeDecoratedRoleWithSAML_ResponseSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-response-AccessKeyId"></a>
The access key ID for the temporary credentials. (The access key consists of an access key ID and a secret key).
Type: String

 ** [Expiration](#API_AssumeDecoratedRoleWithSAML_ResponseSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-response-Expiration"></a>
The date and time when the temporary credentials expire.
Type: Timestamp

 ** [SecretAccessKey](#API_AssumeDecoratedRoleWithSAML_ResponseSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-response-SecretAccessKey"></a>
The secret key for the temporary credentials. (The access key consists of an access key ID and a secret key).
Type: String

 ** [SessionToken](#API_AssumeDecoratedRoleWithSAML_ResponseSyntax) **   <a name="lakeformation-AssumeDecoratedRoleWithSAML-response-SessionToken"></a>
The session token for the temporary credentials.
Type: String

## Errors
<a name="API_AssumeDecoratedRoleWithSAML_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_AssumeDecoratedRoleWithSAML_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/AssumeDecoratedRoleWithSAML)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
