---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddMaintenance.html
---

# AddMaintenance
<a name="API_AddMaintenance"></a>

 Create a maintenance setting for a flow.

## Contents
<a name="API_AddMaintenance_Contents"></a>

 ** maintenanceDay **   <a name="mediaconnect-Type-AddMaintenance-maintenanceDay"></a>
 A day of a week when the maintenance will happen.
Type: String
Valid Values: `Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday`
Required: Yes

 ** maintenanceStartHour **   <a name="mediaconnect-Type-AddMaintenance-maintenanceStartHour"></a>
 UTC time when the maintenance will happen.
Use 24-hour HH:MM format.
Minutes must be 00.
Example: 13:00.
The default value is 02:00.
Type: String
Required: Yes

## See Also
<a name="API_AddMaintenance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AddMaintenance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AddMaintenance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AddMaintenance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
