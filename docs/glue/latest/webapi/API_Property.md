---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Property.html
---

# Property
<a name="API_Property"></a>

An object that defines a connection type for a compute environment.

## Contents
<a name="API_Property_Contents"></a>

 ** Description **   <a name="Glue-Type-Property-Description"></a>
A description of the property.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** Name **   <a name="Glue-Type-Property-Name"></a>
The name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** PropertyTypes **   <a name="Glue-Type-Property-PropertyTypes"></a>
Describes the type of property.
Type: Array of strings
Valid Values: `USER_INPUT | SECRET | READ_ONLY | UNUSED | SECRET_OR_USER_INPUT`
Required: Yes

 ** Required **   <a name="Glue-Type-Property-Required"></a>
Indicates whether the property is required.
Type: Boolean
Required: Yes

 ** AllowedValues **   <a name="Glue-Type-Property-AllowedValues"></a>
A list of `AllowedValue` objects representing the values allowed for the property.
Type: Array of [AllowedValue](API_AllowedValue.md) objects
Required: No

 ** DataOperationScopes **   <a name="Glue-Type-Property-DataOperationScopes"></a>
Indicates which data operations are applicable to the property.
Type: Array of strings
Valid Values: `READ | WRITE`
Required: No

 ** DefaultValue **   <a name="Glue-Type-Property-DefaultValue"></a>
The default value for the property.
Type: String
Required: No

 ** KeyOverride **   <a name="Glue-Type-Property-KeyOverride"></a>
A key name to use when sending this property in API requests, if different from the display name.
Type: String
Required: No

 ** PropertyLocation **   <a name="Glue-Type-Property-PropertyLocation"></a>
Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.
Type: String
Valid Values: `HEADER | BODY | QUERY_PARAM | PATH`
Required: No

## See Also
<a name="API_Property_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Property)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Property)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Property)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
