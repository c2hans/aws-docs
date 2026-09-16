---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html
---

# UpdateRelationalDatabase
<a name="API_UpdateRelationalDatabase"></a>

Allows the update of one or more attributes of a database in Amazon Lightsail.

Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database's predefined maintenance window.

The `update relational database` operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_UpdateRelationalDatabase_RequestSyntax"></a>

```
{
   "applyImmediately": {{boolean}},
   "caCertificateIdentifier": "{{string}}",
   "disableBackupRetention": {{boolean}},
   "enableBackupRetention": {{boolean}},
   "masterUserPassword": "{{string}}",
   "preferredBackupWindow": "{{string}}",
   "preferredMaintenanceWindow": "{{string}}",
   "publiclyAccessible": {{boolean}},
   "relationalDatabaseBlueprintId": "{{string}}",
   "relationalDatabaseName": "{{string}}",
   "rotateMasterUserPassword": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateRelationalDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applyImmediately](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-applyImmediately"></a>
When `true`, applies changes immediately. When `false`, applies changes during the preferred maintenance window. Some changes may cause an outage.
Default: `false`
Type: Boolean
Required: No

 ** [caCertificateIdentifier](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-caCertificateIdentifier"></a>
Indicates the certificate that needs to be associated with the database.
Type: String
Required: No

 ** [disableBackupRetention](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-disableBackupRetention"></a>
When `true`, disables automated backup retention for your database.
Disabling backup retention deletes all automated database backups. Before disabling this, you may want to create a snapshot of your database using the `create relational database snapshot` operation.
Updates are applied during the next maintenance window because this can result in an outage.
Type: Boolean
Required: No

 ** [enableBackupRetention](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-enableBackupRetention"></a>
When `true`, enables automated backup retention for your database.
Updates are applied during the next maintenance window because this can result in an outage.
Type: Boolean
Required: No

 ** [masterUserPassword](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-masterUserPassword"></a>
The password for the master user. The password can include any printable ASCII character except "/", """, or "@".
My**SQL**
Constraints: Must contain from 8 to 41 characters.
 **PostgreSQL**
Constraints: Must contain from 8 to 128 characters.
Type: String
Required: No

 ** [preferredBackupWindow](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-preferredBackupWindow"></a>
The daily time range during which automated backups are created for your database if automated backups are enabled.
Constraints:
+ Must be in the `hh24:mi-hh24:mi` format.

  Example: `16:00-16:30`
+ Specified in Coordinated Universal Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String
Required: No

 ** [preferredMaintenanceWindow](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-preferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur on your database.
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
Constraints:
+ Must be in the `ddd:hh24:mi-ddd:hh24:mi` format.
+ Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
+ Must be at least 30 minutes.
+ Specified in Coordinated Universal Time (UTC).
+ Example: `Tue:17:00-Tue:17:30`
Type: String
Required: No

 ** [publiclyAccessible](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-publiclyAccessible"></a>
Specifies the accessibility options for your database. A value of `true` specifies a database that is available to resources outside of your Lightsail account. A value of `false` specifies a database that is available only to your Lightsail resources in the same region as your database.
Type: Boolean
Required: No

 ** [relationalDatabaseBlueprintId](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-relationalDatabaseBlueprintId"></a>
This parameter is used to update the major version of the database. Enter the `blueprintId` for the major version that you want to update to.
Use the [GetRelationalDatabaseBlueprints](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRelationalDatabaseBlueprints.html) action to get a list of available blueprint IDs.
Type: String
Required: No

 ** [relationalDatabaseName](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-relationalDatabaseName"></a>
The name of your Lightsail database resource to update.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [rotateMasterUserPassword](#API_UpdateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-request-rotateMasterUserPassword"></a>
When `true`, the master user password is changed to a new strong password generated by Lightsail.
Use the `get relational database master user password` operation to get the new password.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateRelationalDatabase_ResponseSyntax"></a>

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
<a name="API_UpdateRelationalDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_UpdateRelationalDatabase_ResponseSyntax) **   <a name="Lightsail-UpdateRelationalDatabase-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_UpdateRelationalDatabase_Errors"></a>

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
<a name="API_UpdateRelationalDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateRelationalDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateRelationalDatabase)
