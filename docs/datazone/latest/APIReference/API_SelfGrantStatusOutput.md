---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SelfGrantStatusOutput.html
---

# SelfGrantStatusOutput
<a name="API_SelfGrantStatusOutput"></a>

The details for the self granting status for a data source.

## Contents
<a name="API_SelfGrantStatusOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glueSelfGrantStatus **   <a name="datazone-Type-SelfGrantStatusOutput-glueSelfGrantStatus"></a>
The details for the self granting status for a Glue data source.
Type: [GlueSelfGrantStatusOutput](API_GlueSelfGrantStatusOutput.md) object
Required: No

 ** redshiftSelfGrantStatus **   <a name="datazone-Type-SelfGrantStatusOutput-redshiftSelfGrantStatus"></a>
The details for the self granting status for an Amazon Redshift data source.
Type: [RedshiftSelfGrantStatusOutput](API_RedshiftSelfGrantStatusOutput.md) object
Required: No

## See Also
<a name="API_SelfGrantStatusOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SelfGrantStatusOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SelfGrantStatusOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SelfGrantStatusOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
