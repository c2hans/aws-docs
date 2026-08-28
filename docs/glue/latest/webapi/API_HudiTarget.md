---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_HudiTarget.html
---

# HudiTarget
<a name="API_HudiTarget"></a>

Specifies an Apache Hudi data source.

## Contents
<a name="API_HudiTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-HudiTarget-ConnectionName"></a>
The name of the connection to use to connect to the Hudi target. If your Hudi files are stored in buckets that require VPC authorization, you can set their connection properties here.
Type: String
Required: No

 ** Exclusions **   <a name="Glue-Type-HudiTarget-Exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
Type: Array of strings
Required: No

 ** MaximumTraversalDepth **   <a name="Glue-Type-HudiTarget-MaximumTraversalDepth"></a>
The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Hudi metadata folder in your Amazon S3 path. Used to limit the crawler run time.
Type: Integer
Required: No

 ** Paths **   <a name="Glue-Type-HudiTarget-Paths"></a>
An array of Amazon S3 location strings for Hudi, each indicating the root folder with which the metadata files for a Hudi table resides. The Hudi folder may be located in a child folder of the root folder.
The crawler will scan all folders underneath a path for a Hudi folder.
Type: Array of strings
Required: No

## See Also
<a name="API_HudiTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/HudiTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/HudiTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/HudiTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
