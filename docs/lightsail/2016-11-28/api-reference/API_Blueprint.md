---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Blueprint.html
---

# Blueprint
<a name="API_Blueprint"></a>

Describes a blueprint (a virtual private server image).

## Contents
<a name="API_Blueprint_Contents"></a>

 ** appCategory **   <a name="Lightsail-Type-Blueprint-appCategory"></a>
Virtual computer blueprints that are supported by Lightsail for Research.
This parameter only applies to Lightsail for Research resources.
Type: String
Valid Values: `LfR`
Required: No

 ** blueprintId **   <a name="Lightsail-Type-Blueprint-blueprintId"></a>
The ID for the virtual private server image (`app_wordpress_x_x` or `app_lamp_x_x`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** description **   <a name="Lightsail-Type-Blueprint-description"></a>
The description of the blueprint.
Type: String
Required: No

 ** group **   <a name="Lightsail-Type-Blueprint-group"></a>
The group name of the blueprint (`amazon-linux`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** isActive **   <a name="Lightsail-Type-Blueprint-isActive"></a>
A Boolean value indicating whether the blueprint is active. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.
Type: Boolean
Required: No

 ** licenseUrl **   <a name="Lightsail-Type-Blueprint-licenseUrl"></a>
The end-user license agreement URL for the image or blueprint.
Type: String
Required: No

 ** minPower **   <a name="Lightsail-Type-Blueprint-minPower"></a>
The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. `0` indicates that the blueprint runs on all instance sizes.
Type: Integer
Required: No

 ** name **   <a name="Lightsail-Type-Blueprint-name"></a>
The friendly name of the blueprint (`Amazon Linux`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** platform **   <a name="Lightsail-Type-Blueprint-platform"></a>
The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.
Type: String
Valid Values: `LINUX_UNIX | WINDOWS`
Required: No

 ** productUrl **   <a name="Lightsail-Type-Blueprint-productUrl"></a>
The product URL to learn more about the image or blueprint.
Type: String
Required: No

 ** type **   <a name="Lightsail-Type-Blueprint-type"></a>
The type of the blueprint (`os` or `app`).
Type: String
Valid Values: `os | app`
Required: No

 ** version **   <a name="Lightsail-Type-Blueprint-version"></a>
The version number of the operating system, application, or stack ( `2016.03.0`).
Type: String
Required: No

 ** versionCode **   <a name="Lightsail-Type-Blueprint-versionCode"></a>
The version code.
Type: String
Required: No

## See Also
<a name="API_Blueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Blueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Blueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Blueprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
