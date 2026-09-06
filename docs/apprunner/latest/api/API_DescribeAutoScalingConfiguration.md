---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeAutoScalingConfiguration.html
---

# DescribeAutoScalingConfiguration
<a name="API_DescribeAutoScalingConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Return a full description of an AWS App Runner automatic scaling configuration resource.

## Request Syntax
<a name="API_DescribeAutoScalingConfiguration_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAutoScalingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_DescribeAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-DescribeAutoScalingConfiguration-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want a description for.
The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DescribeAutoScalingConfiguration_ResponseSyntax"></a>

```
{
   "AutoScalingConfiguration": {
      "AutoScalingConfigurationArn": "string",
      "AutoScalingConfigurationName": "string",
      "AutoScalingConfigurationRevision": number,
      "CreatedAt": number,
      "DeletedAt": number,
      "HasAssociatedService": boolean,
      "IsDefault": boolean,
      "Latest": boolean,
      "MaxConcurrency": number,
      "MaxSize": number,
      "MinSize": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAutoScalingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScalingConfiguration](#API_DescribeAutoScalingConfiguration_ResponseSyntax) **   <a name="apprunner-DescribeAutoScalingConfiguration-response-AutoScalingConfiguration"></a>
A full description of the App Runner auto scaling configuration that you specified in this request.
Type: [AutoScalingConfiguration](API_AutoScalingConfiguration.md) object

## Errors
<a name="API_DescribeAutoScalingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAutoScalingConfiguration_Examples"></a>

### Describe the latest active revision of an auto scaling configuration
<a name="API_DescribeAutoScalingConfiguration_Example_1"></a>

This example illustrates how to get a description of the latest active revision of an App Runner auto scaling configuration. To describe the latest active revision, specify an ARN that ends with the configuration name, without the revision component.

In the example, two revisions exist. Therefore, revision `2` (the latest) is described. The resulting object shows `"Latest": true`.

#### Sample Request
<a name="API_DescribeAutoScalingConfiguration_Example_1_Request"></a>

```
$ aws apprunner describe-auto-scaling-configuration --cli-input-json "`cat`"
{
  "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability"
}
```

#### Sample Response
<a name="API_DescribeAutoScalingConfiguration_Example_1_Response"></a>

```
{
  "AutoScalingConfiguration": {
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6",
    "AutoScalingConfigurationName": "high-availability",
    "AutoScalingConfigurationRevision": 2,
    "CreatedAt": "2021-02-25T17:42:59Z",
    "Latest": true,
    "Status": "ACTIVE",
    "MaxConcurrency": 30,
    "MaxSize": 25,
    "MinSize": 5
  }
}
```

### Describe a specific revision of an auto scaling configuration
<a name="API_DescribeAutoScalingConfiguration_Example_2"></a>

This example illustrates how to get a description of a specific revision of an App Runner auto scaling configuration. To describe a specific revision, specify an ARN that includes the revision number.

In the example, several revisions exist and revision `1` is queried. The resulting object shows `"Latest": false`.

#### Sample Request
<a name="API_DescribeAutoScalingConfiguration_Example_2_Request"></a>

```
$ aws apprunner describe-auto-scaling-configuration --cli-input-json "`cat`"
{
  "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1"
}
```

#### Sample Response
<a name="API_DescribeAutoScalingConfiguration_Example_2_Response"></a>

```
{
  "AutoScalingConfiguration": {
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e",
    "AutoScalingConfigurationName": "high-availability",
    "AutoScalingConfigurationRevision": 1,
    "CreatedAt": "2020-11-03T00:29:17Z",
    "Latest": false,
    "Status": "ACTIVE",
    "MaxConcurrency": 100,
    "MaxSize": 25,
    "MinSize": 5
  }
}
```

## See Also
<a name="API_DescribeAutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DescribeAutoScalingConfiguration)
