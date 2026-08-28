---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePredefinedAttribute.html
---

# CreatePredefinedAttribute
<a name="API_CreatePredefinedAttribute"></a>

Creates a new predefined attribute for the specified Connect Customer instance. A *predefined attribute* is made up of a name and a value.

For the predefined attributes per instance quota, see [Connect Customer quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#connect-quotas).

 **Use cases**

Following are common uses cases for this API:
+ Create an attribute for routing proficiency (for example, agent certification) that has predefined values (for example, a list of possible certifications). For more information, see [Create predefined attributes for routing contacts to agents](https://docs.aws.amazon.com/connect/latest/adminguide/predefined-attributes.html).
+ Create an attribute for business unit name that has a list of predefined business unit names used in your organization. This is a use case where information for a contact varies between transfers or conferences. For more information, see [Use contact segment attributes](https://docs.aws.amazon.com/connect/latest/adminguide/use-contact-segment-attributes.html).

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_CreatePredefinedAttribute_RequestSyntax"></a>

```
PUT /predefined-attributes/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "AttributeConfiguration": {
      "EnableValueValidationOnAssociation": {{boolean}}
   },
   "Name": "{{string}}",
   "Purposes": [ "{{string}}" ],
   "Values": { ... }
}
```

## URI Request Parameters
<a name="API_CreatePredefinedAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreatePredefinedAttribute_RequestSyntax) **   <a name="connect-CreatePredefinedAttribute-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreatePredefinedAttribute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttributeConfiguration](#API_CreatePredefinedAttribute_RequestSyntax) **   <a name="connect-CreatePredefinedAttribute-request-AttributeConfiguration"></a>
Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.
Type: [InputPredefinedAttributeConfiguration](API_InputPredefinedAttributeConfiguration.md) object
Required: No

 ** [Name](#API_CreatePredefinedAttribute_RequestSyntax) **   <a name="connect-CreatePredefinedAttribute-request-Name"></a>
 The name of the predefined attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Purposes](#API_CreatePredefinedAttribute_RequestSyntax) **   <a name="connect-CreatePredefinedAttribute-request-Purposes"></a>
Values that enable you to categorize your predefined attributes. You can use them in custom UI elements across the Connect Customer admin website.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [Values](#API_CreatePredefinedAttribute_RequestSyntax) **   <a name="connect-CreatePredefinedAttribute-request-Values"></a>
 The values of the predefined attribute.
Type: [PredefinedAttributeValues](API_PredefinedAttributeValues.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_CreatePredefinedAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreatePredefinedAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreatePredefinedAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_CreatePredefinedAttribute_Examples"></a>

### Example
<a name="API_CreatePredefinedAttribute_Example_1"></a>

The following request and response example shows setting the proficiency on an attribute named Name1.

```
PUT https://connect.us-west-2.amazonaws.com/predefined-attributes/InstanceId HTTP/1.1
Content-type: application/json
{
    "Name": "Name1",
    "Values": {
        "StringList": [
            "value1"
        ]
    },
    "Purposes": [
        "proficiency"
    ],
    "Configuration": {
        "EnableValueValidationOnAssociation": true
    }
}

Response:
200
```

## See Also
<a name="API_CreatePredefinedAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreatePredefinedAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreatePredefinedAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
