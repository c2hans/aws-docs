---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListAutoScalingConfigurations.html
---

# ListAutoScalingConfigurations
<a name="API_ListAutoScalingConfigurations"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Returns a list of active AWS App Runner automatic scaling configurations in your AWS account. You can query the revisions for a specific configuration name or the revisions for all active configurations in your account. You can optionally query only the latest revision of each requested name.

To retrieve a full description of a particular configuration revision, call [DescribeAutoScalingConfiguration](API_DescribeAutoScalingConfiguration.md) and provide one of the ARNs returned by `ListAutoScalingConfigurations`.

## Request Syntax
<a name="API_ListAutoScalingConfigurations_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationName": "{{string}}",
   "LatestOnly": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutoScalingConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationName](#API_ListAutoScalingConfigurations_RequestSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-request-AutoScalingConfigurationName"></a>
The name of the App Runner auto scaling configuration that you want to list. If specified, App Runner lists revisions that share this name. If not specified, App Runner returns revisions of all active configurations.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** [LatestOnly](#API_ListAutoScalingConfigurations_RequestSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-request-LatestOnly"></a>
Set to `true` to list only the latest revision for each requested configuration name.
Set to `false` to list all revisions for each requested configuration name.
Default: `true`
Type: Boolean
Required: No

 ** [MaxResults](#API_ListAutoScalingConfigurations_RequestSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-request-MaxResults"></a>
The maximum number of results to include in each response (result page). It's used for a paginated request.
If you don't specify `MaxResults`, the request retrieves all available results in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAutoScalingConfigurations_RequestSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-request-NextToken"></a>
A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.
If you don't specify `NextToken`, the request retrieves the first result page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListAutoScalingConfigurations_ResponseSyntax"></a>

```
{
   "AutoScalingConfigurationSummaryList": [
      {
         "AutoScalingConfigurationArn": "string",
         "AutoScalingConfigurationName": "string",
         "AutoScalingConfigurationRevision": number,
         "CreatedAt": number,
         "HasAssociatedService": boolean,
         "IsDefault": boolean,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAutoScalingConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScalingConfigurationSummaryList](#API_ListAutoScalingConfigurations_ResponseSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-response-AutoScalingConfigurationSummaryList"></a>
A list of summary information records for auto scaling configurations. In a paginated request, the request returns up to `MaxResults` records for each call.
Type: Array of [AutoScalingConfigurationSummary](API_AutoScalingConfigurationSummary.md) objects

 ** [NextToken](#API_ListAutoScalingConfigurations_ResponseSyntax) **   <a name="apprunner-ListAutoScalingConfigurations-response-NextToken"></a>
The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListAutoScalingConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

## Examples
<a name="API_ListAutoScalingConfigurations_Examples"></a>

### Paginated listing of App Runner auto scaling configurations
<a name="API_ListAutoScalingConfigurations_Example_1"></a>

This example illustrates how to list all App Runner auto scaling configurations in your AWS account. Up to five auto scaling configurations are listed in each response. `AutoScalingConfigurationName` and `LatestOnly` aren't specified. Their defaults cause the latest revision of all active configurations to be listed.

In this example, the response includes two results and there aren't additional ones, so no `NextToken` is returned.

#### Sample Request
<a name="API_ListAutoScalingConfigurations_Example_1_Request"></a>

```
$ aws apprunner list-auto-scaling-configurations --cli-input-json "`cat`"
{
  "MaxResults": 5
}
```

#### Sample Response
<a name="API_ListAutoScalingConfigurations_Example_1_Response"></a>

```
{
  "AutoScalingConfigurationSummaryList": [
    {
      "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6",
      "AutoScalingConfigurationName": "high-availability",
      "AutoScalingConfigurationRevision": 2
    },
    {
      "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/low-cost/1/50d7804e7656fead0f59672e62f2e819",
      "AutoScalingConfigurationName": "low-cost",
      "AutoScalingConfigurationRevision": 1
    }
  ]
}
```

## See Also
<a name="API_ListAutoScalingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/ListAutoScalingConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListAutoScalingConfigurations)
