---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateBillingGroup.html
---

# CreateBillingGroup
<a name="API_CreateBillingGroup"></a>

Creates a billing group. If this call is made multiple times using the same billing group name and configuration, the call will succeed. If this call is made with the same billing group name but different configuration a `ResourceAlreadyExistsException` is thrown.

Requires permission to access the [CreateBillingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateBillingGroup_RequestSyntax"></a>

```
POST /billing-groups/{{billingGroupName}} HTTP/1.1
Content-type: application/json

{
   "billingGroupProperties": {
      "billingGroupDescription": "{{string}}"
   },
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateBillingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [billingGroupName](#API_CreateBillingGroup_RequestSyntax) **   <a name="iot-CreateBillingGroup-request-uri-billingGroupName"></a>
The name you wish to give to the billing group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateBillingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [billingGroupProperties](#API_CreateBillingGroup_RequestSyntax) **   <a name="iot-CreateBillingGroup-request-billingGroupProperties"></a>
The properties of the billing group.
Type: [BillingGroupProperties](API_BillingGroupProperties.md) object
Required: No

 ** [tags](#API_CreateBillingGroup_RequestSyntax) **   <a name="iot-CreateBillingGroup-request-tags"></a>
Metadata which can be used to manage the billing group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateBillingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "billingGroupArn": "string",
   "billingGroupId": "string",
   "billingGroupName": "string"
}
```

## Response Elements
<a name="API_CreateBillingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingGroupArn](#API_CreateBillingGroup_ResponseSyntax) **   <a name="iot-CreateBillingGroup-response-billingGroupArn"></a>
The ARN of the billing group.
Type: String

 ** [billingGroupId](#API_CreateBillingGroup_ResponseSyntax) **   <a name="iot-CreateBillingGroup-response-billingGroupId"></a>
The ID of the billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

 ** [billingGroupName](#API_CreateBillingGroup_ResponseSyntax) **   <a name="iot-CreateBillingGroup-response-billingGroupName"></a>
The name you gave to the billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateBillingGroup_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateBillingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateBillingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateBillingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
