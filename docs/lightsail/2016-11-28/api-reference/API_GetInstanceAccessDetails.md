---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstanceAccessDetails.html
---

# GetInstanceAccessDetails
<a name="API_GetInstanceAccessDetails"></a>

Returns temporary SSH keys you can use to connect to a specific virtual private server, or *instance*.

The `get instance access details` operation supports tag-based access control via resource tags applied to the resource identified by `instance name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_GetInstanceAccessDetails_RequestSyntax"></a>

```
{
   "instanceName": "{{string}}",
   "protocol": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInstanceAccessDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [instanceName](#API_GetInstanceAccessDetails_RequestSyntax) **   <a name="Lightsail-GetInstanceAccessDetails-request-instanceName"></a>
The name of the instance to access.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [protocol](#API_GetInstanceAccessDetails_RequestSyntax) **   <a name="Lightsail-GetInstanceAccessDetails-request-protocol"></a>
The protocol to use to connect to your instance. Defaults to `ssh`.
Type: String
Valid Values: `ssh | rdp`
Required: No

## Response Syntax
<a name="API_GetInstanceAccessDetails_ResponseSyntax"></a>

```
{
   "accessDetails": {
      "certKey": "string",
      "expiresAt": number,
      "hostKeys": [
         {
            "algorithm": "string",
            "fingerprintSHA1": "string",
            "fingerprintSHA256": "string",
            "notValidAfter": number,
            "notValidBefore": number,
            "publicKey": "string",
            "witnessedAt": number
         }
      ],
      "instanceName": "string",
      "ipAddress": "string",
      "ipv6Addresses": [ "string" ],
      "password": "string",
      "passwordData": {
         "ciphertext": "string",
         "keyPairName": "string"
      },
      "privateKey": "string",
      "protocol": "string",
      "username": "string"
   }
}
```

## Response Elements
<a name="API_GetInstanceAccessDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessDetails](#API_GetInstanceAccessDetails_ResponseSyntax) **   <a name="Lightsail-GetInstanceAccessDetails-response-accessDetails"></a>
An array of key-value pairs containing information about a get instance access request.
Type: [InstanceAccessDetails](API_InstanceAccessDetails.md) object

## Errors
<a name="API_GetInstanceAccessDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
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
<a name="API_GetInstanceAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetInstanceAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetInstanceAccessDetails)
