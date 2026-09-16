---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetupInstanceHttps.html
---

# SetupInstanceHttps
<a name="API_SetupInstanceHttps"></a>

Creates an SSL/TLS certificate that secures traffic for your website. After the certificate is created, it is installed on the specified Lightsail instance.

If you provide more than one domain name in the request, at least one name must be less than or equal to 63 characters in length.

## Request Syntax
<a name="API_SetupInstanceHttps_RequestSyntax"></a>

```
{
   "certificateProvider": "{{string}}",
   "domainNames": [ "{{string}}" ],
   "emailAddress": "{{string}}",
   "instanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_SetupInstanceHttps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateProvider](#API_SetupInstanceHttps_RequestSyntax) **   <a name="Lightsail-SetupInstanceHttps-request-certificateProvider"></a>
The certificate authority that issues the SSL/TLS certificate.
Type: String
Valid Values: `LetsEncrypt`
Required: Yes

 ** [domainNames](#API_SetupInstanceHttps_RequestSyntax) **   <a name="Lightsail-SetupInstanceHttps-request-domainNames"></a>
The name of the domain and subdomains that were specified for the SSL/TLS certificate.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 4. Maximum length of 253.
Pattern: `^[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z0-9\-]{1,63}){0,8}(\.[a-zA-Z]{2,63})$`
Required: Yes

 ** [emailAddress](#API_SetupInstanceHttps_RequestSyntax) **   <a name="Lightsail-SetupInstanceHttps-request-emailAddress"></a>
The contact method for SSL/TLS certificate renewal alerts. You can enter one email address.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 254.
Pattern: `^[\w!#$%&.'*+\/=?^_\x60{|}~\-]{1,64}@[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z0-9\-]{1,63}){0,8}(\.[a-zA-Z]{2,63})$`
Required: Yes

 ** [instanceName](#API_SetupInstanceHttps_RequestSyntax) **   <a name="Lightsail-SetupInstanceHttps-request-instanceName"></a>
The name of the Lightsail instance.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_SetupInstanceHttps_ResponseSyntax"></a>

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
<a name="API_SetupInstanceHttps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_SetupInstanceHttps_ResponseSyntax) **   <a name="Lightsail-SetupInstanceHttps-response-operations"></a>
The available API operations for `SetupInstanceHttps`.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_SetupInstanceHttps_Errors"></a>

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
<a name="API_SetupInstanceHttps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/SetupInstanceHttps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetupInstanceHttps)
