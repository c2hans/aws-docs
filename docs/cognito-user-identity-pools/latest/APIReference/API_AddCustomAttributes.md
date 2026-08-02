---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddCustomAttributes.html
---

# AddCustomAttributes
<a name="API_AddCustomAttributes"></a>

Adds additional user attributes to the user pool schema. Custom attributes can be mutable or immutable and have a `custom:` or `dev:` prefix. For more information, see [Custom attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-custom-attributes).

You can also create custom attributes in the [CreateUserPool](API_CreateUserPool.md) of `CreateUserPool` and `UpdateUserPool`. You can't delete custom attributes after you create them.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AddCustomAttributes_RequestSyntax"></a>

```
{
   "CustomAttributes": [
      {
         "AttributeDataType": "{{string}}",
         "DeveloperOnlyAttribute": {{boolean}},
         "Mutable": {{boolean}},
         "Name": "{{string}}",
         "NumberAttributeConstraints": {
            "MaxValue": "{{string}}",
            "MinValue": "{{string}}"
         },
         "Required": {{boolean}},
         "StringAttributeConstraints": {
            "MaxLength": "{{string}}",
            "MinLength": "{{string}}"
         }
      }
   ],
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AddCustomAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CustomAttributes](#API_AddCustomAttributes_RequestSyntax) **   <a name="CognitoUserPools-AddCustomAttributes-request-CustomAttributes"></a>
An array of custom attribute names and other properties. Sets the following characteristics:
AttributeDataType
The expected data type. Can be a string, a number, a date and time, or a boolean.
Mutable
If true, you can grant app clients write access to the attribute value. If false, the attribute value can only be set up on sign-up or administrator creation of users.
Name
The attribute name. For an attribute like `custom:myAttribute`, enter `myAttribute` for this field.
Required
When true, users who sign up or are created must set a value for the attribute.
NumberAttributeConstraints
The minimum and maximum length of accepted values for a `Number`-type attribute.
StringAttributeConstraints
The minimum and maximum length of accepted values for a `String`-type attribute.
DeveloperOnlyAttribute
This legacy option creates an attribute with a `dev:` prefix. You can only set the value of a developer-only attribute with administrative IAM credentials.
Type: Array of [SchemaAttributeType](API_SchemaAttributeType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** [UserPoolId](#API_AddCustomAttributes_RequestSyntax) **   <a name="CognitoUserPools-AddCustomAttributes-request-UserPoolId"></a>
The ID of the user pool where you want to add custom attributes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AddCustomAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddCustomAttributes_Errors"></a>

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

 ** UserImportInProgressException **
This exception is thrown when you're trying to modify a user pool while a user import job is in progress for that pool.
 ** message **
The message returned when the user pool has an import job running.
HTTP Status Code: 400

## Examples
<a name="API_AddCustomAttributes_Examples"></a>

### Example
<a name="API_AddCustomAttributes_Example_1"></a>

This example request adds the mutable custom attribute `custom:deliverables`, a string with a maximum length of 255 characters, to the user pool schema.

#### Sample Request
<a name="API_AddCustomAttributes_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AddCustomAttributes
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "CustomAttributes": [
        {
            "AttributeDataType": "String",
            "DeveloperOnlyAttribute": false,
            "Mutable": true,
            "Name": "deliverables",
            "Required": false,
            "StringAttributeConstraints": {
                "MaxLength": "255",
                "MinLength": "1"
            }
        }
    ],
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_AddCustomAttributes_Example_1_Response"></a>

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
<a name="API_AddCustomAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AddCustomAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AddCustomAttributes)
