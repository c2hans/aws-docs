---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateLakeFormationIdentityCenterConfiguration.html
---

# UpdateLakeFormationIdentityCenterConfiguration
<a name="API_UpdateLakeFormationIdentityCenterConfiguration"></a>

Updates the IAM Identity Center connection parameters.

## Request Syntax
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax"></a>

```
POST /UpdateLakeFormationIdentityCenterConfiguration HTTP/1.1
Content-type: application/json

{
   "ApplicationStatus": "{{string}}",
   "CatalogId": "{{string}}",
   "ExternalFiltering": {
      "AuthorizedTargets": [ "{{string}}" ],
      "Status": "{{string}}"
   },
   "ServiceIntegrations": [
      { ... }
   ],
   "ShareRecipients": [
      {
         "DataLakePrincipalIdentifier": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationStatus](#API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-UpdateLakeFormationIdentityCenterConfiguration-request-ApplicationStatus"></a>
Allows to enable or disable the IAM Identity Center connection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [CatalogId](#API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-UpdateLakeFormationIdentityCenterConfiguration-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ExternalFiltering](#API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-UpdateLakeFormationIdentityCenterConfiguration-request-ExternalFiltering"></a>
A list of the account IDs of AWS accounts of third-party applications that are allowed to access data managed by Lake Formation.
Type: [ExternalFilteringConfiguration](API_ExternalFilteringConfiguration.md) object
Required: No

 ** [ServiceIntegrations](#API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-UpdateLakeFormationIdentityCenterConfiguration-request-ServiceIntegrations"></a>
A list of service integrations for enabling trusted identity propagation with external services such as Redshift.
Type: Array of [ServiceIntegrationUnion](API_ServiceIntegrationUnion.md) objects
Required: No

 ** [ShareRecipients](#API_UpdateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-UpdateLakeFormationIdentityCenterConfiguration-request-ShareRecipients"></a>
A list of AWS account IDs or AWS organization/organizational unit ARNs that are allowed to access to access data managed by Lake Formation.
If the `ShareRecipients` list includes valid values, then the resource share is updated with the principals you want to have access to the resources.
If the `ShareRecipients` value is null, both the list of share recipients and the resource share remain unchanged.
If the `ShareRecipients` value is an empty list, then the existing share recipients list will be cleared, and the resource share will be deleted.
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

## Response Syntax
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_UpdateLakeFormationIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/UpdateLakeFormationIdentityCenterConfiguration)
