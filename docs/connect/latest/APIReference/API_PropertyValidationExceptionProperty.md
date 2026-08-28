---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PropertyValidationExceptionProperty.html
---

# PropertyValidationExceptionProperty
<a name="API_PropertyValidationExceptionProperty"></a>

Contains information about why a property is not valid.

## Contents
<a name="API_PropertyValidationExceptionProperty_Contents"></a>

 ** Message **   <a name="connect-Type-PropertyValidationExceptionProperty-Message"></a>
A message describing why the property is not valid.
Type: String
Required: Yes

 ** PropertyPath **   <a name="connect-Type-PropertyValidationExceptionProperty-PropertyPath"></a>
The full property path.
Type: String
Required: Yes

 ** Reason **   <a name="connect-Type-PropertyValidationExceptionProperty-Reason"></a>
Why the property is not valid.
Type: String
Valid Values: `INVALID_FORMAT | UNIQUE_CONSTRAINT_VIOLATED | REFERENCED_RESOURCE_NOT_FOUND | RESOURCE_NAME_ALREADY_EXISTS | REQUIRED_PROPERTY_MISSING | NOT_SUPPORTED | TYPE_MISMATCH`
Required: Yes

## See Also
<a name="API_PropertyValidationExceptionProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PropertyValidationExceptionProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PropertyValidationExceptionProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PropertyValidationExceptionProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
