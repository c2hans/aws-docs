---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterPatchBaselineForPatchGroup.html
---

# DeregisterPatchBaselineForPatchGroup
<a name="API_DeregisterPatchBaselineForPatchGroup"></a>

Removes a patch group from a patch baseline.

## Request Syntax
<a name="API_DeregisterPatchBaselineForPatchGroup_RequestSyntax"></a>

```
{
   "BaselineId": "{{string}}",
   "PatchGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterPatchBaselineForPatchGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineId](#API_DeregisterPatchBaselineForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DeregisterPatchBaselineForPatchGroup-request-BaselineId"></a>
The ID of the patch baseline to deregister the patch group from.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

 ** [PatchGroup](#API_DeregisterPatchBaselineForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DeregisterPatchBaselineForPatchGroup-request-PatchGroup"></a>
The name of the patch group that should be deregistered from the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_DeregisterPatchBaselineForPatchGroup_ResponseSyntax"></a>

```
{
   "BaselineId": "string",
   "PatchGroup": "string"
}
```

## Response Elements
<a name="API_DeregisterPatchBaselineForPatchGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineId](#API_DeregisterPatchBaselineForPatchGroup_ResponseSyntax) **   <a name="systemsmanager-DeregisterPatchBaselineForPatchGroup-response-BaselineId"></a>
The ID of the patch baseline the patch group was deregistered from.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

 ** [PatchGroup](#API_DeregisterPatchBaselineForPatchGroup_ResponseSyntax) **   <a name="systemsmanager-DeregisterPatchBaselineForPatchGroup-response-PatchGroup"></a>
The name of the patch group deregistered from the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_DeregisterPatchBaselineForPatchGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterPatchBaselineForPatchGroup_Examples"></a>

### Example
<a name="API_DeregisterPatchBaselineForPatchGroup_Example_1"></a>

This example illustrates one usage of DeregisterPatchBaselineForPatchGroup.

#### Sample Request
<a name="API_DeregisterPatchBaselineForPatchGroup_Example_1_Request"></a>

```
POST / HTTP/1.1
  Host: ssm.us-east-2.amazonaws.com
  Accept-Encoding: identity
  Content-Length: 74
  X-Amz-Target: AmazonSSM.DeregisterPatchBaselineForPatchGroup
  X-Amz-Date: 20240309T062043Z
  User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
  Content-Type: application/x-amz-json-1.1
  Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "PatchGroup": "mypatchgroup",
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_DeregisterPatchBaselineForPatchGroup_Example_1_Response"></a>

```
{
    "PatchGroup": "mypatchgroup",
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

## See Also
<a name="API_DeregisterPatchBaselineForPatchGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup)
