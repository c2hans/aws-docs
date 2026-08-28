---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ValidationExceptionError.html
---

# ValidationExceptionError
<a name="API_ValidationExceptionError"></a>

Indicates an invalid value for a field.
+  *REQUIRED\_FIELD\_MISSING:* The request is missing a required field.

  Fix: Verify your request payload includes all required fields.
+  *INVALID\_ENUM\_VALUE:* The enum field value isn't an accepted values.

  Fix: Check the documentation for the list of valid enum values, and update your request with a valid value.
+  *INVALID\_STRING\_FORMAT:* The string format is invalid.

  Fix: Confirm that the string is in the expected format (For example: email address, date).
+  *INVALID\_VALUE:* The value isn't valid.

  Fix: Confirm that the value meets the expected criteria and is within the allowable range or set.
+  *TOO\_MANY\_VALUES:* There are too many values in a field that expects fewer entries.

  Fix: Reduce the number of values to match the expected limit.
+  *NOT\_ENOUGH\_VALUES:* There are not enough values in a field that expects more entries.

  Fix: Increase the number of values to match the expected threshold.
+  *ACTION\_NOT\_PERMITTED:* The action isn't permitted due to current state or permissions.

  Fix: Verify that the action is appropriate for the current state, and that you have the necessary permissions to perform it.
+  *DUPLICATE\_KEY\_VALUE:* The value in a field duplicates a value that must be unique.

  Fix: Verify that the value is unique and doesn't duplicate an existing value in the system.

## Contents
<a name="API_ValidationExceptionError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="AWSPartnerCentral-Type-ValidationExceptionError-Code"></a>
Specifies the error code for the invalid field value.
Type: String
Valid Values: `REQUIRED_FIELD_MISSING | INVALID_ENUM_VALUE | INVALID_STRING_FORMAT | INVALID_VALUE | NOT_ENOUGH_VALUES | TOO_MANY_VALUES | INVALID_RESOURCE_STATE | DUPLICATE_KEY_VALUE | VALUE_OUT_OF_RANGE | ACTION_NOT_PERMITTED`
Required: Yes

 ** Message **   <a name="AWSPartnerCentral-Type-ValidationExceptionError-Message"></a>
Specifies the detailed error message for the invalid field value.
Type: String
Required: Yes

 ** FieldName **   <a name="AWSPartnerCentral-Type-ValidationExceptionError-FieldName"></a>
Specifies the field name with the invalid value.
Type: String
Required: No

## See Also
<a name="API_ValidationExceptionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ValidationExceptionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ValidationExceptionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ValidationExceptionError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
