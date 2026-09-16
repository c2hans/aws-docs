---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRelationalDatabaseMasterUserPassword.html
---

# GetRelationalDatabaseMasterUserPassword
<a name="API_GetRelationalDatabaseMasterUserPassword"></a>

Returns the current, previous, or pending versions of the master user password for a Lightsail database.

The `GetRelationalDatabaseMasterUserPassword` operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName.

## Request Syntax
<a name="API_GetRelationalDatabaseMasterUserPassword_RequestSyntax"></a>

```
{
   "passwordVersion": "{{string}}",
   "relationalDatabaseName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRelationalDatabaseMasterUserPassword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [passwordVersion](#API_GetRelationalDatabaseMasterUserPassword_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseMasterUserPassword-request-passwordVersion"></a>
The password version to return.
Specifying `CURRENT` or `PREVIOUS` returns the current or previous passwords respectively. Specifying `PENDING` returns the newest version of the password that will rotate to `CURRENT`. After the `PENDING` password rotates to `CURRENT`, the `PENDING` password is no longer available.
Default: `CURRENT`
Type: String
Valid Values: `CURRENT | PREVIOUS | PENDING`
Required: No

 ** [relationalDatabaseName](#API_GetRelationalDatabaseMasterUserPassword_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseMasterUserPassword-request-relationalDatabaseName"></a>
The name of your database for which to get the master user password.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_GetRelationalDatabaseMasterUserPassword_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "masterUserPassword": "string"
}
```

## Response Elements
<a name="API_GetRelationalDatabaseMasterUserPassword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetRelationalDatabaseMasterUserPassword_ResponseSyntax) **   <a name="Lightsail-GetRelationalDatabaseMasterUserPassword-response-createdAt"></a>
The timestamp when the specified version of the master user password was created.
Type: Timestamp

 ** [masterUserPassword](#API_GetRelationalDatabaseMasterUserPassword_ResponseSyntax) **   <a name="Lightsail-GetRelationalDatabaseMasterUserPassword-response-masterUserPassword"></a>
The master user password for the `password version` specified.
Type: String

## Errors
<a name="API_GetRelationalDatabaseMasterUserPassword_Errors"></a>

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
<a name="API_GetRelationalDatabaseMasterUserPassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword)
