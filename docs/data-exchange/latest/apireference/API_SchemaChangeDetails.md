---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SchemaChangeDetails.html
---

# SchemaChangeDetails
<a name="API_SchemaChangeDetails"></a>

Object encompassing information about a schema change to a single, particular field, a notification can have up to 100 of these.

## Contents
<a name="API_SchemaChangeDetails_Contents"></a>

 ** Name **   <a name="dataexchange-Type-SchemaChangeDetails-Name"></a>
Name of the changing field. This value can be up to 255 characters long.
Type: String
Required: Yes

 ** Type **   <a name="dataexchange-Type-SchemaChangeDetails-Type"></a>
Is the field being added, removed, or modified?
Type: String
Valid Values: `ADD | REMOVE | MODIFY`
Required: Yes

 ** Description **   <a name="dataexchange-Type-SchemaChangeDetails-Description"></a>
Description of what's changing about this field. This value can be up to 512 characters long.
Type: String
Required: No

## See Also
<a name="API_SchemaChangeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/SchemaChangeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/SchemaChangeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/SchemaChangeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
