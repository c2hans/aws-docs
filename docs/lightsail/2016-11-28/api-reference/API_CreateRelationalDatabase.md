---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateRelationalDatabase.html
---

# CreateRelationalDatabase
<a name="API_CreateRelationalDatabase"></a>

Creates a new database in Amazon Lightsail.

The `create relational database` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateRelationalDatabase_RequestSyntax"></a>

```
{
   "availabilityZone": "{{string}}",
   "masterDatabaseName": "{{string}}",
   "masterUsername": "{{string}}",
   "masterUserPassword": "{{string}}",
   "preferredBackupWindow": "{{string}}",
   "preferredMaintenanceWindow": "{{string}}",
   "publiclyAccessible": {{boolean}},
   "relationalDatabaseBlueprintId": "{{string}}",
   "relationalDatabaseBundleId": "{{string}}",
   "relationalDatabaseName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRelationalDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-availabilityZone"></a>
The Availability Zone in which to create your new database. Use the `us-east-2a` case-sensitive format.
You can get a list of Availability Zones by using the `get regions` operation. Be sure to add the `include relational database Availability Zones` parameter to your request.
Type: String
Required: No

 ** [masterDatabaseName](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-masterDatabaseName"></a>
The meaning of this parameter differs according to the database engine you use.
 **MySQL**
The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.
Constraints:
+ Must contain 1 to 64 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).
+ Can't be a word reserved by the specified database engine.

  For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html), [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html), and [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).
 **PostgreSQL**
The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named `postgres` is created in the database resource.
Constraints:
+ Must contain 1 to 63 letters or numbers.
+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).
+ Can't be a word reserved by the specified database engine.

  For more information about reserved words in PostgreSQL, see the SQL Key Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html), [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html), [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html), and [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html).
Type: String
Required: Yes

 ** [masterUsername](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-masterUsername"></a>
The name for the master user.
 **MySQL**
Constraints:
+ Required for MySQL.
+ Must be 1 to 16 letters or numbers. Can contain underscores.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.

  For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html), [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html), or [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).
 **PostgreSQL**
Constraints:
+ Required for PostgreSQL.
+ Must be 1 to 63 letters or numbers. Can contain underscores.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.

  For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html), [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html), [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html), and [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html).
Type: String
Required: Yes

 ** [masterUserPassword](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-masterUserPassword"></a>
The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It cannot contain spaces.
 **MySQL**
Constraints: Must contain from 8 to 41 characters.
 **PostgreSQL**
Constraints: Must contain from 8 to 128 characters.
Type: String
Required: No

 ** [preferredBackupWindow](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-preferredBackupWindow"></a>
The daily time range during which automated backups are created for your new database if automated backups are enabled.
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the [Working With Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) guide in the Amazon Relational Database Service documentation.
Constraints:
+ Must be in the `hh24:mi-hh24:mi` format.

  Example: `16:00-16:30`
+ Specified in Coordinated Universal Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String
Required: No

 ** [preferredMaintenanceWindow](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-preferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur on your new database.
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
Constraints:
+ Must be in the `ddd:hh24:mi-ddd:hh24:mi` format.
+ Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
+ Must be at least 30 minutes.
+ Specified in Coordinated Universal Time (UTC).
+ Example: `Tue:17:00-Tue:17:30`
Type: String
Required: No

 ** [publiclyAccessible](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-publiclyAccessible"></a>
Specifies the accessibility options for your new database. A value of `true` specifies a database that is available to resources outside of your Lightsail account. A value of `false` specifies a database that is available only to your Lightsail resources in the same region as your database.
Type: Boolean
Required: No

 ** [relationalDatabaseBlueprintId](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-relationalDatabaseBlueprintId"></a>
The blueprint ID for your new database. A blueprint describes the major engine version of a database.
You can get a list of database blueprints IDs by using the `get relational database blueprints` operation.
Type: String
Required: Yes

 ** [relationalDatabaseBundleId](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-relationalDatabaseBundleId"></a>
The bundle ID for your new database. A bundle describes the performance specifications for your database.
You can get a list of database bundle IDs by using the `get relational database bundles` operation.
Type: String
Required: Yes

 ** [relationalDatabaseName](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-relationalDatabaseName"></a>
The name to use for your new Lightsail database resource.
Constraints:
+ Must contain from 2 to 255 alphanumeric characters, or hyphens.
+ The first and last character must be a letter or number.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [tags](#API_CreateRelationalDatabase_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabase-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateRelationalDatabase_ResponseSyntax"></a>

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
<a name="API_CreateRelationalDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateRelationalDatabase_ResponseSyntax) **   <a name="Lightsail-CreateRelationalDatabase-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateRelationalDatabase_Errors"></a>

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
<a name="API_CreateRelationalDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateRelationalDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateRelationalDatabase)
