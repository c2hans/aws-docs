---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html
---

# RegisterAccount
<a name="API_RegisterAccount"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Enables AWS Audit Manager for the specified AWS account.

## Request Syntax
<a name="API_RegisterAccount_RequestSyntax"></a>

```
POST /account/registerAccount HTTP/1.1
Content-type: application/json

{
   "delegatedAdminAccount": "{{string}}",
   "kmsKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [delegatedAdminAccount](#API_RegisterAccount_RequestSyntax) **   <a name="auditmanager-RegisterAccount-request-delegatedAdminAccount"></a>
 The delegated administrator account for Audit Manager.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** [kmsKey](#API_RegisterAccount_RequestSyntax) **   <a name="auditmanager-RegisterAccount-request-kmsKey"></a>
 The AWS KMS key details.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `^arn:.*:kms:.*|DEFAULT`
Required: No

## Response Syntax
<a name="API_RegisterAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_RegisterAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_RegisterAccount_ResponseSyntax) **   <a name="auditmanager-RegisterAccount-response-status"></a>
 The status of the account registration request.
Type: String
Valid Values: `ACTIVE | INACTIVE | PENDING_ACTIVATION`

## Errors
<a name="API_RegisterAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_RegisterAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/RegisterAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/RegisterAccount)
