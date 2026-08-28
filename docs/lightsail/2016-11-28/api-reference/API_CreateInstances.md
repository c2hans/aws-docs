---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateInstances.html
---

# CreateInstances
<a name="API_CreateInstances"></a>

Creates one or more Amazon Lightsail instances.

The `create instances` operation supports tag-based access control via request tags. For more information, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateInstances_RequestSyntax"></a>

```
{
   "addOns": [
      {
         "addOnType": "{{string}}",
         "autoSnapshotAddOnRequest": {
            "snapshotTimeOfDay": "{{string}}"
         },
         "stopInstanceOnIdleRequest": {
            "duration": "{{string}}",
            "threshold": "{{string}}"
         }
      }
   ],
   "availabilityZone": "{{string}}",
   "blueprintId": "{{string}}",
   "bundleId": "{{string}}",
   "customImageName": "{{string}}",
   "instanceNames": [ "{{string}}" ],
   "ipAddressType": "{{string}}",
   "keyPairName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "userData": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addOns](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-addOns"></a>
An array of objects representing the add-ons to enable for the new instance.
Type: Array of [AddOnRequest](API_AddOnRequest.md) objects
Required: No

 ** [availabilityZone](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-availabilityZone"></a>
The Availability Zone in which to create your instance. Use the following format: `us-east-2a` (case sensitive). You can get a list of Availability Zones by using the [get regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html) operation. Be sure to add the `include Availability Zones` parameter to your request.
Type: String
Required: Yes

 ** [blueprintId](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-blueprintId"></a>
The ID for a virtual private server image (`app_wordpress_x_x` or `app_lamp_x_x`). Use the `get blueprints` operation to return a list of available images (or *blueprints*).
Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [bundleId](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-bundleId"></a>
The bundle of specification information for your virtual private server (or *instance*), including the pricing plan (`medium_x_x`).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [customImageName](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-customImageName"></a>
 *This parameter has been deprecated.*
(Discontinued) The name for your custom image.
In releases prior to June 12, 2017, this parameter was ignored by the API. It is now discontinued.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [instanceNames](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-instanceNames"></a>
The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: `["MyFirstInstance","MySecondInstance"]`
Type: Array of strings
Required: Yes

 ** [ipAddressType](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-ipAddressType"></a>
The IP address type for the instance.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
The default value is `dualstack`.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** [keyPairName](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-keyPairName"></a>
The name of your key pair.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [tags](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [userData](#API_CreateInstances_RequestSyntax) **   <a name="Lightsail-CreateInstances-request-userData"></a>
A launch script you can create that configures a server with additional user data. For example, you might want to run `apt-get -y update`.
Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image).
Type: String
Required: No

## Response Syntax
<a name="API_CreateInstances_ResponseSyntax"></a>

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
<a name="API_CreateInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateInstances_ResponseSyntax) **   <a name="Lightsail-CreateInstances-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateInstances_Errors"></a>

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
<a name="API_CreateInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
