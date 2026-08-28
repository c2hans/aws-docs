---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentInfoDescription.html
---

# EnvironmentInfoDescription
<a name="API_EnvironmentInfoDescription"></a>

The information retrieved from the Amazon EC2 instances.

## Contents
<a name="API_EnvironmentInfoDescription_Contents"></a>

 ** Ec2InstanceId **
The Amazon EC2 Instance ID for this information.
Type: String
Required: No

 ** InfoType **
The type of information retrieved.
Type: String
Valid Values: `tail | bundle`
Required: No

 ** Message **
The retrieved information. Currently contains a presigned Amazon S3 URL. The files are deleted after 15 minutes.
Anyone in possession of this URL can access the files before they are deleted. Make the URL available only to trusted parties.
Type: String
Required: No

 ** SampleTimestamp **
The time stamp when this information was retrieved.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentInfoDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/EnvironmentInfoDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/EnvironmentInfoDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/EnvironmentInfoDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
