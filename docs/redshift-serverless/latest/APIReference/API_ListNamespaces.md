---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListNamespaces.html
---

# ListNamespaces
<a name="API_ListNamespaces"></a>

Returns information about a list of specified namespaces.

## Request Syntax
<a name="API_ListNamespaces_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNamespaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListNamespaces_RequestSyntax) **   <a name="redshiftserverless-ListNamespaces-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListNamespaces_RequestSyntax) **   <a name="redshiftserverless-ListNamespaces-request-nextToken"></a>
If your initial `ListNamespaces` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListNamespaces` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_ListNamespaces_ResponseSyntax"></a>

```
{
   "namespaces": [
      {
         "adminPasswordSecretArn": "string",
         "adminPasswordSecretKmsKeyId": "string",
         "adminUsername": "string",
         "catalogArn": "string",
         "creationDate": "string",
         "dbName": "string",
         "defaultIamRoleArn": "string",
         "iamRoles": [ "string" ],
         "kmsKeyId": "string",
         "lakehouseRegistrationStatus": "string",
         "logExports": [ "string" ],
         "namespaceArn": "string",
         "namespaceId": "string",
         "namespaceName": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespaces](#API_ListNamespaces_ResponseSyntax) **   <a name="redshiftserverless-ListNamespaces-response-namespaces"></a>
The list of returned namespaces.
Type: Array of [Namespace](API_Namespace.md) objects

 ** [nextToken](#API_ListNamespaces_ResponseSyntax) **   <a name="redshiftserverless-ListNamespaces-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListNamespaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListNamespaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListNamespaces)
