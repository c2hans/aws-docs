---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html
---

# ListAssessments
<a name="API_ListAssessments"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Returns a list of current and past assessments from AWS Audit Manager.

## Request Syntax
<a name="API_ListAssessments_RequestSyntax"></a>

```
GET /assessments?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssessments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAssessments_RequestSyntax) **   <a name="auditmanager-ListAssessments-request-uri-maxResults"></a>
 Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAssessments_RequestSyntax) **   <a name="auditmanager-ListAssessments-request-uri-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

 ** [status](#API_ListAssessments_RequestSyntax) **   <a name="auditmanager-ListAssessments-request-uri-status"></a>
 The current status of the assessment.
Valid Values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_ListAssessments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssessments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentMetadata": [
      {
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
         "id": "string",
         "lastUpdated": number,
         "name": "string",
         "roles": [
            {
               "roleArn": "string",
               "roleType": "string"
            }
         ],
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentMetadata](#API_ListAssessments_ResponseSyntax) **   <a name="auditmanager-ListAssessments-response-assessmentMetadata"></a>
The metadata that the `ListAssessments` API returns for each assessment.
Type: Array of [AssessmentMetadataItem](API_AssessmentMetadataItem.md) objects

 ** [nextToken](#API_ListAssessments_ResponseSyntax) **   <a name="auditmanager-ListAssessments-response-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_ListAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_ListAssessments_Examples"></a>

### Retrieving a list of assessments
<a name="API_ListAssessments_Example_1"></a>

This shows a sample response that the `ListAssessments` operation might return if you had three active assessments.

#### Sample Response
<a name="API_ListAssessments_Example_1_Response"></a>

```
{
    "assessmentMetadata": [
        {
            "name": "my GxP assessment",
            "id": "a1b2c3d4-5678-90ab-cdef-example11111",
            "complianceType": "GxP 21 CFR Part 11",
            "status": "ACTIVE",
            "roles": [
                {
                    "roleType": "PROCESS_OWNER",
                    "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                }
            ],
            "delegations": [],
            "creationTime": "2022-12-20T16:38:09.215000-08:00",
            "lastUpdated": "2022-12-20T16:38:09.397000-08:00"
        },
        {
            "name": "My control tower assessment",
            "id": "a1b2c3d4-5678-90ab-cdef-example22222",
            "complianceType": "AWS Control Tower Guardrails",
            "status": "ACTIVE",
            "roles": [
                {
                    "roleType": "PROCESS_OWNER",
                    "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                }
            ],
            "delegations": [],
            "creationTime": "2022-02-23T10:25:41.083000-08:00",
            "lastUpdated": "2022-02-23T17:06:54.132000-08:00"
        },
        {
            "name": "My PCI DSS assessment",
            "id": "a1b2c3d4-5678-90ab-cdef-example33333",
            "complianceType": "PCI DSS",
            "status": "ACTIVE",
            "roles": [
                {
                    "roleType": "PROCESS_OWNER",
                    "roleArn": "arn:aws:iam::111122223333:role/Administrator"
                }
            ],
            "delegations": [],
            "creationTime": "2022-02-23T09:34:42.850000-08:00",
            "lastUpdated": "2022-02-23T09:34:42.982000-08:00"
        }
    ]
}
```

## See Also
<a name="API_ListAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListAssessments)
