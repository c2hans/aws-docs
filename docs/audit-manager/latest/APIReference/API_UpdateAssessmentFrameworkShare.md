---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFrameworkShare.html
---

# UpdateAssessmentFrameworkShare
<a name="API_UpdateAssessmentFrameworkShare"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Updates a share request for a custom framework in AWS Audit Manager.

## Request Syntax
<a name="API_UpdateAssessmentFrameworkShare_RequestSyntax"></a>

```
PUT /assessmentFrameworkShareRequests/{{requestId}} HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "requestType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssessmentFrameworkShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [requestId](#API_UpdateAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFrameworkShare-request-uri-requestId"></a>
 The unique identifier for the share request.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAssessmentFrameworkShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdateAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFrameworkShare-request-action"></a>
Specifies the update action for the share request.
Type: String
Valid Values: `ACCEPT | DECLINE | REVOKE`
Required: Yes

 ** [requestType](#API_UpdateAssessmentFrameworkShare_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentFrameworkShare-request-requestType"></a>
Specifies whether the share request is a sent request or a received request.
Type: String
Valid Values: `SENT | RECEIVED`
Required: Yes

## Response Syntax
<a name="API_UpdateAssessmentFrameworkShare_ResponseSyntax"></a>

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
<a name="API_UpdateAssessmentFrameworkShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentFrameworkShareRequest](#API_UpdateAssessmentFrameworkShare_ResponseSyntax) **   <a name="auditmanager-UpdateAssessmentFrameworkShare-response-assessmentFrameworkShareRequest"></a>
 The updated share request that's returned by the `UpdateAssessmentFrameworkShare` operation.
Type: [AssessmentFrameworkShareRequest](API_AssessmentFrameworkShareRequest.md) object

## Errors
<a name="API_UpdateAssessmentFrameworkShare_Errors"></a>

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

 ** ServiceQuotaExceededException **
You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or [request a quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) from the Service Quotas console. For a list of Audit Manager service quotas, see [Quotas and restrictions for AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html).
HTTP Status Code: 402

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAssessmentFrameworkShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/UpdateAssessmentFrameworkShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
