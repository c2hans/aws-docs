---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListRLSPolicies.html
---

# ListRLSPolicies
<a name="API_ListRLSPolicies"></a>

Lists the row-level security policies in the Data Catalog.

## Request Syntax
<a name="API_ListRLSPolicies_RequestSyntax"></a>

```
POST /ListRLSPolicies HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRLSPolicies_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRLSPolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRLSPolicies_RequestSyntax) **   <a name="lakeformation-ListRLSPolicies-request-MaxResults"></a>
The maximum number of row-level security policies to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListRLSPolicies_RequestSyntax) **   <a name="lakeformation-ListRLSPolicies-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_ListRLSPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RLSPolicies": [
      {
         "AttachmentColumns": [
            {
               "Name": "string",
               "Type": "string"
            }
         ],
         "CatalogId": "string",
         "FilterExpression": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRLSPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRLSPolicies_ResponseSyntax) **   <a name="lakeformation-ListRLSPolicies-response-NextToken"></a>
A continuation token, if not all row-level security policies have been returned.
Type: String

 ** [RLSPolicies](#API_ListRLSPolicies_ResponseSyntax) **   <a name="lakeformation-ListRLSPolicies-response-RLSPolicies"></a>
A list of `RLSPolicy` structures.
Type: Array of [RLSPolicy](API_RLSPolicy.md) objects

## Errors
<a name="API_ListRLSPolicies_Errors"></a>

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

## See Also
<a name="API_ListRLSPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListRLSPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListRLSPolicies)
