---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an application that has one configuration template named `default` and no application versions.

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application. Must be unique within your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **
Your description of the application.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** ResourceLifecycleConfig **
Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
Type: [ApplicationResourceLifecycleConfig](API_ApplicationResourceLifecycleConfig.md) object
Required: No

 **Tags.member.N**
Specifies the tags applied to the application.
Elastic Beanstalk applies these tags only to the application. Environments that you create in the application don't inherit the tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

The following element is returned by the service.

 ** Application **
 The [ApplicationDescription](API_ApplicationDescription.md) of the application.
Type: [ApplicationDescription](API_ApplicationDescription.md) object

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TooManyApplications **
The specified account has reached its limit of applications.
HTTP Status Code: 400

## Examples
<a name="API_CreateApplication_Examples"></a>

### Example
<a name="API_CreateApplication_Example_1"></a>

This example illustrates one usage of CreateApplication.

#### Sample Request
<a name="API_CreateApplication_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&Description=Sample%20Description
&Operation=CreateApplication
&AuthParams
```

#### Sample Response
<a name="API_CreateApplication_Example_1_Response"></a>

```
<CreateApplicationResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CreateApplicationResult>
    <Application>
      <Versions/>
      <Description>Sample Description</Description>
      <ApplicationName>SampleApp</ApplicationName>
      <DateCreated>2010-11-16T23:09:20.256Z</DateCreated>
      <DateUpdated>2010-11-16T23:09:20.256Z</DateUpdated>
      <ConfigurationTemplates>
        <member>Default</member>
      </ConfigurationTemplates>
    </Application>
  </CreateApplicationResult>
  <ResponseMetadata>
    <RequestId>8b00e053-f1d6-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CreateApplicationResponse>
```

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreateApplication)
