---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html
---

# ListAssessmentFrameworks
<a name="API_ListAssessmentFrameworks"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Returns a list of the frameworks that are available in the Audit Manager framework library.

## Request Syntax
<a name="API_ListAssessmentFrameworks_RequestSyntax"></a>

```
GET /assessmentFrameworks?frameworkType={{frameworkType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssessmentFrameworks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [frameworkType](#API_ListAssessmentFrameworks_RequestSyntax) **   <a name="auditmanager-ListAssessmentFrameworks-request-uri-frameworkType"></a>
 The type of framework, such as a standard framework or a custom framework.
Valid Values: `Standard | Custom`
Required: Yes

 ** [maxResults](#API_ListAssessmentFrameworks_RequestSyntax) **   <a name="auditmanager-ListAssessmentFrameworks-request-uri-maxResults"></a>
 Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAssessmentFrameworks_RequestSyntax) **   <a name="auditmanager-ListAssessmentFrameworks-request-uri-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Request Body
<a name="API_ListAssessmentFrameworks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssessmentFrameworks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "frameworkMetadataList": [
      {
         "arn": "string",
         "complianceType": "string",
         "controlsCount": number,
         "controlSetsCount": number,
         "createdAt": number,
         "description": "string",
         "id": "string",
         "lastUpdatedAt": number,
         "logo": "string",
         "name": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessmentFrameworks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [frameworkMetadataList](#API_ListAssessmentFrameworks_ResponseSyntax) **   <a name="auditmanager-ListAssessmentFrameworks-response-frameworkMetadataList"></a>
 A list of metadata that the `ListAssessmentFrameworks` API returns for each framework.
Type: Array of [AssessmentFrameworkMetadata](API_AssessmentFrameworkMetadata.md) objects

 ** [nextToken](#API_ListAssessmentFrameworks_ResponseSyntax) **   <a name="auditmanager-ListAssessmentFrameworks-response-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_ListAssessmentFrameworks_Errors"></a>

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
<a name="API_ListAssessmentFrameworks_Examples"></a>

### Retrieving a list of custom frameworks
<a name="API_ListAssessmentFrameworks_Example_1"></a>

This shows a sample response that the `ListAssessmentFrameworks` operation might return if you had two custom frameworks in your AWS account.

#### Sample Response
<a name="API_ListAssessmentFrameworks_Example_1_Response"></a>

```
{
    "frameworkMetadataList": [
        {
            "arn": "arn:aws:auditmanager:us-east-1:111122223333:assessmentFramework/a1b2c3d4-5678-90ab-cdef-example11111",
            "id": "a1b2c3d4-5678-90ab-cdef-example11111",
            "type": "Custom",
            "name": "My custom framework",
            "description": "My custom framework for internal audits",
            "complianceType": "Internal",
            "controlsCount": 3,
            "controlSetsCount": 1,
            "createdAt": "2022-03-29T14:57:31.634000-07:00",
            "lastUpdatedAt": "2022-03-29T14:57:31.635000-07:00"
        },
        {
            "arn": "arn:aws:auditmanager:us-east-1:111122223333:assessmentFramework/a1b2c3d4-5678-90ab-cdef-example22222",
            "id": "a1b2c3d4-5678-90ab-cdef-example22222",
            "type": "Custom",
            "name": "My custom HIPAA framework",
            "description": "My custom framework for HIPAA audits",
            "complianceType": "HIPAA",
            "controlsCount": 4,
            "controlSetsCount": 2,
            "createdAt": "2021-03-02T16:35:24.177000-08:00",
            "lastUpdatedAt": "2022-01-10T14:32:18.855000-08:00"
        }
    ]
}
```

## See Also
<a name="API_ListAssessmentFrameworks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListAssessmentFrameworks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListAssessmentFrameworks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
