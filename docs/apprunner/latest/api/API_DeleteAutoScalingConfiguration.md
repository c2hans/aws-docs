---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteAutoScalingConfiguration.html
---

# DeleteAutoScalingConfiguration
<a name="API_DeleteAutoScalingConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Delete an AWS App Runner automatic scaling configuration resource. You can delete a top level auto scaling configuration, a specific revision of one, or all revisions associated with the top level configuration. You can't delete the default auto scaling configuration or a configuration that's used by one or more App Runner services.

## Request Syntax
<a name="API_DeleteAutoScalingConfiguration_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}",
   "DeleteAllRevisions": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteAutoScalingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_DeleteAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-DeleteAutoScalingConfiguration-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to delete.
The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

 ** [DeleteAllRevisions](#API_DeleteAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-DeleteAutoScalingConfiguration-request-DeleteAllRevisions"></a>
Set to `true` to delete all of the revisions associated with the `AutoScalingConfigurationArn` parameter value.
When `DeleteAllRevisions` is set to `true`, the only valid value for the Amazon Resource Name (ARN) is a partial ARN ending with: `.../name`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteAutoScalingConfiguration_ResponseSyntax"></a>

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
<a name="API_DeleteAutoScalingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScalingConfiguration](#API_DeleteAutoScalingConfiguration_ResponseSyntax) **   <a name="apprunner-DeleteAutoScalingConfiguration-response-AutoScalingConfiguration"></a>
A description of the App Runner auto scaling configuration that this request just deleted.
Type: [AutoScalingConfiguration](API_AutoScalingConfiguration.md) object

## Errors
<a name="API_DeleteAutoScalingConfiguration_Errors"></a>

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
<a name="API_DeleteAutoScalingConfiguration_Examples"></a>

### Delete the latest active revision of an auto scaling configuration
<a name="API_DeleteAutoScalingConfiguration_Example_1"></a>

This example illustrates how to delete the latest active revision of an App Runner auto scaling configuration. To delete the latest active revision, specify an Amazon Resource Name (ARN) that ends with the configuration name, without the revision component.

In the example, two revisions exist before this action. Therefore, revision `2` (the latest) is deleted. However, it now shows `"Latest": false`, because, after being deleted, it isn't the latest active revision anymore.

#### Sample Request
<a name="API_DeleteAutoScalingConfiguration_Example_1_Request"></a>

```
$ aws apprunner delete-auto-scaling-configuration --cli-input-json "`cat`"
{
  "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability"
}
```

#### Sample Response
<a name="API_DeleteAutoScalingConfiguration_Example_1_Response"></a>

```
{
  "AutoScalingConfiguration": {
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6",
    "AutoScalingConfigurationName": "high-availability",
    "AutoScalingConfigurationRevision": 2,
    "CreatedAt": "2021-02-25T17:42:59Z",
    "DeletedAt": "2021-03-02T08:07:06Z",
    "Latest": false,
    "Status": "INACTIVE",
    "MaxConcurrency": 30,
    "MaxSize": 25,
    "MinSize": 5
  }
}
```

### Delete a specific revision of an auto scaling configuration
<a name="API_DeleteAutoScalingConfiguration_Example_2"></a>

This example illustrates how to delete a specific revision of an App Runner auto scaling configuration. To delete a specific revision, specify an ARN that includes the revision number.

In the example, several revisions exist before this action. The action deletes revision `1`.

#### Sample Request
<a name="API_DeleteAutoScalingConfiguration_Example_2_Request"></a>

```
$ aws apprunner delete-auto-scaling-configuration --cli-input-json "`cat`"
{
  "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1"
}
```

#### Sample Response
<a name="API_DeleteAutoScalingConfiguration_Example_2_Response"></a>

```
{
  "AutoScalingConfiguration": {
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e",
    "AutoScalingConfigurationName": "high-availability",
    "AutoScalingConfigurationRevision": 1,
    "CreatedAt": "2020-11-03T00:29:17Z",
    "DeletedAt": "2021-03-02T08:07:06Z",
    "Latest": false,
    "Status": "INACTIVE",
    "MaxConcurrency": 100,
    "MaxSize": 25,
    "MinSize": 5
  }
}
```

### Delete all revisions of an auto scaling configuration
<a name="API_DeleteAutoScalingConfiguration_Example_3"></a>

This example illustrates how to delete all of the revisions associated with an App Runner auto scaling configuration.

To delete all associated revisions set `DeleteAllRevisions` to `true`. Specify a partial ARN ending with `.../name `.

The response does not include all of the fields listed in the *Response Syntax*. It only contains the fields shown in the sample response.

#### Sample Request
<a name="API_DeleteAutoScalingConfiguration_Example_3_Request"></a>

```
$ aws apprunner delete-auto-scaling-configuration --cli-input-json "`cat`"
{
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability",
    "DeleteAllRevisions": true
}
```

#### Sample Response
<a name="API_DeleteAutoScalingConfiguration_Example_3_Response"></a>

```
{
    "AutoScalingConfiguration": {
        "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability",
        "AutoScalingConfigurationName": "high-availability",
        "Status": "inactive"
    }
}
```

## See Also
<a name="API_DeleteAutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DeleteAutoScalingConfiguration)
