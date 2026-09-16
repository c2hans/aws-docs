---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteOpsItem.html
---

# DeleteOpsItem
<a name="API_DeleteOpsItem"></a>

Delete an OpsItem. You must have permission in AWS Identity and Access Management (IAM) to delete an OpsItem.

**Important**
Note the following important information about this operation.
Deleting an OpsItem is irreversible. You can't restore a deleted OpsItem.
This operation uses an *eventual consistency model*, which means the system can take a few minutes to complete this operation. If you delete an OpsItem and immediately call, for example, [GetOpsItem](API_GetOpsItem.md), the deleted OpsItem might still appear in the response.
This operation is idempotent. The system doesn't throw an exception if you repeatedly call this operation for the same OpsItem. If the first call is successful, all additional calls return the same successful response as the first call.
This operation doesn't support cross-account calls. A delegated administrator or management account can't delete OpsItems in other accounts, even if OpsCenter has been set up for cross-account administration. For more information about cross-account administration, see [Setting up OpsCenter to centrally manage OpsItems across accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.html) in the *Systems Manager User Guide*.

## Request Syntax
<a name="API_DeleteOpsItem_RequestSyntax"></a>

```
{
   "OpsItemId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteOpsItem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OpsItemId](#API_DeleteOpsItem_RequestSyntax) **   <a name="systemsmanager-DeleteOpsItem-request-OpsItemId"></a>
The ID of the OpsItem that you want to delete.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

## Response Elements
<a name="API_DeleteOpsItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteOpsItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsItemInvalidParameterException **
A specified parameter argument isn't valid. Verify the available arguments and try again.
HTTP Status Code: 400

## Examples
<a name="API_DeleteOpsItem_Examples"></a>

### Example
<a name="API_DeleteOpsItem_Example_1"></a>

This example illustrates one usage of DeleteOpsItem.

#### Sample Request
<a name="API_DeleteOpsItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteOpsItem
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T151532Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 19

{
    "OpsItemId": "oi-abcdef12345"
}
```

#### Sample Response
<a name="API_DeleteOpsItem_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteOpsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteOpsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteOpsItem)
