---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_StartIncident.html
---

# StartIncident
<a name="API_StartIncident"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Used to start an incident from CloudWatch alarms, EventBridge events, or manually.

## Request Syntax
<a name="API_StartIncident_RequestSyntax"></a>

```
POST /startIncident HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "impact": {{number}},
   "relatedItems": [
      {
         "generatedId": "{{string}}",
         "identifier": {
            "type": "{{string}}",
            "value": { ... }
         },
         "title": "{{string}}"
      }
   ],
   "responsePlanArn": "{{string}}",
   "title": "{{string}}",
   "triggerDetails": {
      "rawData": "{{string}}",
      "source": "{{string}}",
      "timestamp": {{number}},
      "triggerArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartIncident_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartIncident_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-clientToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [impact](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-impact"></a>
Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.

**Supported impact codes**
+  `1` - Critical
+  `2` - High
+  `3` - Medium
+  `4` - Low
+  `5` - No Impact
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [relatedItems](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-relatedItems"></a>
Add related items to the incident for other responders to use. Related items are AWS resources, external links, or files uploaded to an Amazon S3 bucket.
Type: Array of [RelatedItem](API_RelatedItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [responsePlanArn](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-responsePlanArn"></a>
The Amazon Resource Name (ARN) of the response plan that pre-defines summary, chat channels, Amazon SNS topics, runbooks, title, and impact of the incident.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** [title](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-title"></a>
Provide a title for the incident. Providing a title overwrites the title provided by the response plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** [triggerDetails](#API_StartIncident_RequestSyntax) **   <a name="IncidentManager-StartIncident-request-triggerDetails"></a>
Details of what created the incident record in Incident Manager.
Type: [TriggerDetails](API_TriggerDetails.md) object
Required: No

## Response Syntax
<a name="API_StartIncident_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "incidentRecordArn": "string"
}
```

## Response Elements
<a name="API_StartIncident_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [incidentRecordArn](#API_StartIncident_ResponseSyntax) **   <a name="IncidentManager-StartIncident-response-incidentRecordArn"></a>
The ARN of the newly created incident record.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

## Errors
<a name="API_StartIncident_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
HTTP Status Code: 409

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
<a name="API_StartIncident_Examples"></a>

### Example
<a name="API_StartIncident_Example_1"></a>

This example illustrates one usage of StartIncident.

#### Sample Request
<a name="API_StartIncident_Example_1_Request"></a>

```
POST /startIncident HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.start-incident
X-Amz-Date: 20210811T181411Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=AKIAIOSFODNN7EXAMPLE
Content-Length: 144

{
	"responsePlanArn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response",
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_StartIncident_Example_1_Response"></a>

```
{
    "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/1abd9b35-ff4c-eb47-f20f-712a6c4c88cc"
}
```

## See Also
<a name="API_StartIncident_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/StartIncident)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/StartIncident)
