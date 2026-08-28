---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetPolicyVersion.html
---

# GetPolicyVersion
<a name="API_GetPolicyVersion"></a>

Returns details for the version of a policy. Policies define the permissions for team resources.

## Request Syntax
<a name="API_GetPolicyVersion_RequestSyntax"></a>

```
GET /policy-versions/{{PolicyVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicyVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PolicyVersionArn](#API_GetPolicyVersion_RequestSyntax) **   <a name="mpa-GetPolicyVersion-request-uri-PolicyVersionArn"></a>
Amazon Resource Name (ARN) for the policy.
Length Constraints: Minimum length of 0. Maximum length of 1224.
Pattern: `arn:.{1,63}:mpa:::aws:policy/[a-zA-Z0-9_\.-]{1,1023}/[a-zA-Z0-9_\.-]{1,1023}/(?:[\d]+|\$DEFAULT)`
Required: Yes

## Request Body
<a name="API_GetPolicyVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicyVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyVersion": {
      "Arn": "string",
      "CreationTime": "string",
      "Document": "string",
      "IsDefault": boolean,
      "LastUpdatedTime": "string",
      "Name": "string",
      "PolicyArn": "string",
      "PolicyType": "string",
      "Status": "string",
      "VersionId": number
   }
}
```

## Response Elements
<a name="API_GetPolicyVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyVersion](#API_GetPolicyVersion_ResponseSyntax) **   <a name="mpa-GetPolicyVersion-response-PolicyVersion"></a>
A `PolicyVersion` object. Contains details for the version of the policy. Policies define the permissions for team resources.
Type: [PolicyVersion](API_PolicyVersion.md) object

## Errors
<a name="API_GetPolicyVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_GetPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/GetPolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetPolicyVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
