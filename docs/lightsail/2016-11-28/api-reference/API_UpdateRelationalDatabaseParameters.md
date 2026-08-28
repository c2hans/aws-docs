---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabaseParameters.html
---

# UpdateRelationalDatabaseParameters
<a name="API_UpdateRelationalDatabaseParameters"></a>

Allows the update of one or more parameters of a database in Amazon Lightsail.

Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which parameter updates are applied: `dynamic` or `pending-reboot`. Parameters marked with a `dynamic` apply type are applied immediately. Parameters marked with a `pending-reboot` apply type are applied only after the database is rebooted using the `reboot relational database` operation.

The `update relational database parameters` operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_UpdateRelationalDatabaseParameters_RequestSyntax"></a>

```
{
   "parameters": [
      {
         "allowedValues": "{{string}}",
         "applyMethod": "{{string}}",
         "applyType": "{{string}}",
         "dataType": "{{string}}",
         "description": "{{string}}",
         "isModifiable": {{boolean}},
         "parameterName": "{{string}}",
         "parameterValue": "{{string}}"
      }
   ],
   "relationalDatabaseName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRelationalDatabaseParameters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [parameters](#API_UpdateRelationalDatabaseParameters_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabaseParameters-request-parameters"></a>
The database parameters to update.
Type: Array of [RelationalDatabaseParameter](API_RelationalDatabaseParameter.md) objects
Required: Yes

 ** [relationalDatabaseName](#API_UpdateRelationalDatabaseParameters_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabaseParameters-request-relationalDatabaseName"></a>
The name of your database for which to update parameters.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_UpdateRelationalDatabaseParameters_ResponseSyntax"></a>

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
<a name="API_UpdateRelationalDatabaseParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_UpdateRelationalDatabaseParameters_ResponseSyntax) **   <a name="Lightsail-UpdateRelationalDatabaseParameters-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_UpdateRelationalDatabaseParameters_Errors"></a>

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
<a name="API_UpdateRelationalDatabaseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateRelationalDatabaseParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
