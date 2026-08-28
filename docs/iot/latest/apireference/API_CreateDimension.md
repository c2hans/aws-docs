---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDimension.html
---

# CreateDimension
<a name="API_CreateDimension"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Create a dimension that you can use to limit the scope of a metric used in a security profile for AWS IoT Device Defender. For example, using a `TOPIC_FILTER` dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.

Requires permission to access the [CreateDimension](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateDimension_RequestSyntax"></a>

```
POST /dimensions/{{name}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "stringValues": [ "{{string}}" ],
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDimension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateDimension_RequestSyntax) **   <a name="iot-CreateDimension-request-uri-name"></a>
A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateDimension_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateDimension_RequestSyntax) **   <a name="iot-CreateDimension-request-clientRequestToken"></a>
Each dimension must have a unique client request token. If you try to create a new dimension with the same token as a dimension that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [stringValues](#API_CreateDimension_RequestSyntax) **   <a name="iot-CreateDimension-request-stringValues"></a>
Specifies the value or list of values for the dimension. For `TOPIC_FILTER` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/\#").
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [tags](#API_CreateDimension_RequestSyntax) **   <a name="iot-CreateDimension-request-tags"></a>
Metadata that can be used to manage the dimension.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [type](#API_CreateDimension_RequestSyntax) **   <a name="iot-CreateDimension-request-type"></a>
Specifies the type of dimension. Supported types: `TOPIC_FILTER.`
Type: String
Valid Values: `TOPIC_FILTER`
Required: Yes

## Response Syntax
<a name="API_CreateDimension_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateDimension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDimension_ResponseSyntax) **   <a name="iot-CreateDimension-response-arn"></a>
The Amazon Resource Name (ARN) of the created dimension.
Type: String

 ** [name](#API_CreateDimension_ResponseSyntax) **   <a name="iot-CreateDimension-response-name"></a>
A unique identifier for the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateDimension_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateDimension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateDimension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateDimension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateDimension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateDimension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateDimension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateDimension)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
