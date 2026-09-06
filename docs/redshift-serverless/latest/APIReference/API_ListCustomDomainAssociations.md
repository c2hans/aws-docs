---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListCustomDomainAssociations.html
---

# ListCustomDomainAssociations
<a name="API_ListCustomDomainAssociations"></a>

 Lists custom domain associations for Amazon Redshift Serverless.

## Request Syntax
<a name="API_ListCustomDomainAssociations_RequestSyntax"></a>

```
{
   "customDomainCertificateArn": "{{string}}",
   "customDomainName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomDomainAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [customDomainCertificateArn](#API_ListCustomDomainAssociations_RequestSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-request-customDomainCertificateArn"></a>
The custom domain name’s certificate Amazon resource name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*.*`
Required: No

 ** [customDomainName](#API_ListCustomDomainAssociations_RequestSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-request-customDomainName"></a>
The custom domain name associated with the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: No

 ** [maxResults](#API_ListCustomDomainAssociations_RequestSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCustomDomainAssociations_RequestSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-request-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListCustomDomainAssociations_ResponseSyntax"></a>

```
{
   "associations": [
      {
         "customDomainCertificateArn": "string",
         "customDomainCertificateExpiryTime": "string",
         "customDomainName": "string",
         "workgroupName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomDomainAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associations](#API_ListCustomDomainAssociations_ResponseSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-response-associations"></a>
A list of Association objects.
Type: Array of [Association](API_Association.md) objects

 ** [nextToken](#API_ListCustomDomainAssociations_ResponseSyntax) **   <a name="redshiftserverless-ListCustomDomainAssociations-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

## Errors
<a name="API_ListCustomDomainAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidPaginationException **
The provided pagination token is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListCustomDomainAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListCustomDomainAssociations)
