---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteIncidentRecord.html
---

# DeleteIncidentRecord
<a name="API_DeleteIncidentRecord"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Delete an incident record from Incident Manager.

## Request Syntax
<a name="API_DeleteIncidentRecord_RequestSyntax"></a>

```
POST /deleteIncidentRecord HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteIncidentRecord_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteIncidentRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_DeleteIncidentRecord_RequestSyntax) **   <a name="IncidentManager-DeleteIncidentRecord-request-arn"></a>
The Amazon Resource Name (ARN) of the incident record you are deleting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_DeleteIncidentRecord_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteIncidentRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteIncidentRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_DeleteIncidentRecord_Examples"></a>

### Example
<a name="API_DeleteIncidentRecord_Example_1"></a>

This example illustrates one usage of DeleteIncidentRecord.

#### Sample Request
<a name="API_DeleteIncidentRecord_Example_1_Request"></a>

```
POST /deleteIncidentRecord HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.delete-incident-record
X-Amz-Date: 20210810T222351Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 116

{
	"arn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/bebd9911-63a7-672f-820b-63731f2543ad"
}
```

#### Sample Response
<a name="API_DeleteIncidentRecord_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteIncidentRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/DeleteIncidentRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/DeleteIncidentRecord)
