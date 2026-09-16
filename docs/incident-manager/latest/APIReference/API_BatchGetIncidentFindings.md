---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_BatchGetIncidentFindings.html
---

# BatchGetIncidentFindings
<a name="API_BatchGetIncidentFindings"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves details about all specified findings for an incident, including descriptive details about each finding. A finding represents a recent application environment change made by an AWS CodeDeploy deployment or an AWS CloudFormation stack creation or update that can be investigated as a potential cause of the incident.

## Request Syntax
<a name="API_BatchGetIncidentFindings_RequestSyntax"></a>

```
POST /batchGetIncidentFindings HTTP/1.1
Content-type: application/json

{
   "findingIds": [ "{{string}}" ],
   "incidentRecordArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchGetIncidentFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetIncidentFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingIds](#API_BatchGetIncidentFindings_RequestSyntax) **   <a name="IncidentManager-BatchGetIncidentFindings-request-findingIds"></a>
A list of IDs of findings for which you want to view details.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** [incidentRecordArn](#API_BatchGetIncidentFindings_RequestSyntax) **   <a name="IncidentManager-BatchGetIncidentFindings-request-incidentRecordArn"></a>
The Amazon Resource Name (ARN) of the incident for which you want to view finding details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_BatchGetIncidentFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "findingId": "string",
         "message": "string"
      }
   ],
   "findings": [
      {
         "creationTime": number,
         "details": { ... },
         "id": "string",
         "lastModifiedTime": number
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetIncidentFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetIncidentFindings_ResponseSyntax) **   <a name="IncidentManager-BatchGetIncidentFindings-response-errors"></a>
A list of errors encountered during the operation.
Type: Array of [BatchGetIncidentFindingsError](API_BatchGetIncidentFindingsError.md) objects

 ** [findings](#API_BatchGetIncidentFindings_ResponseSyntax) **   <a name="IncidentManager-BatchGetIncidentFindings-response-findings"></a>
Information about the requested findings.
Type: Array of [Finding](API_Finding.md) objects

## Errors
<a name="API_BatchGetIncidentFindings_Errors"></a>

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
<a name="API_BatchGetIncidentFindings_Examples"></a>

### Example
<a name="API_BatchGetIncidentFindings_Example_1"></a>

This example illustrates one usage of BatchGetIncidentFindings.

#### Sample Request
<a name="API_BatchGetIncidentFindings_Example_1_Request"></a>

```
POST /batchGetIncidentFindings HTTP/1.1
Host: ssm-incidents.us-east-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.batch-get-incident-findings
X-Amz-Date: 20231210T104650Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20231210/us-east-2/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 154

{
  "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/my-incident/c6c59324-8fee-34eb-2ea1-1a279EXAMPLE",
  "findingIds": [
    "08c5c945-b204-adaa-f0ef-2f212INVALID",
    "92c59324-ad98-c955-ebe1-35779EXAMPLE",
    "96c59324-ad98-2f5b-f74b-b6c3aEXAMPLE",
    "64c5c950-1d68-8b04-7852-c471dEXAMPLE"
  ]
}
```

#### Sample Response
<a name="API_BatchGetIncidentFindings_Example_1_Response"></a>

```
{
  "errors": [
    {
      "code": "ResourceNotFoundException",
      "findingId": "08c5c945-b204-adaa-f0ef-2f212INVALID",
      "message": "Finding with ID '08c5c945-b204-adaa-f0ef-2f212INVALID' is not accessible"
    }
  ],
  "findings": [
    {
      "creationTime": "2023-12-13T10:47:03.560000+11:00",
      "details": {
        "cloudFormationStackUpdate": {
          "endTime": "2023-12-13T10:46:05.616000+11:00",
          "stackArn": "arn:aws:cloudformation:us-east-2:111122223333:stack/my-test-stack/54ae4890-6632-11ee-8958-0ac64EXAMPLE",
          "startTime": "2023-12-13T10:45:53.850000+11:00"
        }
      },
      "id": "92c59324-ad98-c955-ebe1-35779EXAMPLE",
      "lastModifiedTime": "2023-12-13T10:47:03.560000+11:00"
    },
    {
      "creationTime": "2023-12-13T10:47:03.560000+11:00",
      "details": {
        "cloudFormationStackUpdate": {
          "endTime": "2023-12-13T10:46:33.015000+11:00",
          "stackArn": "arn:aws:cloudformation:us-east-2:111122223333:stack/my-test-stack/54ae4890-6632-11ee-8958-0ac64EXAMPLE",
          "startTime": "2023-12-13T10:46:21.480000+11:00"
        }
      },
      "id": "96c59324-ad98-2f5b-f74b-b6c3aEXAMPLE",
      "lastModifiedTime": "2023-12-13T10:47:03.560000+11:00"
    },
    {
      "creationTime": "2023-12-13T11:40:56.273000+11:00",
      "details": {
        "codeDeployDeployment": {
          "deploymentGroupArn": "arn:aws:codedeploy:us-east-2:111122223333:deploymentgroup:my-ServerlessDeploymentApplication-7lLr2EXAMPLE/myLambdaFunctionDeploymentGroup-ID2K1EXAMPLE",
          "deploymentId": "d-RI2EXAMPLE",
          "endTime": "2023-12-13T11:37:03.174000+11:00",
          "startTime": "2023-12-13T11:37:00.790000+11:00"
        }
      },
      "id": "64c5c950-1d68-8b04-7852-c471dEXAMPLE",
      "lastModifiedTime": "2023-12-13T11:40:56.273000+11:00"
    }
  ]
}
```

## See Also
<a name="API_BatchGetIncidentFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/BatchGetIncidentFindings)
