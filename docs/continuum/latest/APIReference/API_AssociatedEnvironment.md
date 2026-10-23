---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_AssociatedEnvironment.html
---

# AssociatedEnvironment
<a name="API_AssociatedEnvironment"></a>

The associated Environment.

## Contents
<a name="API_AssociatedEnvironment_Contents"></a>

 ** createdAt **   <a name="continuum-Type-AssociatedEnvironment-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** environmentArn **   <a name="continuum-Type-AssociatedEnvironment-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`
Required: Yes

 ** environmentId **   <a name="continuum-Type-AssociatedEnvironment-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** name **   <a name="continuum-Type-AssociatedEnvironment-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.\-]{0,254}`
Required: Yes

 ** status **   <a name="continuum-Type-AssociatedEnvironment-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE`
Required: Yes

## See Also
<a name="API_AssociatedEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/AssociatedEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/AssociatedEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/AssociatedEnvironment)
