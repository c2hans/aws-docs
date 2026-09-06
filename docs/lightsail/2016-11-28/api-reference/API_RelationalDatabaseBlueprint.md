---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseBlueprint.html
---

# RelationalDatabaseBlueprint
<a name="API_RelationalDatabaseBlueprint"></a>

Describes a database image, or blueprint. A blueprint describes the major engine version of a database.

## Contents
<a name="API_RelationalDatabaseBlueprint_Contents"></a>

 ** blueprintId **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-blueprintId"></a>
The ID for the database blueprint.
Type: String
Required: No

 ** engine **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-engine"></a>
The database software of the database blueprint (for example, `MySQL`).
Type: String
Valid Values: `mysql`
Required: No

 ** engineDescription **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-engineDescription"></a>
The description of the database engine for the database blueprint.
Type: String
Required: No

 ** engineVersion **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-engineVersion"></a>
The database engine version for the database blueprint (for example, `5.7.23`).
Type: String
Required: No

 ** engineVersionDescription **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-engineVersionDescription"></a>
The description of the database engine version for the database blueprint.
Type: String
Required: No

 ** isEngineDefault **   <a name="Lightsail-Type-RelationalDatabaseBlueprint-isEngineDefault"></a>
A Boolean value indicating whether the engine version is the default for the database blueprint.
Type: Boolean
Required: No

## See Also
<a name="API_RelationalDatabaseBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabaseBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabaseBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabaseBlueprint)
