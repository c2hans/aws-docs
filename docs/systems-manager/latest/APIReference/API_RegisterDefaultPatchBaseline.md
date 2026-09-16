---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterDefaultPatchBaseline.html
---

# RegisterDefaultPatchBaseline
<a name="API_RegisterDefaultPatchBaseline"></a>

Defines the default patch baseline for the relevant operating system.

To reset the AWS-predefined patch baseline as the default, specify the full patch baseline Amazon Resource Name (ARN) as the baseline ID value. For example, for CentOS, specify `arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed` instead of `pb-0574b43a65ea646ed`.

## Request Syntax
<a name="API_RegisterDefaultPatchBaseline_RequestSyntax"></a>

```
{
   "BaselineId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterDefaultPatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineId](#API_RegisterDefaultPatchBaseline_RequestSyntax) **   <a name="systemsmanager-RegisterDefaultPatchBaseline-request-BaselineId"></a>
The ID of the patch baseline that should be the default patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

## Response Syntax
<a name="API_RegisterDefaultPatchBaseline_ResponseSyntax"></a>

```
{
   "BaselineId": "string"
}
```

## Response Elements
<a name="API_RegisterDefaultPatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineId](#API_RegisterDefaultPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-RegisterDefaultPatchBaseline-response-BaselineId"></a>
The ID of the default patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

## Errors
<a name="API_RegisterDefaultPatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

## Examples
<a name="API_RegisterDefaultPatchBaseline_Examples"></a>

### Example
<a name="API_RegisterDefaultPatchBaseline_Example_1"></a>

This example illustrates one usage of RegisterDefaultPatchBaseline.

#### Sample Request
<a name="API_RegisterDefaultPatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 38
X-Amz-Target: AmazonSSM.RegisterDefaultPatchBaseline
X-Amz-Date: 20240309T025821Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_RegisterDefaultPatchBaseline_Example_1_Response"></a>

```
{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

## See Also
<a name="API_RegisterDefaultPatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/RegisterDefaultPatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/RegisterDefaultPatchBaseline)
