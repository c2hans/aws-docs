---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_PutAdminAccount.html
---

# PutAdminAccount
<a name="API_PutAdminAccount"></a>

Sets the AWS account that serves as an AWS Network Security Manager administrator account, and optionally configures the scope of resources that the administrator can manage.

You can't set an administrator account again immediately after you remove it, or while the service creates its service-linked role. Retry the request after a few minutes.

## Request Syntax
<a name="API_PutAdminAccount_RequestSyntax"></a>

```
PUT /admin-account HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}",
   "adminScope": {
      "firewallTypeScope": {
         "allFirewallTypesEnabled": {{boolean}},
         "firewallTypes": [ "{{string}}" ]
      },
      "scopeFilter": { ... }
   },
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_PutAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAdminAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_PutAdminAccount_RequestSyntax) **   <a name="networksecuritymanager-PutAdminAccount-request-accountId"></a>
The AWS account ID to set as the AWS Network Security Manager administrator account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

 ** [adminScope](#API_PutAdminAccount_RequestSyntax) **   <a name="networksecuritymanager-PutAdminAccount-request-adminScope"></a>
The scope of accounts, organizational units, and firewall types that the administrator can manage.
Type: [AdminScopeInput](API_AdminScopeInput.md) object
Required: No

 ** [priority](#API_PutAdminAccount_RequestSyntax) **   <a name="networksecuritymanager-PutAdminAccount-request-priority"></a>
The priority to assign to the administrator account.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

## Response Syntax
<a name="API_PutAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adminAccountDetails": {
      "adminAccount": "string",
      "adminScope": {
         "firewallTypeScope": {
            "allFirewallTypesEnabled": boolean,
            "firewallTypes": [ "string" ]
         },
         "scopeFilter": { ... }
      },
      "priority": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_PutAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adminAccountDetails](#API_PutAdminAccount_ResponseSyntax) **   <a name="networksecuritymanager-PutAdminAccount-response-adminAccountDetails"></a>
The details of the administrator account that was set.
Type: [AdminAccountDetails](API_AdminAccountDetails.md) object

## Errors
<a name="API_PutAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.
 ** resourceId **
The ID of the resource that is in conflict with the request.
 ** resourceType **
The type of the resource that is in conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
The request processing failed because of an internal error in the service. This is a retryable error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would exceed a service quota.
 ** quotaCode **
The code that identifies the service quota that was exceeded.
 ** resourceId **
The ID of the resource associated with the quota that was exceeded.
 ** resourceType **
The type of the resource associated with the quota that was exceeded.
 ** serviceCode **
The code for the AWS service that owns the quota that was exceeded.
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is temporarily unavailable. This is a retryable error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 503

 ** ThrottlingException **
The request was denied because of request throttling. Reduce your request rate and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation. For details, see the `reason` and `fieldList` members of the response.
 ** fieldList **
The list of request fields that failed validation, if any.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_PutAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-security-manager-2025-10-30/PutAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/PutAdminAccount)
