---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditSuppression.html
---

# DescribeAuditSuppression
<a name="API_DescribeAuditSuppression"></a>

 Gets information about a Device Defender audit suppression.

## Request Syntax
<a name="API_DescribeAuditSuppression_RequestSyntax"></a>

```
POST /audit/suppressions/describe HTTP/1.1
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
<a name="API_DescribeAuditSuppression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAuditSuppression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [checkName](#API_DescribeAuditSuppression_RequestSyntax) **   <a name="iot-DescribeAuditSuppression-request-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String
Required: Yes

 ** [resourceIdentifier](#API_DescribeAuditSuppression_RequestSyntax) **   <a name="iot-DescribeAuditSuppression-request-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_DescribeAuditSuppression_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "checkName": "string",
   "description": "string",
   "expirationDate": number,
   "resourceIdentifier": {
      "account": "string",
      "caCertificateId": "string",
      "clientId": "string",
      "cognitoIdentityPoolId": "string",
      "deviceCertificateArn": "string",
      "deviceCertificateId": "string",
      "iamRoleArn": "string",
      "issuerCertificateIdentifier": {
         "issuerCertificateSerialNumber": "string",
         "issuerCertificateSubject": "string",
         "issuerId": "string"
      },
      "policyVersionIdentifier": {
         "policyName": "string",
         "policyVersionId": "string"
      },
      "roleAliasArn": "string"
   },
   "suppressIndefinitely": boolean
}
```

## Response Elements
<a name="API_DescribeAuditSuppression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checkName](#API_DescribeAuditSuppression_ResponseSyntax) **   <a name="iot-DescribeAuditSuppression-response-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String

 ** [description](#API_DescribeAuditSuppression_ResponseSyntax) **   <a name="iot-DescribeAuditSuppression-response-description"></a>
 The description of the audit suppression.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`

 ** [expirationDate](#API_DescribeAuditSuppression_ResponseSyntax) **   <a name="iot-DescribeAuditSuppression-response-expirationDate"></a>
 The epoch timestamp in seconds at which this suppression expires.
Type: Timestamp

 ** [resourceIdentifier](#API_DescribeAuditSuppression_ResponseSyntax) **   <a name="iot-DescribeAuditSuppression-response-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object

 ** [suppressIndefinitely](#API_DescribeAuditSuppression_ResponseSyntax) **   <a name="iot-DescribeAuditSuppression-response-suppressIndefinitely"></a>
 Indicates whether a suppression should exist indefinitely or not.
Type: Boolean

## Errors
<a name="API_DescribeAuditSuppression_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAuditSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeAuditSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeAuditSuppression)
