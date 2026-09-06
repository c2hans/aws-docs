---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateGUISessionAccessDetails.html
---

# CreateGUISessionAccessDetails
<a name="API_CreateGUISessionAccessDetails"></a>

Creates two URLs that are used to access a virtual computer’s graphical user interface (GUI) session. The primary URL initiates a web-based Amazon DCV session to the virtual computer's application. The secondary URL initiates a web-based Amazon DCV session to the virtual computer's operating session.

Use `StartGUISession` to open the session.

## Request Syntax
<a name="API_CreateGUISessionAccessDetails_RequestSyntax"></a>

```
{
   "resourceName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateGUISessionAccessDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceName](#API_CreateGUISessionAccessDetails_RequestSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-request-resourceName"></a>
The resource name.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_CreateGUISessionAccessDetails_ResponseSyntax"></a>

```
{
   "failureReason": "string",
   "percentageComplete": number,
   "resourceName": "string",
   "sessions": [
      {
         "isPrimary": boolean,
         "name": "string",
         "url": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_CreateGUISessionAccessDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failureReason](#API_CreateGUISessionAccessDetails_ResponseSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-response-failureReason"></a>
The reason the operation failed.
Type: String

 ** [percentageComplete](#API_CreateGUISessionAccessDetails_ResponseSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-response-percentageComplete"></a>
The percentage of completion for the operation.
Type: Integer

 ** [resourceName](#API_CreateGUISessionAccessDetails_ResponseSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-response-resourceName"></a>
The resource name.
Type: String
Pattern: `\w[\w\-]*\w`

 ** [sessions](#API_CreateGUISessionAccessDetails_ResponseSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-response-sessions"></a>
Returns information about the specified Amazon DCV GUI session.
Type: Array of [Session](API_Session.md) objects

 ** [status](#API_CreateGUISessionAccessDetails_ResponseSyntax) **   <a name="Lightsail-CreateGUISessionAccessDetails-response-status"></a>
The status of the operation.
Type: String
Valid Values: `startExpired | notStarted | started | starting | stopped | stopping | settingUpInstance | failedInstanceCreation | failedStartingGUISession | failedStoppingGUISession`

## Errors
<a name="API_CreateGUISessionAccessDetails_Errors"></a>

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
<a name="API_CreateGUISessionAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateGUISessionAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateGUISessionAccessDetails)
