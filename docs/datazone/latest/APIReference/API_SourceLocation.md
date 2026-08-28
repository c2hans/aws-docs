---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SourceLocation.html
---

# SourceLocation
<a name="API_SourceLocation"></a>

The source location for a notebook import in Amazon SageMaker Unified Studio.

## Contents
<a name="API_SourceLocation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="datazone-Type-SourceLocation-s3"></a>
The Amazon Simple Storage Service URI of the notebook source file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://.+`
Required: No

## See Also
<a name="API_SourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SourceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SourceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SourceLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
