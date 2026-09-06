---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteMaintenanceWindow.html
---

# DeleteMaintenanceWindow
<a name="API_DeleteMaintenanceWindow"></a>

Deletes a maintenance window.

## Request Syntax
<a name="API_DeleteMaintenanceWindow_RequestSyntax"></a>

```
{
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WindowId](#API_DeleteMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeleteMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window to delete.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_DeleteMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowId": "string"
}
```

## Response Elements
<a name="API_DeleteMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowId](#API_DeleteMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-DeleteMaintenanceWindow-response-WindowId"></a>
The ID of the deleted maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

## Errors
<a name="API_DeleteMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DeleteMaintenanceWindow_Examples"></a>

### Example
<a name="API_DeleteMaintenanceWindow_Example_1"></a>

This example illustrates one usage of DeleteMaintenanceWindow.

#### Sample Request
<a name="API_DeleteMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 36
X-Amz-Target: AmazonSSM.DeleteMaintenanceWindow
X-Amz-Date: 20240312T210257Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

#### Sample Response
<a name="API_DeleteMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

## See Also
<a name="API_DeleteMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteMaintenanceWindow)
