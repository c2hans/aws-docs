---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_EnvironmentSummary.html
---

# EnvironmentSummary
<a name="API_EnvironmentSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Contains a subset of the possible runtime environment attributes. Used in the environment list.

## Contents
<a name="API_EnvironmentSummary_Contents"></a>

 ** creationTime **   <a name="m2-Type-EnvironmentSummary-creationTime"></a>
The timestamp when the runtime environment was created.
Type: Timestamp
Required: Yes

 ** engineType **   <a name="m2-Type-EnvironmentSummary-engineType"></a>
The target platform for the runtime environment.
Type: String
Valid Values: `microfocus | bluage`
Required: Yes

 ** engineVersion **   <a name="m2-Type-EnvironmentSummary-engineVersion"></a>
The version of the runtime engine.
Type: String
Pattern: `\S{1,10}`
Required: Yes

 ** environmentArn **   <a name="m2-Type-EnvironmentSummary-environmentArn"></a>
The Amazon Resource Name (ARN) of a particular runtime environment.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** environmentId **   <a name="m2-Type-EnvironmentSummary-environmentId"></a>
The unique identifier of a particular runtime environment.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** instanceType **   <a name="m2-Type-EnvironmentSummary-instanceType"></a>
The instance type of the runtime environment.
Type: String
Pattern: `\S{1,20}`
Required: Yes

 ** name **   <a name="m2-Type-EnvironmentSummary-name"></a>
The name of the runtime environment.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** status **   <a name="m2-Type-EnvironmentSummary-status"></a>
The status of the runtime environment
Type: String
Valid Values: `Creating | Available | Updating | Deleting | Failed | UnHealthy`
Required: Yes

 ** networkType **   <a name="m2-Type-EnvironmentSummary-networkType"></a>
The network type supported by the runtime environment.
Type: String
Valid Values: `ipv4 | dual`
Required: No

## See Also
<a name="API_EnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/EnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/EnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/EnvironmentSummary)
