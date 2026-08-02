---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DynamicSsmParameterValue.html
---

# DynamicSsmParameterValue
<a name="API_DynamicSsmParameterValue"></a>

The dynamic SSM parameter value.

## Contents
<a name="API_DynamicSsmParameterValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** variable **   <a name="IncidentManager-Type-DynamicSsmParameterValue-variable"></a>
Variable dynamic parameters. A parameter value is determined when an incident is created.
Type: String
Valid Values: `INCIDENT_RECORD_ARN | INVOLVED_RESOURCES`
Required: No

## See Also
<a name="API_DynamicSsmParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/DynamicSsmParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/DynamicSsmParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/DynamicSsmParameterValue)
