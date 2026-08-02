---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabaseConnectionStrings.html
---

# AutonomousDatabaseConnectionStrings
<a name="API_AutonomousDatabaseConnectionStrings"></a>

The connection strings used to connect to an Autonomous Database.

## Contents
<a name="API_AutonomousDatabaseConnectionStrings_Contents"></a>

 ** allConnectionStrings **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-allConnectionStrings"></a>
The list of all connection strings that you can use to connect to the Autonomous Database.
Type: String to string map
Required: No

 ** dedicated **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-dedicated"></a>
The connection string for connecting to the Autonomous Database with a dedicated service.
Type: String
Required: No

 ** high **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-high"></a>
The connection string for the high-priority database service.
Type: String
Required: No

 ** low **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-low"></a>
The connection string for the low-priority database service.
Type: String
Required: No

 ** medium **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-medium"></a>
The connection string for the medium-priority database service.
Type: String
Required: No

 ** profiles **   <a name="odb-Type-AutonomousDatabaseConnectionStrings-profiles"></a>
The list of connection string profiles for the Autonomous Database.
Type: Array of [DatabaseConnectionStringProfile](API_DatabaseConnectionStringProfile.md) objects
Required: No

## See Also
<a name="API_AutonomousDatabaseConnectionStrings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabaseConnectionStrings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabaseConnectionStrings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabaseConnectionStrings)
