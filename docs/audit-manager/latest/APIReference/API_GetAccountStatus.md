---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAccountStatus.html
---

# GetAccountStatus
<a name="API_GetAccountStatus"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Gets the registration status of an account in AWS Audit Manager.

## Request Syntax
<a name="API_GetAccountStatus_RequestSyntax"></a>

```
GET /account/status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_GetAccountStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetAccountStatus_ResponseSyntax) **   <a name="auditmanager-GetAccountStatus-response-status"></a>
 The status of the AWS account.
Type: String
Valid Values: `ACTIVE | INACTIVE | PENDING_ACTIVATION`

## Errors
<a name="API_GetAccountStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

## Examples
<a name="API_GetAccountStatus_Examples"></a>

### Identifying the registration status for an account
<a name="API_GetAccountStatus_Example_1"></a>

This is an example response of the `GetAccountStatus` API operation for an active account.

#### Sample Response
<a name="API_GetAccountStatus_Example_1_Response"></a>

```
{
    "status": "ACTIVE"
}
```

## See Also
<a name="API_GetAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetAccountStatus)
