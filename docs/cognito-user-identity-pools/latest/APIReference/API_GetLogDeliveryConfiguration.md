---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.html
---

# GetLogDeliveryConfiguration
<a name="API_GetLogDeliveryConfiguration"></a>

Given a user pool ID, returns the logging configuration. User pools can export message-delivery error and threat-protection activity logs to external AWS services. For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_GetLogDeliveryConfiguration_RequestSyntax"></a>

```
{
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLogDeliveryConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserPoolId](#API_GetLogDeliveryConfiguration_RequestSyntax) **   <a name="CognitoUserPools-GetLogDeliveryConfiguration-request-UserPoolId"></a>
The ID of the user pool that has the logging configuration that you want to view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_GetLogDeliveryConfiguration_ResponseSyntax"></a>

```
{
   "LogDeliveryConfiguration": {
      "LogConfigurations": [
         {
            "CloudWatchLogsConfiguration": {
               "LogGroupArn": "string"
            },
            "EventSource": "string",
            "FirehoseConfiguration": {
               "StreamArn": "string"
            },
            "LogLevel": "string",
            "S3Configuration": {
               "BucketArn": "string"
            }
         }
      ],
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_GetLogDeliveryConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LogDeliveryConfiguration](#API_GetLogDeliveryConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-GetLogDeliveryConfiguration-response-LogDeliveryConfiguration"></a>
The logging configuration of the requested user pool. Includes types of logs configured and their destinations.
Type: [LogDeliveryConfigurationType](API_LogDeliveryConfigurationType.md) object

## Errors
<a name="API_GetLogDeliveryConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_GetLogDeliveryConfiguration_Examples"></a>

### Example
<a name="API_GetLogDeliveryConfiguration_Example_1"></a>

The following example request returns the log delivery configuration for message-delivery errors to CloudWatch Logs and user activity to Amazon S3.

#### Sample Request
<a name="API_GetLogDeliveryConfiguration_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.GetLogDeliveryConfiguration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_GetLogDeliveryConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "LogDeliveryConfiguration": {
        "LogConfigurations": [
            {
                "CloudWatchLogsConfiguration": {
                    "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:cognito-exported"
                },
                "EventSource": "userNotification",
                "LogLevel": "ERROR"
            },
            {
                "EventSource": "userAuthEvents",
                "LogLevel": "INFO",
                "S3Configuration": {
                    "BucketArn": "arn:aws:s3:::amzn-s3-demo-bucket1"
                }
            }
        ],
        "UserPoolId": "us-west-2_EXAMPLE"
    }
}
```

## See Also
<a name="API_GetLogDeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)
