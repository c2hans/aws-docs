---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetExecutionPreview.html
---

# GetExecutionPreview
<a name="API_GetExecutionPreview"></a>

Initiates the process of retrieving an existing preview that shows the effects that running a specified Automation runbook would have on the targeted resources.

## Request Syntax
<a name="API_GetExecutionPreview_RequestSyntax"></a>

```
{
   "ExecutionPreviewId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExecutionPreview_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExecutionPreviewId](#API_GetExecutionPreview_RequestSyntax) **   <a name="systemsmanager-GetExecutionPreview-request-ExecutionPreviewId"></a>
The ID of the existing execution preview.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_GetExecutionPreview_ResponseSyntax"></a>

```
{
   "EndedAt": number,
   "ExecutionPreview": { ... },
   "ExecutionPreviewId": "string",
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_GetExecutionPreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndedAt](#API_GetExecutionPreview_ResponseSyntax) **   <a name="systemsmanager-GetExecutionPreview-response-EndedAt"></a>
A UTC timestamp indicating when the execution preview operation ended.
Type: Timestamp

 ** [ExecutionPreview](#API_GetExecutionPreview_ResponseSyntax) **   <a name="systemsmanager-GetExecutionPreview-response-ExecutionPreview"></a>
Information about the changes that would be made if an execution were run.
Type: [ExecutionPreview](API_ExecutionPreview.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [ExecutionPreviewId](#API_GetExecutionPreview_ResponseSyntax) **   <a name="systemsmanager-GetExecutionPreview-response-ExecutionPreviewId"></a>
The generated ID for the existing execution preview.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

 ** [Status](#API_GetExecutionPreview_ResponseSyntax) **   <a name="systemsmanager-GetExecutionPreview-response-Status"></a>
The current status of the execution preview operation.
Type: String
Valid Values: `Pending | InProgress | Success | Failed`

 ** [StatusMessage](#API_GetExecutionPreview_ResponseSyntax) **   <a name="systemsmanager-GetExecutionPreview-response-StatusMessage"></a>
Supplemental information about the current status of the execution preview.
Type: String

## Errors
<a name="API_GetExecutionPreview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

## Examples
<a name="API_GetExecutionPreview_Examples"></a>

### Example
<a name="API_GetExecutionPreview_Example_1"></a>

This example illustrates one usage of GetExecutionPreview.

#### Sample Request
<a name="API_GetExecutionPreview_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetExecutionPreview
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20241125T162110Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 86

{
    "ExecutionPreviewId": "2f27d6e5-9676-4708-b8bd-aef0aEXAMPLE"
}
```

### Example
<a name="API_GetExecutionPreview_Example_2"></a>

This example illustrates one usage of GetExecutionPreview.

#### Sample Response
<a name="API_GetExecutionPreview_Example_2_Response"></a>

```
{
    "ExecutionPreviewId": "2f27d6e5-9676-4708-b8bd-aef0EXAMPLE",
    "EndedAt": "2024-11-25T01:50:39.424000+00:00",
    "Status": "Success",
    "ExecutionPreview": {
        "Automation": {
            "StepPreviews": {
                "Undetermined": 1
            },
            "Regions": [
                "us-east-2"
            ],
            "TotalAccounts": 7
        }
    }
}
```

## See Also
<a name="API_GetExecutionPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetExecutionPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetExecutionPreview)
