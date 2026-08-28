---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBlueprints.html
---

# GetBlueprints
<a name="API_GetBlueprints"></a>

Returns the list of available instance images, or *blueprints*. You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.

**Note**
Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.

## Request Syntax
<a name="API_GetBlueprints_RequestSyntax"></a>

```
{
   "appCategory": "{{string}}",
   "includeInactive": {{boolean}},
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBlueprints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [appCategory](#API_GetBlueprints_RequestSyntax) **   <a name="Lightsail-GetBlueprints-request-appCategory"></a>
Returns a list of blueprints that are specific to Lightsail for Research.
You must use this parameter to view Lightsail for Research blueprints.
Type: String
Valid Values: `LfR`
Required: No

 ** [includeInactive](#API_GetBlueprints_RequestSyntax) **   <a name="Lightsail-GetBlueprints-request-includeInactive"></a>
A Boolean value that indicates whether to include inactive (unavailable) blueprints in the response of your request.
Type: Boolean
Required: No

 ** [pageToken](#API_GetBlueprints_RequestSyntax) **   <a name="Lightsail-GetBlueprints-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetBlueprints` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetBlueprints_ResponseSyntax"></a>

```
{
   "blueprints": [
      {
         "appCategory": "string",
         "blueprintId": "string",
         "description": "string",
         "group": "string",
         "isActive": boolean,
         "licenseUrl": "string",
         "minPower": number,
         "name": "string",
         "platform": "string",
         "productUrl": "string",
         "type": "string",
         "version": "string",
         "versionCode": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetBlueprints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blueprints](#API_GetBlueprints_ResponseSyntax) **   <a name="Lightsail-GetBlueprints-response-blueprints"></a>
An array of key-value pairs that contains information about the available blueprints.
Type: Array of [Blueprint](API_Blueprint.md) objects

 ** [nextPageToken](#API_GetBlueprints_ResponseSyntax) **   <a name="Lightsail-GetBlueprints-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetBlueprints` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetBlueprints_Errors"></a>

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
<a name="API_GetBlueprints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetBlueprints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetBlueprints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
