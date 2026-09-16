---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateContactMethod.html
---

# CreateContactMethod
<a name="API_CreateContactMethod"></a>

Creates an email or SMS text message contact method.

A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each AWS Region. However, SMS text messaging is not supported in some AWS Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see [Notifications in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications).

The `create contact method` operation supports tag-based access control via request tags. For more information, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateContactMethod_RequestSyntax"></a>

```
{
   "contactEndpoint": "{{string}}",
   "protocol": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateContactMethod_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [contactEndpoint](#API_CreateContactMethod_RequestSyntax) **   <a name="Lightsail-CreateContactMethod-request-contactEndpoint"></a>
The destination of the contact method, such as an email address or a mobile phone number.
Use the E.164 format when specifying a mobile phone number. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (\+) and the country code. For example, a U.S. phone number in E.164 format would be specified as \+1XXX5550100. For more information, see [E.164](https://en.wikipedia.org/wiki/E.164) on *Wikipedia*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [protocol](#API_CreateContactMethod_RequestSyntax) **   <a name="Lightsail-CreateContactMethod-request-protocol"></a>
The protocol of the contact method, such as `Email` or `SMS` (text messaging).
The `SMS` protocol is supported only in the following AWS Regions.
+ US East (N. Virginia) (`us-east-1`)
+ US West (Oregon) (`us-west-2`)
+ Europe (Ireland) (`eu-west-1`)
+ Asia Pacific (Tokyo) (`ap-northeast-1`)
+ Asia Pacific (Singapore) (`ap-southeast-1`)
+ Asia Pacific (Sydney) (`ap-southeast-2`)
For a list of countries/regions where SMS text messages can be sent, and the latest AWS Regions where SMS text messaging is supported, see [Supported Regions and Countries](https://docs.aws.amazon.com/sns/latest/dg/sns-supported-regions-countries.html) in the *Amazon SNS Developer Guide*.
For more information about notifications in Amazon Lightsail, see [Notifications in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications).
Type: String
Valid Values: `Email | SMS`
Required: Yes

 ** [tags](#API_CreateContactMethod_RequestSyntax) **   <a name="Lightsail-CreateContactMethod-request-tags"></a>
The tag keys and optional values to add to the contact method during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateContactMethod_ResponseSyntax"></a>

```
{
   "operations": [
      {
         "createdAt": number,
         "errorCode": "string",
         "errorDetails": "string",
         "id": "string",
         "isTerminal": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "operationDetails": "string",
         "operationType": "string",
         "resourceName": "string",
         "resourceType": "string",
         "status": "string",
         "statusChangedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_CreateContactMethod_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateContactMethod_ResponseSyntax) **   <a name="Lightsail-CreateContactMethod-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateContactMethod_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_CreateContactMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateContactMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateContactMethod)
