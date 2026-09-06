---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListServicesForAutoScalingConfiguration.html
---

# ListServicesForAutoScalingConfiguration
<a name="API_ListServicesForAutoScalingConfiguration"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Returns a list of the associated App Runner services using an auto scaling configuration.

## Request Syntax
<a name="API_ListServicesForAutoScalingConfiguration_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServicesForAutoScalingConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_ListServicesForAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-ListServicesForAutoScalingConfiguration-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to list the services for.
The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either `.../name ` or `.../name/revision `. If a revision isn't specified, the latest active revision is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

 ** [MaxResults](#API_ListServicesForAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-ListServicesForAutoScalingConfiguration-request-MaxResults"></a>
The maximum number of results to include in each response (result page). It's used for a paginated request.
If you don't specify `MaxResults`, the request retrieves all available results in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListServicesForAutoScalingConfiguration_RequestSyntax) **   <a name="apprunner-ListServicesForAutoScalingConfiguration-request-NextToken"></a>
A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.
If you don't specify `NextToken`, the request retrieves the first result page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListServicesForAutoScalingConfiguration_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ServiceArnList": [ "string" ]
}
```

## Response Elements
<a name="API_ListServicesForAutoScalingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServicesForAutoScalingConfiguration_ResponseSyntax) **   <a name="apprunner-ListServicesForAutoScalingConfiguration-response-NextToken"></a>
The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

 ** [ServiceArnList](#API_ListServicesForAutoScalingConfiguration_ResponseSyntax) **   <a name="apprunner-ListServicesForAutoScalingConfiguration-response-ServiceArnList"></a>
A list of service ARN records. In a paginated request, the request returns up to `MaxResults` records for each call.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`

## Errors
<a name="API_ListServicesForAutoScalingConfiguration_Errors"></a>

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
<a name="API_ListServicesForAutoScalingConfiguration_Examples"></a>

### Paginated listing of all App Runner services associated to an auto scaling configuration
<a name="API_ListServicesForAutoScalingConfiguration_Example_1"></a>

This example illustrates how to list all of the App Runner services that are associated with a specific auto scaling configuration. The response includes two results and a token that can be used in the next request. When a subsequent response doesn't include a token, all associated services have been listed.

#### Sample Request
<a name="API_ListServicesForAutoScalingConfiguration_Example_1_Request"></a>

```
$ aws apprunner list-services-for-auto-scaling-configuration --cli-input-json "`cat`"
{
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/6a4d47db94434d30a42cab9a00d21d44",
    "MaxResults": 2
}
```

#### Sample Response
<a name="API_ListServicesForAutoScalingConfiguration_Example_1_Response"></a>

```
{
    "ServiceArnList": [
        "arn:aws:apprunner:us-east-1:123456789012:service/golang-container-app/e598803c0a7848459f3fd978ef5ed86c",
        "arn:aws:apprunner:us-east-1:123456789012:service/java-app/b6644b84cd04451faaad27054a70e21a"
    ],
    "NextToken": "eyJBdXRvU2NhbGluZ0NvbmZpZ3VyYXRpb25Bcm4iOiJhcm46YXdzOmFwcHJ1bm5lcjp1cy1lYXN0LTE6MTIzNDU2Nzg5MDEyOmF1dG9zY2FsaW5nY29uZmlndXJhdGlvbi9oaWdoLWF2YWlsYWJpbGl0eS8yLzZhNGQ0N2RiOTQ0MzRkMzBhNDJjYWI5YTAwZDIxZDQ0IiwiU2VydmljZUFybiI6ImFybjphd3M6YXBwcnVubmVyOnVzLWVhc3QtMToxMjM0NTY3ODkwMTI6c2VydmljZS9ydW5sYWl5YW5nL2I2NjQ0Yjg0Y2QwNDQ1MWZhYWFkMjcwNTRhNzBlMjFhIn0="
}
```

## See Also
<a name="API_ListServicesForAutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListServicesForAutoScalingConfiguration)
