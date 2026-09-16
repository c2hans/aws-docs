---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_StartAssessmentFrameworkShare.html
---

# StartAssessmentFrameworkShare
<a name="API_StartAssessmentFrameworkShare"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Creates a share request for a custom framework in AWS Audit Manager.

The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to accept or decline the request. If no action is taken, the share request expires.

When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) AWS Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) AWS Region.

Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:
+ The sender revokes the share request.
+ The recipient declines the share request.
+ The recipient encounters an error and doesn't successfully accept the share request.
+ The share request expires before the recipient responds to the request.

When a sender [resends a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend), the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework.

When a recipient accepts a share request, the snapshot is replicated into their AWS account under the AWS Region that was specified in the share request.

**Important**
When you invoke the `StartAssessmentFrameworkShare` API, you are about to share a custom framework with another AWS account. You may not share a custom framework that is derived from a standard framework if the standard framework is designated as not eligible for sharing by AWS, unless you have obtained permission to do so from the owner of the standard framework. To learn more about which standard frameworks are eligible for sharing, see [Framework sharing eligibility](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility) in the * AWS Audit Manager User Guide*.

## Request Syntax
<a name="API_StartAssessmentFrameworkShare_RequestSyntax"></a>

```
POST /assessmentFrameworks/{{frameworkId}}/shareRequests HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "destinationAccount": "{{string}}",
   "destinationRegion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartAssessmentFrameworkShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [frameworkId](#API_StartAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-StartAssessmentFrameworkShare-request-uri-frameworkId"></a>
 The unique identifier for the custom framework to be shared.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_StartAssessmentFrameworkShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_StartAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-StartAssessmentFrameworkShare-request-comment"></a>
 An optional comment from the sender about the share request.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** [destinationAccount](#API_StartAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-StartAssessmentFrameworkShare-request-destinationAccount"></a>
 The AWS account of the recipient.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [destinationRegion](#API_StartAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-StartAssessmentFrameworkShare-request-destinationRegion"></a>
 The AWS Region of the recipient.
Type: String
Pattern: `^[a-z]{2}-[a-z]+-[0-9]{1}$`
Required: Yes

## Response Syntax
<a name="API_StartAssessmentFrameworkShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentFrameworkShareRequest": {
      "comment": "string",
      "complianceType": "string",
      "creationTime": number,
      "customControlsCount": number,
      "destinationAccount": "string",
      "destinationRegion": "string",
      "expirationTime": number,
      "frameworkDescription": "string",
      "frameworkId": "string",
      "frameworkName": "string",
      "id": "string",
      "lastUpdated": number,
      "sourceAccount": "string",
      "standardControlsCount": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_StartAssessmentFrameworkShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentFrameworkShareRequest](#API_StartAssessmentFrameworkShare_ResponseSyntax) **   <a name="auditmanager-StartAssessmentFrameworkShare-response-assessmentFrameworkShareRequest"></a>
 The share request that's created by the `StartAssessmentFrameworkShare` API.
Type: [AssessmentFrameworkShareRequest](API_AssessmentFrameworkShareRequest.md) object

## Errors
<a name="API_StartAssessmentFrameworkShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_StartAssessmentFrameworkShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/StartAssessmentFrameworkShare)
