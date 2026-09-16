---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfiles.html
---

# ListProfiles
<a name="API_ListProfiles"></a>

List profiles.

## Request Syntax
<a name="API_ListProfiles_RequestSyntax"></a>

```
GET /profileSummaries?MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProfileNamePrefix={{ProfileNamePrefix}}&ProfileOwnerType={{ProfileOwnerType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListProfiles_RequestSyntax) **   <a name="wellarchitected-ListProfiles-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListProfiles_RequestSyntax) **   <a name="wellarchitected-ListProfiles-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

 ** [ProfileNamePrefix](#API_ListProfiles_RequestSyntax) **   <a name="wellarchitected-ListProfiles-request-uri-ProfileNamePrefix"></a>
An optional string added to the beginning of each profile name returned in the results.
Length Constraints: Maximum length of 100.

 ** [ProfileOwnerType](#API_ListProfiles_RequestSyntax) **   <a name="wellarchitected-ListProfiles-request-uri-ProfileOwnerType"></a>
Profile owner type.
Valid Values: `SELF | SHARED`

## Request Body
<a name="API_ListProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProfileSummaries": [
      {
         "CreatedAt": number,
         "Owner": "string",
         "ProfileArn": "string",
         "ProfileDescription": "string",
         "ProfileName": "string",
         "ProfileVersion": "string",
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProfiles_ResponseSyntax) **   <a name="wellarchitected-ListProfiles-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [ProfileSummaries](#API_ListProfiles_ResponseSyntax) **   <a name="wellarchitected-ListProfiles-response-ProfileSummaries"></a>
Profile summaries.
Type: Array of [ProfileSummary](API_ProfileSummary.md) objects

## Errors
<a name="API_ListProfiles_Errors"></a>

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
<a name="API_ListProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListProfiles)
