---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeLakeFormationIdentityCenterConfiguration.html
---

# DescribeLakeFormationIdentityCenterConfiguration
<a name="API_DescribeLakeFormationIdentityCenterConfiguration"></a>

Retrieves the instance ARN and application ARN for the connection.

## Request Syntax
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_RequestSyntax"></a>

```
POST /DescribeLakeFormationIdentityCenterConfiguration HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_DescribeLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationArn": "string",
   "CatalogId": "string",
   "ExternalFiltering": {
      "AuthorizedTargets": [ "string" ],
      "Status": "string"
   },
   "InstanceArn": "string",
   "ResourceShare": "string",
   "ServiceIntegrations": [
      { ... }
   ],
   "ShareRecipients": [
      {
         "DataLakePrincipalIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the Lake Formation application integrated with IAM Identity Center.
Type: String

 ** [CatalogId](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [ExternalFiltering](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-ExternalFiltering"></a>
Indicates if external filtering is enabled.
Type: [ExternalFilteringConfiguration](API_ExternalFilteringConfiguration.md) object

 ** [InstanceArn](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-InstanceArn"></a>
The Amazon Resource Name (ARN) of the connection.
Type: String

 ** [ResourceShare](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-ResourceShare"></a>
The Amazon Resource Name (ARN) of the RAM share.
Type: String

 ** [ServiceIntegrations](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-ServiceIntegrations"></a>
A list of service integrations for enabling trusted identity propagation with external services such as Redshift.
Type: Array of [ServiceIntegrationUnion](API_ServiceIntegrationUnion.md) objects

 ** [ShareRecipients](#API_DescribeLakeFormationIdentityCenterConfiguration_ResponseSyntax) **   <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration-response-ShareRecipients"></a>
A list of AWS account IDs or AWS organization/organizational unit ARNs that are allowed to access data managed by Lake Formation.
If the `ShareRecipients` list includes valid values, a resource share is created with the principals you want to have access to the resources as the `ShareRecipients`.
If the `ShareRecipients` value is null or the list is empty, no resource share is created.
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

## Errors
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

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

## Examples
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_Examples"></a>

### Response example
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_Example_1"></a>

This example illustrates one usage of DescribeLakeFormationIdentityCenterConfiguration.

```
{
    "CatalogId": "123456789012",
    "InstanceArn": "arn:aws:sso:::instance/ssoins-1223f2dba9f23211",
    "ApplicationArn": "arn:aws:sso::123456789012:application/ssoins-1223f2dba9f23211/apl-8effb002e2841417",
    "ShareRecipients": [
        {
            "DataLakePrincipalIdentifier": "555555555555"
        },
        {
            "DataLakePrincipalIdentifier": "444455556666"
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
    ],
    "ResourceShare": "arn:aws:ram:us-east-1:123456789012:resource-share/2b5032f6-19e4-461e-8b02-cd711d119df7"
}
```

## See Also
<a name="API_DescribeLakeFormationIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DescribeLakeFormationIdentityCenterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
