---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThing.html
---

# CreateThing
<a name="API_CreateThing"></a>

Creates a thing record in the registry. If this call is made multiple times using the same thing name and configuration, the call will succeed. If this call is made with the same thing name but different configuration a `ResourceAlreadyExistsException` is thrown.

**Note**
This is a control plane operation. See [Authorization](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html) for information about authorizing control plane actions.

Requires permission to access the [CreateThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateThing_RequestSyntax"></a>

```
POST /things/{{thingName}} HTTP/1.1
Content-type: application/json

{
   "attributePayload": {
      "attributes": {
         "{{string}}" : "{{string}}"
      },
      "merge": {{boolean}}
   },
   "billingGroupName": "{{string}}",
   "thingTypeName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_CreateThing_RequestSyntax) **   <a name="iot-CreateThing-request-uri-thingName"></a>
The name of the thing to create.
You can't change a thing's name after you create it. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributePayload](#API_CreateThing_RequestSyntax) **   <a name="iot-CreateThing-request-attributePayload"></a>
The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:
 `{\"attributes\":{\"string1\":\"string2\"}}`
Type: [AttributePayload](API_AttributePayload.md) object
Required: No

 ** [billingGroupName](#API_CreateThing_RequestSyntax) **   <a name="iot-CreateThing-request-billingGroupName"></a>
The name of the billing group the thing will be added to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [thingTypeName](#API_CreateThing_RequestSyntax) **   <a name="iot-CreateThing-request-thingTypeName"></a>
The name of the thing type associated with the new thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## Response Syntax
<a name="API_CreateThing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "thingArn": "string",
   "thingId": "string",
   "thingName": "string"
}
```

## Response Elements
<a name="API_CreateThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [thingArn](#API_CreateThing_ResponseSyntax) **   <a name="iot-CreateThing-response-thingArn"></a>
The ARN of the new thing.
Type: String

 ** [thingId](#API_CreateThing_ResponseSyntax) **   <a name="iot-CreateThing-response-thingId"></a>
The thing ID.
Type: String

 ** [thingName](#API_CreateThing_ResponseSyntax) **   <a name="iot-CreateThing-response-thingName"></a>
The name of the new thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateThing_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateThing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
