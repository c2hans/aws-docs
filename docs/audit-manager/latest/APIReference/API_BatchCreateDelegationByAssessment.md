---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchCreateDelegationByAssessment.html
---

# BatchCreateDelegationByAssessment
<a name="API_BatchCreateDelegationByAssessment"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Creates a batch of delegations for an assessment in AWS Audit Manager.

## Request Syntax
<a name="API_BatchCreateDelegationByAssessment_RequestSyntax"></a>

```
POST /assessments/{{assessmentId}}/delegations HTTP/1.1
Content-type: application/json

{
   "createDelegationRequests": [
      {
         "comment": "{{string}}",
         "controlSetId": "{{string}}",
         "roleArn": "{{string}}",
         "roleType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateDelegationByAssessment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_BatchCreateDelegationByAssessment_RequestSyntax) **   <a name="auditmanager-BatchCreateDelegationByAssessment-request-uri-assessmentId"></a>
 The identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_BatchCreateDelegationByAssessment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [createDelegationRequests](#API_BatchCreateDelegationByAssessment_RequestSyntax) **   <a name="auditmanager-BatchCreateDelegationByAssessment-request-createDelegationRequests"></a>
 The API request to batch create delegations in Audit Manager.
Type: Array of [CreateDelegationRequest](API_CreateDelegationRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchCreateDelegationByAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
   "errors": [
      {
         "createDelegationRequest": {
            "comment": "string",
            "controlSetId": "string",
            "roleArn": "string",
            "roleType": "string"
         },
         "errorCode": "string",
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateDelegationByAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [delegations](#API_BatchCreateDelegationByAssessment_ResponseSyntax) **   <a name="auditmanager-BatchCreateDelegationByAssessment-response-delegations"></a>
 The delegations that are associated with the assessment.
Type: Array of [Delegation](API_Delegation.md) objects

 ** [errors](#API_BatchCreateDelegationByAssessment_ResponseSyntax) **   <a name="auditmanager-BatchCreateDelegationByAssessment-response-errors"></a>
 A list of errors that the `BatchCreateDelegationByAssessment` API returned.
Type: Array of [BatchCreateDelegationByAssessmentError](API_BatchCreateDelegationByAssessmentError.md) objects

## Errors
<a name="API_BatchCreateDelegationByAssessment_Errors"></a>

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
<a name="API_BatchCreateDelegationByAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/BatchCreateDelegationByAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
