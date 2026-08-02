---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetResourcePolicies.html
---

# GetResourcePolicies
<a name="API_GetResourcePolicies"></a>

Retrieves the resource policies set on individual resources by AWS Resource Access Manager during cross-account permission grants. Also retrieves the Data Catalog resource policy.

If you enabled metadata encryption in Data Catalog settings, and you do not have permission on the AWS KMS key, the operation can't return the Data Catalog resource policy.

## Request Syntax
<a name="API_GetResourcePolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourcePolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetResourcePolicies_RequestSyntax) **   <a name="Glue-GetResourcePolicies-request-MaxResults"></a>
The maximum size of a list to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetResourcePolicies_RequestSyntax) **   <a name="Glue-GetResourcePolicies-request-NextToken"></a>
A continuation token, if this is a continuation request.
Type: String
Required: No

## Response Syntax
<a name="API_GetResourcePolicies_ResponseSyntax"></a>

```
{
   "GetResourcePoliciesResponseList": [
      {
         "CreateTime": number,
         "PolicyHash": "string",
         "PolicyInJson": "string",
         "UpdateTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GetResourcePoliciesResponseList](#API_GetResourcePolicies_ResponseSyntax) **   <a name="Glue-GetResourcePolicies-response-GetResourcePoliciesResponseList"></a>
A list of the individual resource policies and the account-level resource policy.
Type: Array of [GluePolicy](API_GluePolicy.md) objects

 ** [NextToken](#API_GetResourcePolicies_ResponseSyntax) **   <a name="Glue-GetResourcePolicies-response-NextToken"></a>
A continuation token, if the returned list does not contain the last resource policy available.
Type: String

## Errors
<a name="API_GetResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetResourcePolicies)
