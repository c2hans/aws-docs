---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetCustomDomainAssociation.html
---

# GetCustomDomainAssociation
<a name="API_GetCustomDomainAssociation"></a>

Gets information about a specific custom domain association.

## Request Syntax
<a name="API_GetCustomDomainAssociation_RequestSyntax"></a>

```
{
   "customDomainName": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCustomDomainAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [customDomainName](#API_GetCustomDomainAssociation_RequestSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-request-customDomainName"></a>
The custom domain name associated with the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: Yes

 ** [workgroupName](#API_GetCustomDomainAssociation_RequestSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-request-workgroupName"></a>
The name of the workgroup associated with the database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetCustomDomainAssociation_ResponseSyntax"></a>

```
{
   "customDomainCertificateArn": "string",
   "customDomainCertificateExpiryTime": "string",
   "customDomainName": "string",
   "workgroupName": "string"
}
```

## Response Elements
<a name="API_GetCustomDomainAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customDomainCertificateArn](#API_GetCustomDomainAssociation_ResponseSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-response-customDomainCertificateArn"></a>
The custom domain name’s certificate Amazon resource name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*.*`

 ** [customDomainCertificateExpiryTime](#API_GetCustomDomainAssociation_ResponseSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-response-customDomainCertificateExpiryTime"></a>
The expiration time for the certificate.
Type: Timestamp

 ** [customDomainName](#API_GetCustomDomainAssociation_ResponseSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-response-customDomainName"></a>
The custom domain name associated with the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`

 ** [workgroupName](#API_GetCustomDomainAssociation_ResponseSyntax) **   <a name="redshiftserverless-GetCustomDomainAssociation-response-workgroupName"></a>
The name of the workgroup associated with the database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`

## Errors
<a name="API_GetCustomDomainAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetCustomDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetCustomDomainAssociation)
