---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplate.html
---

# UpdateReviewTemplate
<a name="API_UpdateReviewTemplate"></a>

Update a review template.

## Request Syntax
<a name="API_UpdateReviewTemplate_RequestSyntax"></a>

```
PATCH /reviewTemplates/{{TemplateArn}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "LensesToAssociate": [ "{{string}}" ],
   "LensesToDisassociate": [ "{{string}}" ],
   "Notes": "{{string}}",
   "TemplateName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateReviewTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateArn](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-uri-TemplateArn"></a>
The review template ARN.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_UpdateReviewTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-Description"></a>
The review template description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

 ** [LensesToAssociate](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-LensesToAssociate"></a>
A list of lens aliases or ARNs to apply to the review template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [LensesToDisassociate](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-LensesToDisassociate"></a>
A list of lens aliases or ARNs to unapply to the review template. The `wellarchitected` lens cannot be unapplied.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Notes](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Required: No

 ** [TemplateName](#API_UpdateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-request-TemplateName"></a>
The review template name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

## Response Syntax
<a name="API_UpdateReviewTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ReviewTemplate": {
      "Description": "string",
      "Lenses": [ "string" ],
      "Notes": "string",
      "Owner": "string",
      "QuestionCounts": {
         "string" : number
      },
      "ShareInvitationId": "string",
      "Tags": {
         "string" : "string"
      },
      "TemplateArn": "string",
      "TemplateName": "string",
      "UpdatedAt": number,
      "UpdateStatus": "string"
   }
}
```

## Response Elements
<a name="API_UpdateReviewTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReviewTemplate](#API_UpdateReviewTemplate_ResponseSyntax) **   <a name="wellarchitected-UpdateReviewTemplate-response-ReviewTemplate"></a>
A review template.
Type: [ReviewTemplate](API_ReviewTemplate.md) object

## Errors
<a name="API_UpdateReviewTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_UpdateReviewTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateReviewTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateReviewTemplate)
