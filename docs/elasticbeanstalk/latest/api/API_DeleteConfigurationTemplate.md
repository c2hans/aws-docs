---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteConfigurationTemplate.html
---

# DeleteConfigurationTemplate
<a name="API_DeleteConfigurationTemplate"></a>

Deletes the specified configuration template.

**Note**
When you launch an environment using a configuration template, the environment gets a copy of the template. You can delete or modify the environment's copy of the template without affecting the running environment.

## Request Parameters
<a name="API_DeleteConfigurationTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application to delete the configuration template from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** TemplateName **
The name of the configuration template to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Errors
<a name="API_DeleteConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationInProgressFailure **
Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.
HTTP Status Code: 400

## Examples
<a name="API_DeleteConfigurationTemplate_Examples"></a>

### Example
<a name="API_DeleteConfigurationTemplate_Example_1"></a>

This example illustrates one usage of DeleteConfigurationTemplate.

#### Sample Request
<a name="API_DeleteConfigurationTemplate_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=SampleAppTemplate
&Operation=DeleteConfigurationTemplate
&AuthParams
```

#### Sample Response
<a name="API_DeleteConfigurationTemplate_Example_1_Response"></a>

```
<DeleteConfigurationTemplateResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>af9cf1b6-f25e-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DeleteConfigurationTemplateResponse>
```

## See Also
<a name="API_DeleteConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DeleteConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
