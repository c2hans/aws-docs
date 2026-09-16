---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetIncidentRecord.html
---

# GetIncidentRecord
<a name="API_GetIncidentRecord"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Returns the details for the specified incident record.

## Request Syntax
<a name="API_GetIncidentRecord_RequestSyntax"></a>

```
GET /getIncidentRecord?arn={{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIncidentRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetIncidentRecord_RequestSyntax) **   <a name="IncidentManager-GetIncidentRecord-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the incident record.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_GetIncidentRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIncidentRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "incidentRecord": {
      "arn": "string",
      "automationExecutions": [
         { ... }
      ],
      "chatChannel": { ... },
      "creationTime": number,
      "dedupeString": "string",
      "impact": number,
      "incidentRecordSource": {
         "createdBy": "string",
         "invokedBy": "string",
         "resourceArn": "string",
         "source": "string"
      },
      "lastModifiedBy": "string",
      "lastModifiedTime": number,
      "notificationTargets": [
         { ... }
      ],
      "resolvedTime": number,
      "status": "string",
      "summary": "string",
      "title": "string"
   }
}
```

## Response Elements
<a name="API_GetIncidentRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [incidentRecord](#API_GetIncidentRecord_ResponseSyntax) **   <a name="IncidentManager-GetIncidentRecord-response-incidentRecord"></a>
Details the structure of the incident record.
Type: [IncidentRecord](API_IncidentRecord.md) object

## Errors
<a name="API_GetIncidentRecord_Errors"></a>

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
<a name="API_GetIncidentRecord_Examples"></a>

### Example
<a name="API_GetIncidentRecord_Example_1"></a>

This example illustrates one usage of GetIncidentRecord.

#### Sample Request
<a name="API_GetIncidentRecord_Example_1_Request"></a>

```
GET /getIncidentRecord?arn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Aincident-record%2Fexample-response%2F78bd9919-b9ac-962d-91e0-149960600e3f HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.get-incident-record
X-Amz-Date: 20210810T223503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetIncidentRecord_Example_1_Response"></a>

```
{
	"incidentRecord":
		{
			"arn":"arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f",
			"automationExecutions":[],
			"chatChannel":{
				"chatbotSns":["arn:aws:sns:us-east-1:111122223333:Standard_User"]
			},
			"creationTime":1.628634837849E9,
			"dedupeString":"00bd9919-b99f-367c-c282-eabcaff587f7",
			"impact":5,
			"incidentRecordSource": {
				"createdBy":"arn:aws:sts::111122223333:assumed-role/Admin/exampleUser",
				"invokedBy":"arn:aws:sts::111122223333:assumed-role/Admin/exampleUser",
				"resourceArn":null,"source":"aws.ssm-incidents.custom"
			},
			"lastModifiedBy":"arn:aws:sts::111122223333:assumed-role/Admin/exampleUser",
			"lastModifiedTime":1.628634838724E9,
			"notificationTargets":[],
			"resolvedTime":null,
			"status":"OPEN",
			"summary":null,
			"title":"example-incident"
		}
}
```

## See Also
<a name="API_GetIncidentRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/GetIncidentRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/GetIncidentRecord)
