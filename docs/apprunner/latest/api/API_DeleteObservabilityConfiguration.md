---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteObservabilityConfiguration.html
---

# DeleteObservabilityConfiguration
<a name="API_DeleteObservabilityConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Delete an AWS App Runner observability configuration resource. You can delete a specific revision or the latest active revision. You can't delete a configuration that's used by one or more App Runner services.

## Request Syntax
<a name="API_DeleteObservabilityConfiguration_RequestSyntax"></a>

```
{
   "ObservabilityConfigurationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteObservabilityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ObservabilityConfigurationArn](#API_DeleteObservabilityConfiguration_RequestSyntax) **   <a name="apprunner-DeleteObservabilityConfiguration-request-ObservabilityConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner observability configuration that you want to delete.
The ARN can be a full observability configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DeleteObservabilityConfiguration_ResponseSyntax"></a>

```
{
   "ObservabilityConfiguration": {
      "CreatedAt": number,
      "DeletedAt": number,
      "Latest": boolean,
      "ObservabilityConfigurationArn": "string",
      "ObservabilityConfigurationName": "string",
      "ObservabilityConfigurationRevision": number,
      "Status": "string",
      "TraceConfiguration": {
         "Vendor": "string"
      }
   }
}
```

## Response Elements
<a name="API_DeleteObservabilityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ObservabilityConfiguration](#API_DeleteObservabilityConfiguration_ResponseSyntax) **   <a name="apprunner-DeleteObservabilityConfiguration-response-ObservabilityConfiguration"></a>
A description of the App Runner observability configuration that this request just deleted.
Type: [ObservabilityConfiguration](API_ObservabilityConfiguration.md) object

## Errors
<a name="API_DeleteObservabilityConfiguration_Errors"></a>

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
<a name="API_DeleteObservabilityConfiguration_Examples"></a>

### Delete the latest active revision of an observability configuration
<a name="API_DeleteObservabilityConfiguration_Example_1"></a>

This example illustrates how to delete the latest active revision of an App Runner observability configuration. To delete the latest active revision, specify an Amazon Resource Name (ARN) that ends with the configuration name, without the revision component.

In the example, two revisions exist before this action. Therefore, revision `2` (the latest) is deleted. However, it now shows `"Latest": false`, because, after being deleted, it isn't the latest active revision anymore.

**Note**
The two revisions in our examples are identical, because App Runner doesn't yet support enough observability functionality to demonstrate two significantly different revisions (for example, multiple tracing vendors). We're including the two examples only to demonstrate the revisioning behavior during deletion.

#### Sample Request
<a name="API_DeleteObservabilityConfiguration_Example_1_Request"></a>

```
$ aws apprunner delete-observability-configuration --cli-input-json "`cat`"
{
  "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing"
}
```

#### Sample Response
<a name="API_DeleteObservabilityConfiguration_Example_1_Response"></a>

```
{
  "ObservabilityConfiguration": {
    "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/2/e76562f50d78042e819fead0f59672e6",
    "ObservabilityConfigurationName": "xray-tracing",
    "ObservabilityConfigurationRevision": 2,
    "CreatedAt": "2021-02-25T17:42:59Z",
    "DeletedAt": "2021-03-02T08:07:06Z",
    "Latest": false,
    "Status": "INACTIVE",
    "TraceConfiguration": {
        "Vendor": "AWSXRAY"
    }
  }
}
```

### Delete a specific revision of an observability configuration
<a name="API_DeleteObservabilityConfiguration_Example_2"></a>

This example illustrates how to delete a specific revision of an App Runner observability configuration. To delete a specific revision, specify an ARN that includes the revision number.

In the example, several revisions exist before this action. The action deletes revision `1`.

#### Sample Request
<a name="API_DeleteObservabilityConfiguration_Example_2_Request"></a>

```
$ aws apprunner delete-observability-configuration --cli-input-json "`cat`"
{
  "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/1"
}
```

#### Sample Response
<a name="API_DeleteObservabilityConfiguration_Example_2_Response"></a>

```
{
  "ObservabilityConfiguration": {
    "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/1/2f50e7656d7819fead0f59672e68042e",
    "ObservabilityConfigurationName": "xray-tracing",
    "ObservabilityConfigurationRevision": 1,
    "CreatedAt": "2020-11-03T00:29:17Z",
    "DeletedAt": "2021-03-02T08:07:06Z",
    "Latest": false,
    "Status": "INACTIVE",
    "TraceConfiguration": {
        "Vendor": "AWSXRAY"
    }
  }
}
```

## See Also
<a name="API_DeleteObservabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DeleteObservabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DeleteObservabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
