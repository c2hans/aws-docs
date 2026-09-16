---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListIncidentFindings.html
---

# ListIncidentFindings
<a name="API_ListIncidentFindings"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves a list of the IDs of findings, plus their last modified times, that have been identified for a specified incident. A finding represents a recent application environment change made by an AWS CloudFormation stack creation or update or an AWS CodeDeploy deployment that can be investigated as a potential cause of the incident.

## Request Syntax
<a name="API_ListIncidentFindings_RequestSyntax"></a>

```
POST /listIncidentFindings HTTP/1.1
Content-type: application/json

{
   "incidentRecordArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIncidentFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIncidentFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [incidentRecordArn](#API_ListIncidentFindings_RequestSyntax) **   <a name="IncidentManager-ListIncidentFindings-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident for which you want to view associated findings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [maxResults](#API_ListIncidentFindings_RequestSyntax) **   <a name="IncidentManager-ListIncidentFindings-request-maxResults"></a>
The maximum number of findings to retrieve per call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [nextToken](#API_ListIncidentFindings_RequestSyntax) **   <a name="IncidentManager-ListIncidentFindings-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListIncidentFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "id": "string",
         "lastModifiedTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIncidentFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_ListIncidentFindings_ResponseSyntax) **   <a name="IncidentManager-ListIncidentFindings-response-findings"></a>
A list of findings that represent deployments that might be the potential cause of the incident.
Type: Array of [FindingSummary](API_FindingSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListIncidentFindings_ResponseSyntax) **   <a name="IncidentManager-ListIncidentFindings-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

## Errors
<a name="API_ListIncidentFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListIncidentFindings_Examples"></a>

### Example
<a name="API_ListIncidentFindings_Example_1"></a>

This example illustrates one usage of ListIncidentFindings.

#### Sample Request
<a name="API_ListIncidentFindings_Example_1_Request"></a>

```
POST /listIncidentFindings HTTP/1.1
Host: ssm-incidents.us-east-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-incident-findings
X-Amz-Date: 20231210T104650Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20231210/us-east-2/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 113

{
  "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/my-incident/c6c59324-8fee-34eb-2ea1-1a279EXAMPLE"
}
```

#### Sample Response
<a name="API_ListIncidentFindings_Example_1_Response"></a>

```
{
  "findings": [
    {
      "id": "92c59324-ad98-c955-ebe1-35779EXAMPLE",
      "lastModifiedTime": "2023-12-13T10:47:03.560000+11:00"
    },
    {
      "id": "96c59324-ad98-2f5b-f74b-b6c3aEXAMPLE",
      "lastModifiedTime": "2023-12-13T10:47:03.560000+11:00"
    }
  ]
}
```

## See Also
<a name="API_ListIncidentFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListIncidentFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListIncidentFindings)
