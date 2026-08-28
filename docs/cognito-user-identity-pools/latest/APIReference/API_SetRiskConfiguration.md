---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.html
---

# SetRiskConfiguration
<a name="API_SetRiskConfiguration"></a>

Configures threat protection for a user pool or app client. Sets configuration for the following.
+ Responses to risks with adaptive authentication
+ Responses to vulnerable passwords with compromised-credentials detection
+ Notifications to users who have had risky activity detected
+ IP-address denylist and allowlist

To set the risk configuration for the user pool to defaults, send this request with only the `UserPoolId` parameter. To reset the threat protection settings of an app client to be inherited from the user pool, send `UserPoolId` and `ClientId` parameters only. To change threat protection to audit-only or off, update the value of `UserPoolAddOns` in an `UpdateUserPool` request. To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).

In secondary regions for user pools with multi-region replication, only the `SourceARN` and `From` attributes of `NotifyConfiguration` can be modified to configure region-specific SES integration. All other risk configuration settings must match the existing values to maintain consistency across replicas.

## Request Syntax
<a name="API_SetRiskConfiguration_RequestSyntax"></a>

```
{
   "AccountTakeoverRiskConfiguration": {
      "Actions": {
         "HighAction": {
            "EventAction": "{{string}}",
            "Notify": {{boolean}}
         },
         "LowAction": {
            "EventAction": "{{string}}",
            "Notify": {{boolean}}
         },
         "MediumAction": {
            "EventAction": "{{string}}",
            "Notify": {{boolean}}
         }
      },
      "NotifyConfiguration": {
         "BlockEmail": {
            "HtmlBody": "{{string}}",
            "Subject": "{{string}}",
            "TextBody": "{{string}}"
         },
         "From": "{{string}}",
         "MfaEmail": {
            "HtmlBody": "{{string}}",
            "Subject": "{{string}}",
            "TextBody": "{{string}}"
         },
         "NoActionEmail": {
            "HtmlBody": "{{string}}",
            "Subject": "{{string}}",
            "TextBody": "{{string}}"
         },
         "ReplyTo": "{{string}}",
         "SourceArn": "{{string}}"
      }
   },
   "ClientId": "{{string}}",
   "CompromisedCredentialsRiskConfiguration": {
      "Actions": {
         "EventAction": "{{string}}"
      },
      "EventFilter": [ "{{string}}" ]
   },
   "RiskExceptionConfiguration": {
      "BlockedIPRangeList": [ "{{string}}" ],
      "SkippedIPRangeList": [ "{{string}}" ]
   },
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_SetRiskConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountTakeoverRiskConfiguration](#API_SetRiskConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-request-AccountTakeoverRiskConfiguration"></a>
The settings for automated responses and notification templates for adaptive authentication with threat protection.
Type: [AccountTakeoverRiskConfigurationType](API_AccountTakeoverRiskConfigurationType.md) object
Required: No

 ** [ClientId](#API_SetRiskConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-request-ClientId"></a>
The ID of the app client where you want to set a risk configuration. If `ClientId` is null, then the risk configuration is mapped to `UserPoolId`. When the client ID is null, the same risk configuration is applied to all the clients in the userPool.
When you include a `ClientId` parameter, Amazon Cognito maps the configuration to the app client. When you include both `ClientId` and `UserPoolId`, Amazon Cognito maps the configuration to the app client only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** [CompromisedCredentialsRiskConfiguration](#API_SetRiskConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-request-CompromisedCredentialsRiskConfiguration"></a>
The configuration of automated reactions to detected compromised credentials. Includes settings for blocking future sign-in requests and for the types of password-submission events you want to monitor.
Type: [CompromisedCredentialsRiskConfigurationType](API_CompromisedCredentialsRiskConfigurationType.md) object
Required: No

 ** [RiskExceptionConfiguration](#API_SetRiskConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-request-RiskExceptionConfiguration"></a>
A set of IP-address overrides to threat protection. You can set up IP-address always-block and always-allow lists.
Type: [RiskExceptionConfigurationType](API_RiskExceptionConfigurationType.md) object
Required: No

 ** [UserPoolId](#API_SetRiskConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-request-UserPoolId"></a>
The ID of the user pool where you want to set a risk configuration. If you include `UserPoolId` in your request, don't include `ClientId`. When the client ID is null, the same risk configuration is applied to all the clients in the userPool. When you include both `ClientId` and `UserPoolId`, Amazon Cognito maps the configuration to the app client only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_SetRiskConfiguration_ResponseSyntax"></a>

```
{
   "RiskConfiguration": {
      "AccountTakeoverRiskConfiguration": {
         "Actions": {
            "HighAction": {
               "EventAction": "string",
               "Notify": boolean
            },
            "LowAction": {
               "EventAction": "string",
               "Notify": boolean
            },
            "MediumAction": {
               "EventAction": "string",
               "Notify": boolean
            }
         },
         "NotifyConfiguration": {
            "BlockEmail": {
               "HtmlBody": "string",
               "Subject": "string",
               "TextBody": "string"
            },
            "From": "string",
            "MfaEmail": {
               "HtmlBody": "string",
               "Subject": "string",
               "TextBody": "string"
            },
            "NoActionEmail": {
               "HtmlBody": "string",
               "Subject": "string",
               "TextBody": "string"
            },
            "ReplyTo": "string",
            "SourceArn": "string"
         }
      },
      "ClientId": "string",
      "CompromisedCredentialsRiskConfiguration": {
         "Actions": {
            "EventAction": "string"
         },
         "EventFilter": [ "string" ]
      },
      "LastModifiedDate": number,
      "RiskExceptionConfiguration": {
         "BlockedIPRangeList": [ "string" ],
         "SkippedIPRangeList": [ "string" ]
      },
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_SetRiskConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RiskConfiguration](#API_SetRiskConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-SetRiskConfiguration-response-RiskConfiguration"></a>
The API response that contains the risk configuration that you set and the timestamp of the most recent change.
Type: [RiskConfigurationType](API_RiskConfigurationType.md) object

## Errors
<a name="API_SetRiskConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeDeliveryFailureException **
This exception is thrown when a verification code fails to deliver successfully.
 ** message **
The message sent when a verification code fails to deliver successfully.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidEmailRoleAccessPolicyException **
This exception is thrown when Amazon Cognito isn't allowed to use your email identity. HTTP status code: 400.
 ** message **
The message returned when you have an unverified email address or the identity policy isn't set on an email address that Amazon Cognito can access.
HTTP Status Code: 400

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

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
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

 ** UserPoolAddOnNotEnabledException **
This exception is thrown when user pool add-ons aren't enabled.
HTTP Status Code: 400

## Examples
<a name="API_SetRiskConfiguration_Examples"></a>

### Example
<a name="API_SetRiskConfiguration_Example_1"></a>

The following example request configures the requested app client with adaptive authentication actions, compromised-credentials behavior, and IP-address exceptions. It also configures user notification templates.

#### Sample Request
<a name="API_SetRiskConfiguration_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SetRiskConfiguration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "AccountTakeoverRiskConfiguration": {
        "Actions": {
            "HighAction": {
                "EventAction": "MFA_REQUIRED",
                "Notify": true
            },
            "LowAction": {
                "EventAction": "NO_ACTION",
                "Notify": true
            },
            "MediumAction": {
                "EventAction": "MFA_IF_CONFIGURED",
                "Notify": true
            }
        },
        "NotifyConfiguration": {
            "BlockEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "Blocked sign-in attempt",
                "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "From": "admin@example.com",
            "MfaEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "New sign-in attempt",
                "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "NoActionEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "New sign-in attempt",
                "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "ReplyTo": "Administrator <admin@example.com>",
            "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com"
        }
    },
    "ClientId": "1example23456789",
    "CompromisedCredentialsRiskConfiguration": {
        "Actions": {
            "EventAction": "BLOCK"
        },
        "EventFilter": [
            "PASSWORD_CHANGE",
            "SIGN_UP",
            "SIGN_IN"
        ]
    },
    "RiskExceptionConfiguration": {
        "BlockedIPRangeList": [
            "192.0.2.1/32",
            "192.0.2.2/32"
        ],
        "SkippedIPRangeList": [
            "203.0.113.1/32",
            "203.0.113.2/32"
        ]
    },
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_SetRiskConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "RiskConfiguration": {
        "AccountTakeoverRiskConfiguration": {
            "Actions": {
                "HighAction": {
                    "EventAction": "MFA_REQUIRED",
                    "Notify": true
                },
                "LowAction": {
                    "EventAction": "NO_ACTION",
                    "Notify": true
                },
                "MediumAction": {
                    "EventAction": "MFA_IF_CONFIGURED",
                    "Notify": true
                }
            },
            "NotifyConfiguration": {
                "BlockEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "Blocked sign-in attempt",
                    "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "From": "admin@example.com",
                "MfaEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "New sign-in attempt",
                    "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "NoActionEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "New sign-in attempt",
                    "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "ReplyTo": "admin@example.com",
                "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com"
            }
        },
        "ClientId": "1example23456789",
        "CompromisedCredentialsRiskConfiguration": {
            "Actions": {
                "EventAction": "BLOCK"
            },
            "EventFilter": [
                "PASSWORD_CHANGE",
                "SIGN_UP",
                "SIGN_IN"
            ]
        },
        "RiskExceptionConfiguration": {
            "BlockedIPRangeList": [
                "192.0.2.1/32",
                "192.0.2.2/32"
            ],
            "SkippedIPRangeList": [
                "203.0.113.1/32",
                "203.0.113.2/32"
            ]
        },
        "UserPoolId": "us-west-2_EXAMPLE"
    }
}
```

### Example
<a name="API_SetRiskConfiguration_Example_2"></a>

The following example request clears the threat protection settings of the requested app client.

#### Sample Request
<a name="API_SetRiskConfiguration_Example_2_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SetRiskConfiguration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "ClientId": "1example23456789",
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_SetRiskConfiguration_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

### Example
<a name="API_SetRiskConfiguration_Example_3"></a>

The following example request resets threat protection settings to default for the requested user pool.

#### Sample Request
<a name="API_SetRiskConfiguration_Example_3_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SetRiskConfiguration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_SetRiskConfiguration_Example_3_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

## See Also
<a name="API_SetRiskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/SetRiskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SetRiskConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
