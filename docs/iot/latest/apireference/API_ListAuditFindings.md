---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditFindings.html
---

# ListAuditFindings
<a name="API_ListAuditFindings"></a>

Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 90 days.)

Requires permission to access the [ListAuditFindings](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAuditFindings_RequestSyntax"></a>

```
POST /audit/findings HTTP/1.1
Content-type: application/json

{
   "checkName": "{{string}}",
   "endTime": {{number}},
   "listSuppressedFindings": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceIdentifier": {
      "account": "{{string}}",
      "caCertificateId": "{{string}}",
      "clientId": "{{string}}",
      "cognitoIdentityPoolId": "{{string}}",
      "deviceCertificateArn": "{{string}}",
      "deviceCertificateId": "{{string}}",
      "iamRoleArn": "{{string}}",
      "issuerCertificateIdentifier": {
         "issuerCertificateSerialNumber": "{{string}}",
         "issuerCertificateSubject": "{{string}}",
         "issuerId": "{{string}}"
      },
      "policyVersionIdentifier": {
         "policyName": "{{string}}",
         "policyVersionId": "{{string}}"
      },
      "roleAliasArn": "{{string}}"
   },
   "startTime": {{number}},
   "taskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAuditFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAuditFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [checkName](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-checkName"></a>
A filter to limit results to the findings for the specified audit check.
Type: String
Required: No

 ** [endTime](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-endTime"></a>
A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.
Type: Timestamp
Required: No

 ** [listSuppressedFindings](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-listSuppressedFindings"></a>
 Boolean flag indicating whether only the suppressed findings or the unsuppressed findings should be listed. If this parameter isn't provided, the response will list both suppressed and unsuppressed findings.
Type: Boolean
Required: No

 ** [maxResults](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [nextToken](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-nextToken"></a>
The token for the next set of results.
Type: String
Required: No

 ** [resourceIdentifier](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-resourceIdentifier"></a>
Information identifying the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

 ** [startTime](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-startTime"></a>
A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.
Type: Timestamp
Required: No

 ** [taskId](#API_ListAuditFindings_RequestSyntax) **   <a name="iot-ListAuditFindings-request-taskId"></a>
A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

## Response Syntax
<a name="API_ListAuditFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "checkName": "string",
         "findingId": "string",
         "findingTime": number,
         "isSuppressed": boolean,
         "nonCompliantResource": {
            "additionalInfo": {
               "string" : "string"
            },
            "resourceIdentifier": {
               "account": "string",
               "caCertificateId": "string",
               "clientId": "string",
               "cognitoIdentityPoolId": "string",
               "deviceCertificateArn": "string",
               "deviceCertificateId": "string",
               "iamRoleArn": "string",
               "issuerCertificateIdentifier": {
                  "issuerCertificateSerialNumber": "string",
                  "issuerCertificateSubject": "string",
                  "issuerId": "string"
               },
               "policyVersionIdentifier": {
                  "policyName": "string",
                  "policyVersionId": "string"
               },
               "roleAliasArn": "string"
            },
            "resourceType": "string"
         },
         "reasonForNonCompliance": "string",
         "reasonForNonComplianceCode": "string",
         "relatedResources": [
            {
               "additionalInfo": {
                  "string" : "string"
               },
               "resourceIdentifier": {
                  "account": "string",
                  "caCertificateId": "string",
                  "clientId": "string",
                  "cognitoIdentityPoolId": "string",
                  "deviceCertificateArn": "string",
                  "deviceCertificateId": "string",
                  "iamRoleArn": "string",
                  "issuerCertificateIdentifier": {
                     "issuerCertificateSerialNumber": "string",
                     "issuerCertificateSubject": "string",
                     "issuerId": "string"
                  },
                  "policyVersionIdentifier": {
                     "policyName": "string",
                     "policyVersionId": "string"
                  },
                  "roleAliasArn": "string"
               },
               "resourceType": "string"
            }
         ],
         "severity": "string",
         "taskId": "string",
         "taskStartTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAuditFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_ListAuditFindings_ResponseSyntax) **   <a name="iot-ListAuditFindings-response-findings"></a>
The findings (results) of the audit.
Type: Array of [AuditFinding](API_AuditFinding.md) objects

 ** [nextToken](#API_ListAuditFindings_ResponseSyntax) **   <a name="iot-ListAuditFindings-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListAuditFindings_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAuditFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAuditFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAuditFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
