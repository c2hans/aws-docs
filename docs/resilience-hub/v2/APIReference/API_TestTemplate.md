---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestTemplate.html
---

# TestTemplate
<a name="API_TestTemplate"></a>

A pre-configured, AWS recommended test that defines which resilience capability to validate, the fault actions it runs, and the parameters it accepts.

## Contents
<a name="API_TestTemplate_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-TestTemplate-name"></a>
The name of the test template.
Type: String
Required: Yes

 ** testTemplateArn **   <a name="ngresiliencehub-Type-TestTemplate-testTemplateArn"></a>
The ARN of the test template.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** actions **   <a name="ngresiliencehub-Type-TestTemplate-actions"></a>
The fault actions the test template runs.
Type: Array of [TestAction](API_TestAction.md) objects
Required: No

 ** description **   <a name="ngresiliencehub-Type-TestTemplate-description"></a>
A description of the test template.
Type: String
Required: No

 ** parameters **   <a name="ngresiliencehub-Type-TestTemplate-parameters"></a>
The parameters the test template accepts.
Type: Array of [TestTemplateParameter](API_TestTemplateParameter.md) objects
Required: No

## See Also
<a name="API_TestTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestTemplate)
