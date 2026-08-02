---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html
---

# UpdateAssessmentStatus
<a name="API_UpdateAssessmentStatus"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Updates the status of an assessment in AWS Audit Manager.

## Request Syntax
<a name="API_UpdateAssessmentStatus_RequestSyntax"></a>

```
PUT /assessments/{{assessmentId}}/status HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssessmentStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_UpdateAssessmentStatus_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentStatus-request-uri-assessmentId"></a>
 The unique identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAssessmentStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateAssessmentStatus_RequestSyntax) **   <a name="auditmanager-UpdateAssessmentStatus-request-status"></a>
 The current status of the assessment.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## Response Syntax
<a name="API_UpdateAssessmentStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessment": {
      "arn": "string",
      "awsAccount": {
         "emailAddress": "string",
         "id": "string",
         "name": "string"
      },
      "framework": {
         "arn": "string",
         "controlSets": [
            {
               "controls": [
                  {
                     "assessmentReportEvidenceCount": number,
                     "comments": [
                        {
                           "authorName": "string",
                           "commentBody": "string",
                           "postedDate": number
                        }
                     ],
                     "description": "string",
                     "evidenceCount": number,
                     "evidenceSources": [ "string" ],
                     "id": "string",
                     "name": "string",
                     "response": "string",
                     "status": "string"
                  }
               ],
               "delegations": [
                  {
                     "assessmentId": "string",
                     "assessmentName": "string",
                     "comment": "string",
                     "controlSetId": "string",
                     "createdBy": "string",
                     "creationTime": number,
                     "id": "string",
                     "lastUpdated": number,
                     "roleArn": "string",
                     "roleType": "string",
                     "status": "string"
                  }
               ],
               "description": "string",
               "id": "string",
               "manualEvidenceCount": number,
               "roles": [
                  {
                     "roleArn": "string",
                     "roleType": "string"
                  }
               ],
               "status": "string",
               "systemEvidenceCount": number
            }
         ],
         "id": "string",
         "metadata": {
            "complianceType": "string",
            "description": "string",
            "logo": "string",
            "name": "string"
         }
      },
      "metadata": {
         "assessmentReportsDestination": {
            "destination": "string",
            "destinationType": "string"
         },
         "complianceType": "string",
         "creationTime": number,
         "delegations": [
            {
               "assessmentId": "string",
               "assessmentName": "string",
               "comment": "string",
               "controlSetId": "string",
               "createdBy": "string",
               "creationTime": number,
               "id": "string",
               "lastUpdated": number,
               "roleArn": "string",
               "roleType": "string",
               "status": "string"
            }
         ],
         "description": "string",
         "id": "string",
         "lastUpdated": number,
         "name": "string",
         "roles": [
            {
               "roleArn": "string",
               "roleType": "string"
            }
         ],
         "scope": {
            "awsAccounts": [
               {
                  "emailAddress": "string",
                  "id": "string",
                  "name": "string"
               }
            ],
            "awsServices": [
               {
                  "serviceName": "string"
               }
            ]
         },
         "status": "string"
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateAssessmentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessment](#API_UpdateAssessmentStatus_ResponseSyntax) **   <a name="auditmanager-UpdateAssessmentStatus-response-assessment"></a>
 The name of the updated assessment that the `UpdateAssessmentStatus` API returned.
Type: [Assessment](API_Assessment.md) object

## Errors
<a name="API_UpdateAssessmentStatus_Errors"></a>

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
<a name="API_UpdateAssessmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/UpdateAssessmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/UpdateAssessmentStatus)
