---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityConfigs.html
---

# ListSecurityConfigs
<a name="API_ListSecurityConfigs"></a>

Returns information about configured OpenSearch Serverless security configurations. For more information, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

## Request Syntax
<a name="API_ListSecurityConfigs_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSecurityConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSecurityConfigs_RequestSyntax) **   <a name="opensearchserverless-ListSecurityConfigs-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSecurityConfigs_RequestSyntax) **   <a name="opensearchserverless-ListSecurityConfigs-request-nextToken"></a>
If your initial `ListSecurityConfigs` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListSecurityConfigs` operations, which returns results in the next page.
Type: String
Required: No

 ** [type](#API_ListSecurityConfigs_RequestSyntax) **   <a name="opensearchserverless-ListSecurityConfigs-request-type"></a>
The type of security configuration.
Type: String
Valid Values: `saml | iamidentitycenter | iamfederation`
Required: Yes

## Response Syntax
<a name="API_ListSecurityConfigs_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "securityConfigSummaries": [
      {
         "configVersion": "string",
         "createdDate": number,
         "description": "string",
         "id": "string",
         "lastModifiedDate": number,
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSecurityConfigs_ResponseSyntax) **   <a name="opensearchserverless-ListSecurityConfigs-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

 ** [securityConfigSummaries](#API_ListSecurityConfigs_ResponseSyntax) **   <a name="opensearchserverless-ListSecurityConfigs-response-securityConfigSummaries"></a>
Details about the security configurations in your account.
Type: Array of [SecurityConfigSummary](API_SecurityConfigSummary.md) objects

## Errors
<a name="API_ListSecurityConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListSecurityConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListSecurityConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListSecurityConfigs)
