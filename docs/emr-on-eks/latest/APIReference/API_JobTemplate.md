---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobTemplate.html
---

# JobTemplate
<a name="API_JobTemplate"></a>

This entity describes a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

## Contents
<a name="API_JobTemplate_Contents"></a>

 ** jobTemplateData **   <a name="emroneks-Type-JobTemplate-jobTemplateData"></a>
The job template data which holds values of StartJobRun API request.
Type: [JobTemplateData](API_JobTemplateData.md) object
Required: Yes

 ** arn **   <a name="emroneks-Type-JobTemplate-arn"></a>
The ARN of the job template.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/jobtemplates\/[0-9a-zA-Z]+$`
Required: No

 ** createdAt **   <a name="emroneks-Type-JobTemplate-createdAt"></a>
 The date and time when the job template was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="emroneks-Type-JobTemplate-createdBy"></a>
 The user who created the job template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+$`
Required: No

 ** decryptionError **   <a name="emroneks-Type-JobTemplate-decryptionError"></a>
The error message in case the decryption of job template fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** id **   <a name="emroneks-Type-JobTemplate-id"></a>
The ID of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** kmsKeyArn **   <a name="emroneks-Type-JobTemplate-kmsKeyArn"></a>
 The KMS key ARN used to encrypt the job template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
Required: No

 ** name **   <a name="emroneks-Type-JobTemplate-name"></a>
The name of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** tags **   <a name="emroneks-Type-JobTemplate-tags"></a>
The tags assigned to the job template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_JobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/JobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/JobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/JobTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
