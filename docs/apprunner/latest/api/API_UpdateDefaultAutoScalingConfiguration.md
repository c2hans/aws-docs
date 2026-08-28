---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_UpdateDefaultAutoScalingConfiguration.html
---

# UpdateDefaultAutoScalingConfiguration
<a name="API_UpdateDefaultAutoScalingConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Update an auto scaling configuration to be the default. The existing default auto scaling configuration will be set to non-default automatically.

## Request Syntax
<a name="API_UpdateDefaultAutoScalingConfiguration_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDefaultAutoScalingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_UpdateDefaultAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-UpdateDefaultAutoScalingConfiguration-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to set as the default.
The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is set as the default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_UpdateDefaultAutoScalingConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateDefaultAutoScalingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScalingConfiguration](#API_UpdateDefaultAutoScalingConfiguration_ResponseSyntax) **   <a name="apprunner-UpdateDefaultAutoScalingConfiguration-response-AutoScalingConfiguration"></a>
A description of the App Runner auto scaling configuration that was set as default.
Type: [AutoScalingConfiguration](API_AutoScalingConfiguration.md) object

## Errors
<a name="API_UpdateDefaultAutoScalingConfiguration_Errors"></a>

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
<a name="API_UpdateDefaultAutoScalingConfiguration_Examples"></a>

### Update the latest active revision of an auto scaling configuration to be the default
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_1"></a>

This example illustrates how to update the latest active revision of an App Runner auto scaling configuration to be the default. To designate the latest active revision as the default, specify an ARN that ends with the configuration name, without the revision component.

In the example, two revisions exist. Therefore, revision 2, (the latest revision), is set as the default. The resulting object shows `"IsDefault": true` and `"Latest": true`.

#### Sample Request
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_1_Request"></a>

```
$ aws apprunner update-default-auto-scaling-configuration --cli-input-json "`cat`"
{
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability"
}
```

#### Sample Response
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_1_Response"></a>

```
{
    "AutoScalingConfiguration": {
        "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/6a4d47db94434d30a42cab9a00d21d44",
        "AutoScalingConfigurationName": "high-availability",
        "AutoScalingConfigurationRevision": 2,
        "Latest": true,
        "Status": "active",
        "MaxConcurrency": 100,
        "MinSize": 1,
        "MaxSize": 25,
        "CreatedAt": "2023-09-01T00:00:00Z",
        "HasAssociatedService": false,
        "IsDefault": true
    }
}
```

### Update a specific revision of an auto scaling configuration to be the default
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_2"></a>

This example illustrates how to update a specific revision of an App Runner auto scaling configuration to be the default. To designate a specific revision as the default, specify an ARN that includes the revision number.

In the example, several revisions exist, and revision 1 is set as the default. The resulting object shows `"IsDefault": true` and `"Latest": false`.

#### Sample Request
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_2_Request"></a>

```
$ aws apprunner update-default-auto-scaling-configuration --cli-input-json "`cat`"
{
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1"
}
```

#### Sample Response
<a name="API_UpdateDefaultAutoScalingConfiguration_Example_2_Response"></a>

```
{
    "AutoScalingConfiguration": {
        "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/d2321df129c8440da8c464af7ebcd887",
        "AutoScalingConfigurationName": "high-availability",
        "AutoScalingConfigurationRevision": 1,
        "Latest": false,
        "Status": "active",
        "MaxConcurrency": 100,
        "MinSize": 1,
        "MaxSize": 25,
        "CreatedAt": "2023-09-01T00:00:00Z",
        "HasAssociatedService": false,
        "IsDefault": true
    }
}
```

## See Also
<a name="API_UpdateDefaultAutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/UpdateDefaultAutoScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
