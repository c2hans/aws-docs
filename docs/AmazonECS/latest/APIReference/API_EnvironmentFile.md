---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_EnvironmentFile.html
---

# EnvironmentFile
<a name="API_EnvironmentFile"></a>

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored.

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they're processed from the top down. We recommend that you use unique variable names. For more information, see [Use a file to pass environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-environment-file.html) in the *Amazon Elastic Container Service Developer Guide*.

Environment variable files are objects in Amazon S3 and all Amazon S3 security considerations apply.

You must use the following platforms for the Fargate launch type:
+ Linux platform version `1.4.0` or later.
+ Windows platform version `1.0.0` or later.

Consider the following when using the Fargate launch type:
+ The file is handled like a native Docker env-file.
+ There is no support for shell escape handling.
+ The container entry point interperts the `VARIABLE` values.

## Contents
<a name="API_EnvironmentFile_Contents"></a>

 ** type **   <a name="ECS-Type-EnvironmentFile-type"></a>
The file type to use. Environment files are objects in Amazon S3. The only supported value is `s3`.
Type: String
Valid Values: `s3`
Required: Yes

 ** value **   <a name="ECS-Type-EnvironmentFile-value"></a>
The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.
Type: String
Required: Yes

## See Also
<a name="API_EnvironmentFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/EnvironmentFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/EnvironmentFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/EnvironmentFile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
