---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DevEndpointCustomLibraries.html
---

# DevEndpointCustomLibraries
<a name="API_DevEndpointCustomLibraries"></a>

Custom libraries to be loaded into a development endpoint.

## Contents
<a name="API_DevEndpointCustomLibraries_Contents"></a>

 ** ExtraJarsS3Path **   <a name="Glue-Type-DevEndpointCustomLibraries-ExtraJarsS3Path"></a>
The path to one or more Java `.jar` files in an S3 bucket that should be loaded in your `DevEndpoint`.
You can only use pure Java/Scala libraries with a `DevEndpoint`.
Type: String
Required: No

 ** ExtraPythonLibsS3Path **   <a name="Glue-Type-DevEndpointCustomLibraries-ExtraPythonLibsS3Path"></a>
The paths to one or more Python libraries in an Amazon Simple Storage Service (Amazon S3) bucket that should be loaded in your `DevEndpoint`. Multiple values must be complete paths separated by a comma.
You can only use pure Python libraries with a `DevEndpoint`. Libraries that rely on C extensions, such as the [pandas](http://pandas.pydata.org/) Python data analysis library, are not currently supported.
Type: String
Required: No

## See Also
<a name="API_DevEndpointCustomLibraries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DevEndpointCustomLibraries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DevEndpointCustomLibraries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DevEndpointCustomLibraries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
