---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLenses.html
---

# ListLenses
<a name="API_ListLenses"></a>

List the available lenses.

## Request Syntax
<a name="API_ListLenses_RequestSyntax"></a>

```
GET /lenses?LensName={{LensName}}&LensStatus={{LensStatus}}&LensType={{LensType}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLenses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensName](#API_ListLenses_RequestSyntax) **   <a name="wellarchitected-ListLenses-request-uri-LensName"></a>
The full name of the lens.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [LensStatus](#API_ListLenses_RequestSyntax) **   <a name="wellarchitected-ListLenses-request-uri-LensStatus"></a>
The status of lenses to be returned.
Valid Values: `ALL | DRAFT | PUBLISHED`

 ** [LensType](#API_ListLenses_RequestSyntax) **   <a name="wellarchitected-ListLenses-request-uri-LensType"></a>
The type of lenses to be returned.
Valid Values: `AWS_OFFICIAL | CUSTOM_SHARED | CUSTOM_SELF`

 ** [MaxResults](#API_ListLenses_RequestSyntax) **   <a name="wellarchitected-ListLenses-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListLenses_RequestSyntax) **   <a name="wellarchitected-ListLenses-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

## Request Body
<a name="API_ListLenses_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLenses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LensSummaries": [
      {
         "CreatedAt": number,
         "Description": "string",
         "LensAlias": "string",
         "LensArn": "string",
         "LensName": "string",
         "LensStatus": "string",
         "LensType": "string",
         "LensVersion": "string",
         "Owner": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLenses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LensSummaries](#API_ListLenses_ResponseSyntax) **   <a name="wellarchitected-ListLenses-response-LensSummaries"></a>
List of lens summaries of available lenses.
Type: Array of [LensSummary](API_LensSummary.md) objects

 ** [NextToken](#API_ListLenses_ResponseSyntax) **   <a name="wellarchitected-ListLenses-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListLenses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListLenses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListLenses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListLenses)
