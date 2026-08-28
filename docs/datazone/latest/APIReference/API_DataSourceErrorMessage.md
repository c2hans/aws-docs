---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceErrorMessage.html
---

# DataSourceErrorMessage
<a name="API_DataSourceErrorMessage"></a>

The details of the error message that is returned if the operation cannot be successfully completed.

## Contents
<a name="API_DataSourceErrorMessage_Contents"></a>

 ** errorType **   <a name="datazone-Type-DataSourceErrorMessage-errorType"></a>
The type of the error message that is returned if the operation cannot be successfully completed.
Type: String
Valid Values: `ACCESS_DENIED_EXCEPTION | CONFLICT_EXCEPTION | INTERNAL_SERVER_EXCEPTION | RESOURCE_NOT_FOUND_EXCEPTION | SERVICE_QUOTA_EXCEEDED_EXCEPTION | THROTTLING_EXCEPTION | VALIDATION_EXCEPTION`
Required: Yes

 ** errorDetail **   <a name="datazone-Type-DataSourceErrorMessage-errorDetail"></a>
The details of the error message that is returned if the operation cannot be successfully completed.
Type: String
Required: No

## See Also
<a name="API_DataSourceErrorMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceErrorMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceErrorMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceErrorMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
