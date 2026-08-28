---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeObservabilityConfiguration.html
---

# DescribeObservabilityConfiguration
<a name="API_DescribeObservabilityConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Return a full description of an AWS App Runner observability configuration resource.

## Request Syntax
<a name="API_DescribeObservabilityConfiguration_RequestSyntax"></a>

```
{
   "ObservabilityConfigurationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeObservabilityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ObservabilityConfigurationArn](#API_DescribeObservabilityConfiguration_RequestSyntax) **   <a name="apprunner-DescribeObservabilityConfiguration-request-ObservabilityConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner observability configuration that you want a description for.
The ARN can be a full observability configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DescribeObservabilityConfiguration_ResponseSyntax"></a>

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
<a name="API_DescribeObservabilityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ObservabilityConfiguration](#API_DescribeObservabilityConfiguration_ResponseSyntax) **   <a name="apprunner-DescribeObservabilityConfiguration-response-ObservabilityConfiguration"></a>
A full description of the App Runner observability configuration that you specified in this request.
Type: [ObservabilityConfiguration](API_ObservabilityConfiguration.md) object

## Errors
<a name="API_DescribeObservabilityConfiguration_Errors"></a>

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
<a name="API_DescribeObservabilityConfiguration_Examples"></a>

### Describe the latest active revision of an observability configuration
<a name="API_DescribeObservabilityConfiguration_Example_1"></a>

This example illustrates how to get a description of the latest active revision of an App Runner observability configuration. To describe the latest active revision, specify an ARN that ends with the configuration name, without the revision component.

In the example, two revisions exist. Therefore, revision `2` (the latest) is described. The resulting object shows `"Latest": true`.

**Note**
The two revisions in our examples are identical, because App Runner doesn't yet support enough observability functionality to demonstrate two significantly different revisions (for example, multiple tracing vendors). We're including the two examples only to demonstrate the revisioning behavior during retrieval.

#### Sample Request
<a name="API_DescribeObservabilityConfiguration_Example_1_Request"></a>

```
$ aws apprunner describe-observability-configuration --cli-input-json "`cat`"
{
  "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing"
}
```

#### Sample Response
<a name="API_DescribeObservabilityConfiguration_Example_1_Response"></a>

```
{
  "ObservabilityConfiguration": {
    "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/2/e76562f50d78042e819fead0f59672e6",
    "ObservabilityConfigurationName": "xray-tracing",
    "ObservabilityConfigurationRevision": 2,
    "CreatedAt": "2021-02-25T17:42:59Z",
    "Latest": true,
    "Status": "ACTIVE",
    "TraceConfiguration": {
        "Vendor": "AWSXRAY"
    }
  }
}
```

### Describe a specific revision of an observability configuration
<a name="API_DescribeObservabilityConfiguration_Example_2"></a>

This example illustrates how to get a description of a specific revision of an App Runner observability configuration. To describe a specific revision, specify an ARN that includes the revision number.

In the example, several revisions exist and revision `1` is queried. The resulting object shows `"Latest": false`.

#### Sample Request
<a name="API_DescribeObservabilityConfiguration_Example_2_Request"></a>

```
$ aws apprunner describe-observability-configuration --cli-input-json "`cat`"
{
  "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/1"
}
```

#### Sample Response
<a name="API_DescribeObservabilityConfiguration_Example_2_Response"></a>

```
{
  "ObservabilityConfiguration": {
    "ObservabilityConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/1/2f50e7656d7819fead0f59672e68042e",
    "ObservabilityConfigurationName": "xray-tracing",
    "ObservabilityConfigurationRevision": 1,
    "CreatedAt": "2020-11-03T00:29:17Z",
    "Latest": false,
    "Status": "ACTIVE",
    "TraceConfiguration": {
        "Vendor": "AWSXRAY"
    }
  }
}
```

## See Also
<a name="API_DescribeObservabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DescribeObservabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DescribeObservabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
