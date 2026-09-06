---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditSuppressions.html
---

# ListAuditSuppressions
<a name="API_ListAuditSuppressions"></a>

 Lists your Device Defender audit listings.

Requires permission to access the [ListAuditSuppressions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAuditSuppressions_RequestSyntax"></a>

```
POST /audit/suppressions/list HTTP/1.1
Content-type: application/json

{
   "ascendingOrder": {{boolean}},
   "checkName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
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
<a name="API_ListAuditSuppressions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAuditSuppressions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ascendingOrder](#API_ListAuditSuppressions_RequestSyntax) **   <a name="iot-ListAuditSuppressions-request-ascendingOrder"></a>
 Determines whether suppressions are listed in ascending order by expiration date or not. If parameter isn't provided, `ascendingOrder=true`.
Type: Boolean
Required: No

 ** [checkName](#API_ListAuditSuppressions_RequestSyntax) **   <a name="iot-ListAuditSuppressions-request-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String
Required: No

 ** [maxResults](#API_ListAuditSuppressions_RequestSyntax) **   <a name="iot-ListAuditSuppressions-request-maxResults"></a>
 The maximum number of results to return at one time. The default is 25.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [nextToken](#API_ListAuditSuppressions_RequestSyntax) **   <a name="iot-ListAuditSuppressions-request-nextToken"></a>
 The token for the next set of results.
Type: String
Required: No

 ** [resourceIdentifier](#API_ListAuditSuppressions_RequestSyntax) **   <a name="iot-ListAuditSuppressions-request-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

## Response Syntax
<a name="API_ListAuditSuppressions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "suppressions": [
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
   ]
}
```

## Response Elements
<a name="API_ListAuditSuppressions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAuditSuppressions_ResponseSyntax) **   <a name="iot-ListAuditSuppressions-response-nextToken"></a>
 A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

 ** [suppressions](#API_ListAuditSuppressions_ResponseSyntax) **   <a name="iot-ListAuditSuppressions-response-suppressions"></a>
 List of audit suppressions.
Type: Array of [AuditSuppression](API_AuditSuppression.md) objects

## Errors
<a name="API_ListAuditSuppressions_Errors"></a>

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
<a name="API_ListAuditSuppressions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAuditSuppressions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAuditSuppressions)
