---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html
---

# AddApplicationVpcConfiguration
<a name="API_AddApplicationVpcConfiguration"></a>

Adds a Virtual Private Cloud (VPC) configuration to the application. Applications can use VPCs to store and access resources securely.

Note the following about VPC configurations for Managed Service for Apache Flink applications:
+ VPC configurations are not supported for SQL applications.
+ When a VPC is added to a Managed Service for Apache Flink application, the application can no longer be accessed from the Internet directly. To enable Internet access to the application, add an Internet gateway to your VPC.

## Request Syntax
<a name="API_AddApplicationVpcConfiguration_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "ConditionalToken": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "VpcConfiguration": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_AddApplicationVpcConfiguration_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ConditionalToken](#API_AddApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-request-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates. You must provide the `ApplicationVersionID` or the `ConditionalToken`. You get the application's current `ConditionalToken` using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** [CurrentApplicationVersionId](#API_AddApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-request-CurrentApplicationVersionId"></a>
The version of the application to which you want to add the VPC configuration. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned. For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** [VpcConfiguration](#API_AddApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-request-VpcConfiguration"></a>
Description of the VPC to add to the application.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_AddApplicationVpcConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "OperationId": "string",
   "VpcConfigurationDescription": {
      "SecurityGroupIds": [ "string" ],
      "SubnetIds": [ "string" ],
      "VpcConfigurationId": "string",
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_AddApplicationVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-response-ApplicationARN"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-response-ApplicationVersionId"></a>
Provides the current application version. Managed Service for Apache Flink updates the ApplicationVersionId each time you update the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [OperationId](#API_AddApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [VpcConfigurationDescription](#API_AddApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationVpcConfiguration-response-VpcConfigurationDescription"></a>
The parameters of the new VPC configuration.
Type: [VpcConfigurationDescription](API_VpcConfigurationDescription.md) object

## Errors
<a name="API_AddApplicationVpcConfiguration_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidApplicationConfigurationException **
The user-provided application configuration is not valid.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_AddApplicationVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationVpcConfiguration)
