---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListShareInvitations.html
---

# ListShareInvitations
<a name="API_ListShareInvitations"></a>

List the share invitations.

 `WorkloadNamePrefix`, `LensNamePrefix`, `ProfileNamePrefix`, and `TemplateNamePrefix` are mutually exclusive. Use the parameter that matches your `ShareResourceType`.

## Request Syntax
<a name="API_ListShareInvitations_RequestSyntax"></a>

```
GET /shareInvitations?LensNamePrefix={{LensNamePrefix}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProfileNamePrefix={{ProfileNamePrefix}}&ShareResourceType={{ShareResourceType}}&TemplateNamePrefix={{TemplateNamePrefix}}&WorkloadNamePrefix={{WorkloadNamePrefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListShareInvitations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensNamePrefix](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-LensNamePrefix"></a>
An optional string added to the beginning of each lens name returned in the results.
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [MaxResults](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [ProfileNamePrefix](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-ProfileNamePrefix"></a>
An optional string added to the beginning of each profile name returned in the results.
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [ShareResourceType](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-ShareResourceType"></a>
The type of share invitations to be returned.
Valid Values: `WORKLOAD | LENS | PROFILE | TEMPLATE`

 ** [TemplateNamePrefix](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-TemplateNamePrefix"></a>
An optional string added to the beginning of each review template name returned in the results.
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`

 ** [WorkloadNamePrefix](#API_ListShareInvitations_RequestSyntax) **   <a name="wellarchitected-ListShareInvitations-request-uri-WorkloadNamePrefix"></a>
An optional string added to the beginning of each workload name returned in the results.
Length Constraints: Minimum length of 0. Maximum length of 100.

## Request Body
<a name="API_ListShareInvitations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListShareInvitations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ShareInvitationSummaries": [
      {
         "LensArn": "string",
         "LensName": "string",
         "PermissionType": "string",
         "ProfileArn": "string",
         "ProfileName": "string",
         "SharedBy": "string",
         "SharedWith": "string",
         "ShareInvitationId": "string",
         "ShareResourceType": "string",
         "TemplateArn": "string",
         "TemplateName": "string",
         "WorkloadId": "string",
         "WorkloadName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListShareInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListShareInvitations_ResponseSyntax) **   <a name="wellarchitected-ListShareInvitations-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [ShareInvitationSummaries](#API_ListShareInvitations_ResponseSyntax) **   <a name="wellarchitected-ListShareInvitations-response-ShareInvitationSummaries"></a>
List of share invitation summaries in a workload.
Type: Array of [ShareInvitationSummary](API_ShareInvitationSummary.md) objects

## Errors
<a name="API_ListShareInvitations_Errors"></a>

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
<a name="API_ListShareInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListShareInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListShareInvitations)
