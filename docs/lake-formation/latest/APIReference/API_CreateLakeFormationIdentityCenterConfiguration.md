---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLakeFormationIdentityCenterConfiguration.html
---

# CreateLakeFormationIdentityCenterConfiguration
<a name="API_CreateLakeFormationIdentityCenterConfiguration"></a>

Creates an IAM Identity Center connection with Lake Formation to allow IAM Identity Center users and groups to access Data Catalog resources.

## Request Syntax
<a name="API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax"></a>

```
POST /CreateLakeFormationIdentityCenterConfiguration HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "ExternalFiltering": {
      "AuthorizedTargets": [ "{{string}}" ],
      "Status": "{{string}}"
   },
   "InstanceArn": "{{string}}",
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
<a name="API_CreateLakeFormationIdentityCenterConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLakeFormationIdentityCenterConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ExternalFiltering](#API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-request-ExternalFiltering"></a>
A list of the account IDs of AWS accounts of third-party applications that are allowed to access data managed by Lake Formation.
Type: [ExternalFilteringConfiguration](API_ExternalFilteringConfiguration.md) object
Required: No

 ** [InstanceArn](#API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance for which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.
Type: String
Required: No

 ** [ServiceIntegrations](#API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-request-ServiceIntegrations"></a>
A list of service integrations for enabling trusted identity propagation with external services such as Redshift.
Type: Array of [ServiceIntegrationUnion](API_ServiceIntegrationUnion.md) objects
Required: No

 ** [ShareRecipients](#API_CreateLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-request-ShareRecipients"></a>
A list of AWS account IDs and/or AWS organization/organizational unit ARNs that are allowed to access data managed by Lake Formation.
If the `ShareRecipients` list includes valid values, a resource share is created with the principals you want to have access to the resources.
If the `ShareRecipients` value is null or the list is empty, no resource share is created.
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

## Response Syntax
<a name="API_CreateLakeFormationIdentityCenterConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationArn": "string"
}
```

## Response Elements
<a name="API_CreateLakeFormationIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_CreateLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-CreateLakeFormationIdentityCenterConfiguration-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the Lake Formation application integrated with IAM Identity Center.
Type: String

## Errors
<a name="API_CreateLakeFormationIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
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

## Examples
<a name="API_CreateLakeFormationIdentityCenterConfiguration_Examples"></a>

### Request example
<a name="API_CreateLakeFormationIdentityCenterConfiguration_Example_1"></a>

This example illustrates one usage of CreateLakeFormationIdentityCenterConfiguration.

```
{
   "CatalogId": "123456789012",
   "ExternalFiltering": {
      "AuthorizedTargets": [ "<app arn1>" ],
      "Status": "ENABLED"
   },
   "InstanceArn": "arn:aws:sso:::instance/ssoins-1223f2dba9f23211",
    "ShareRecipients": [
      {
         "DataLakePrincipalIdentifier": "555555555555"
      }
   ],
   "ServiceIntegrations": [
      {
         "Redshift": [
            {
               "RedshiftConnect": {
                  "Authorization": "ENABLED"
               }
            }
         ]
      }
   ]
}
```

### Response example
<a name="API_CreateLakeFormationIdentityCenterConfiguration_Example_2"></a>

This example illustrates one usage of CreateLakeFormationIdentityCenterConfiguration.

```
{
   "ApplicationArn": "arn:aws:sso::123456789012:application/ssoins-1223f2dba9f23211/apl-8effb002e2841417"
   "ResourceShare": "arn:aws:ram:us-east-1:123456789012:resource-share/2b5032f6-19e4-461e-8b02-cd711d119df7"
}
```

## See Also
<a name="API_CreateLakeFormationIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/CreateLakeFormationIdentityCenterConfiguration)
