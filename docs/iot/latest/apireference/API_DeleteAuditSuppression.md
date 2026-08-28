---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuditSuppression.html
---

# DeleteAuditSuppression
<a name="API_DeleteAuditSuppression"></a>

 Deletes a Device Defender audit suppression.

Requires permission to access the [DeleteAuditSuppression](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteAuditSuppression_RequestSyntax"></a>

```
POST /audit/suppressions/delete HTTP/1.1
Content-type: application/json

{
   "checkName": "{{string}}",
   "resourceIdentifier": {
      "account": "{{string}}",
      "caCertificateId": "{{string}}",
      "clientId": "{{string}}",
      "cognitoIdentityPoolId": "{{string}}",
      "deviceCertificateArn": "{{string}}",
      "deviceCertificateId": "{{string}}",
      "iamRoleArn": "{{string}}",
      "issuerCertificateIdentifier": {
         "issuerCertificateSerialNumber": "{{string}}",
         "issuerCertificateSubject": "{{string}}",
         "issuerId": "{{string}}"
      },
      "policyVersionIdentifier": {
         "policyName": "{{string}}",
         "policyVersionId": "{{string}}"
      },
      "roleAliasArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DeleteAuditSuppression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAuditSuppression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [checkName](#API_DeleteAuditSuppression_RequestSyntax) **   <a name="iot-DeleteAuditSuppression-request-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String
Required: Yes

 ** [resourceIdentifier](#API_DeleteAuditSuppression_RequestSyntax) **   <a name="iot-DeleteAuditSuppression-request-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_DeleteAuditSuppression_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAuditSuppression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAuditSuppression_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAuditSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteAuditSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteAuditSuppression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
