---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AwsLocation.html
---

# AwsLocation
<a name="API_AwsLocation"></a>

The location of a project.

## Contents
<a name="API_AwsLocation_Contents"></a>

 ** accessRole **   <a name="datazone-Type-AwsLocation-accessRole"></a>
The access role of a connection.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

 ** awsAccountId **   <a name="datazone-Type-AwsLocation-awsAccountId"></a>
The account ID of a connection.
Type: String
Pattern: `\d{12}`
Required: No

 ** awsRegion **   <a name="datazone-Type-AwsLocation-awsRegion"></a>
The Region of a connection.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: No

 ** iamConnectionId **   <a name="datazone-Type-AwsLocation-iamConnectionId"></a>
The IAM connection ID of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_AwsLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AwsLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AwsLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AwsLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
