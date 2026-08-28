---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_HomeRegionControl.html
---

# HomeRegionControl
<a name="API_HomeRegionControl"></a>

A home region control is an object that specifies the home region for an account, with some additional information. It contains a target (always of type `ACCOUNT`), an ID, and a time at which the home region was set.

## Contents
<a name="API_HomeRegionControl_Contents"></a>

 ** ControlId **   <a name="migrationhubhomeregion-Type-HomeRegionControl-ControlId"></a>
A unique identifier that's generated for each home region control. It's always a string that begins with "hrc-" followed by 12 lowercase letters and numbers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^hrc-[a-z0-9]{12}$`
Required: No

 ** HomeRegion **   <a name="migrationhubhomeregion-Type-HomeRegionControl-HomeRegion"></a>
The AWS Region that's been set as home region. For example, "us-west-2" or "eu-central-1" are valid home regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([a-z]+)-([a-z]+)-([0-9]+)$`
Required: No

 ** RequestedTime **   <a name="migrationhubhomeregion-Type-HomeRegionControl-RequestedTime"></a>
A timestamp representing the time when the customer called `CreateHomeregionControl` and set the home region for the account.
Type: Timestamp
Required: No

 ** Target **   <a name="migrationhubhomeregion-Type-HomeRegionControl-Target"></a>
The target parameter specifies the identifier to which the home region is applied, which is always an `ACCOUNT`. It applies the home region to the current `ACCOUNT`.
Type: [Target](API_Target.md) object
Required: No

## See Also
<a name="API_HomeRegionControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/HomeRegionControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/HomeRegionControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/HomeRegionControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-home-region` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
