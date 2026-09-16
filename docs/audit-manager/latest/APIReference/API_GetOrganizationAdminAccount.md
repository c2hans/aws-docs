---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetOrganizationAdminAccount.html
---

# GetOrganizationAdminAccount
<a name="API_GetOrganizationAdminAccount"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Gets the name of the delegated AWS administrator account for a specified organization.

## Request Syntax
<a name="API_GetOrganizationAdminAccount_RequestSyntax"></a>

```
GET /account/organizationAdminAccount HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOrganizationAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetOrganizationAdminAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOrganizationAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adminAccountId": "string",
   "organizationId": "string"
}
```

## Response Elements
<a name="API_GetOrganizationAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adminAccountId](#API_GetOrganizationAdminAccount_ResponseSyntax) **   <a name="auditmanager-GetOrganizationAdminAccount-response-adminAccountId"></a>
 The identifier for the administrator account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`

 ** [organizationId](#API_GetOrganizationAdminAccount_ResponseSyntax) **   <a name="auditmanager-GetOrganizationAdminAccount-response-organizationId"></a>
 The identifier for the organization.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`

## Errors
<a name="API_GetOrganizationAdminAccount_Errors"></a>

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

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetOrganizationAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetOrganizationAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetOrganizationAdminAccount)
