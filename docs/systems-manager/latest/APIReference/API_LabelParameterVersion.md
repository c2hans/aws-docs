---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_LabelParameterVersion.html
---

# LabelParameterVersion
<a name="API_LabelParameterVersion"></a>

A parameter label is a user-defined alias to help you manage different versions of a parameter. When you modify a parameter, AWS Systems Manager automatically saves a new version and increments the version number by one. A label can help you remember the purpose of a parameter when there are multiple versions.

Parameter labels have the following requirements and restrictions.
+ A version of a parameter can have a maximum of 10 labels.
+ You can't attach the same label to different versions of the same parameter. For example, if version 1 has the label Production, then you can't attach Production to version 2.
+ You can move a label from one version of a parameter to another.
+ You can't create a label when you create a new parameter. You must attach a label to a specific version of a parameter.
+ If you no longer want to use a parameter label, then you can either delete it or move it to a different version of a parameter.
+ A label can have a maximum of 100 characters.
+ Labels can contain letters (case sensitive), numbers, periods (.), hyphens (-), or underscores (\_).
+ Labels can't begin with a number, "`aws`" or "`ssm`" (not case sensitive). If a label fails to meet these requirements, then the label isn't associated with a parameter and the system displays it in the list of InvalidLabels.
+ Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

## Request Syntax
<a name="API_LabelParameterVersion_RequestSyntax"></a>

```
{
   "Labels": [ "{{string}}" ],
   "Name": "{{string}}",
   "ParameterVersion": {{number}}
}
```

## Request Parameters
<a name="API_LabelParameterVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Labels](#API_LabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-LabelParameterVersion-request-Labels"></a>
One or more labels to attach to the specified parameter version.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_LabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-LabelParameterVersion-request-Name"></a>
The parameter name on which you want to attach one or more labels.
You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ParameterVersion](#API_LabelParameterVersion_RequestSyntax) **   <a name="systemsmanager-LabelParameterVersion-request-ParameterVersion"></a>
The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.
Type: Long
Required: No

## Response Syntax
<a name="API_LabelParameterVersion_ResponseSyntax"></a>

```
{
   "InvalidLabels": [ "string" ],
   "ParameterVersion": number
}
```

## Response Elements
<a name="API_LabelParameterVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvalidLabels](#API_LabelParameterVersion_ResponseSyntax) **   <a name="systemsmanager-LabelParameterVersion-response-InvalidLabels"></a>
The label doesn't meet the requirements. For information about parameter label requirements, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [ParameterVersion](#API_LabelParameterVersion_ResponseSyntax) **   <a name="systemsmanager-LabelParameterVersion-response-ParameterVersion"></a>
The version of the parameter that has been labeled.
Type: Long

## Errors
<a name="API_LabelParameterVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ParameterNotFound **
The parameter couldn't be found. Verify the name and try again.
For the `DeleteParameter` and `GetParameter` actions, if the specified parameter doesn't exist, the `ParameterNotFound` exception is *not* recorded in AWS CloudTrail event logs.
HTTP Status Code: 400

 ** ParameterVersionLabelLimitExceeded **
A parameter version can have a maximum of ten labels.
HTTP Status Code: 400

 ** ParameterVersionNotFound **
The specified parameter version wasn't found. Verify the parameter name and version, and try again.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_LabelParameterVersion_Examples"></a>

### Example
<a name="API_LabelParameterVersion_Example_1"></a>

This example illustrates one usage of LabelParameterVersion.

#### Sample Request
<a name="API_LabelParameterVersion_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.LabelParameterVersion
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T191052Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240229/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 76

{
    "Name": "MyGitHubPassword",
    "ParameterVersion": 3,
    "Labels": [
        "March-2020"
    ]
}
```

#### Sample Response
<a name="API_LabelParameterVersion_Example_1_Response"></a>

```
{
    "InvalidLabels": [],
    "ParameterVersion": 3
}
```

## See Also
<a name="API_LabelParameterVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/LabelParameterVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/LabelParameterVersion)
