---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuditSuppression.html
---

# CreateAuditSuppression
<a name="API_CreateAuditSuppression"></a>

 Creates a Device Defender audit suppression.

Requires permission to access the [CreateAuditSuppression](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateAuditSuppression_RequestSyntax"></a>

```
POST /audit/suppressions/create HTTP/1.1
Content-type: application/json

{
   "checkName": "{{string}}",
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "expirationDate": {{number}},
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
   },
   "suppressIndefinitely": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateAuditSuppression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAuditSuppression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [checkName](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String
Required: Yes

 ** [clientRequestToken](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-clientRequestToken"></a>
 Each audit supression must have a unique client request token. If you try to create a new audit suppression with the same token as one that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [description](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-description"></a>
 The description of the audit suppression.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** [expirationDate](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-expirationDate"></a>
 The epoch timestamp in seconds at which this suppression expires.
Type: Timestamp
Required: No

 ** [resourceIdentifier](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: Yes

 ** [suppressIndefinitely](#API_CreateAuditSuppression_RequestSyntax) **   <a name="iot-CreateAuditSuppression-request-suppressIndefinitely"></a>
 Indicates whether a suppression should exist indefinitely or not.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateAuditSuppression_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateAuditSuppression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateAuditSuppression_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateAuditSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateAuditSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateAuditSuppression)
