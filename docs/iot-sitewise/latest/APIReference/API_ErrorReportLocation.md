---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ErrorReportLocation.html
---

# ErrorReportLocation
<a name="API_ErrorReportLocation"></a>

The Amazon S3 destination where errors associated with the job creation request are saved.

## Contents
<a name="API_ErrorReportLocation_Contents"></a>

 ** bucket **   <a name="iotsitewise-Type-ErrorReportLocation-bucket"></a>
The name of the Amazon S3 bucket to which errors associated with the bulk import job are sent.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** prefix **   <a name="iotsitewise-Type-ErrorReportLocation-prefix"></a>
Amazon S3 uses the prefix as a folder name to organize data in the bucket. Each Amazon S3 object has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/). For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.
Type: String
Required: Yes

## See Also
<a name="API_ErrorReportLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ErrorReportLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ErrorReportLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ErrorReportLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
